# src/model.py - Base code of the model

import pandas as pd                                         # For managing data
import numpy as np                                          # For basic functions
from sklearn.ensemble import HistGradientBoostingClassifier # For training and managing the model
from sklearn.model_selection import KFold                   
from sklearn.metrics import log_loss

def preprocess_one_hot(X, columns_trained=None):
    """
    One-hot encoding for alleles, handling NaN as 'ABSENT' and '+' as 'PRESENT'.
    If columns_trained is provided, aligns the new DataFrame to the training columns.
    """
    X_encoded = pd.DataFrame()
    
    for col in X.columns:
        X[col] = X[col].astype(str).replace("nan", "ABSENT").replace("+", "PRESENT")
        one_hot = X[col].str.split("/", expand=True).stack()
        one_hot.name = col
        one_hot = pd.get_dummies(one_hot, prefix=col)
        one_hot = one_hot.groupby(level=0).max()
        X_encoded = pd.concat([X_encoded, one_hot], axis=1)
    
    if columns_trained is not None:
        for col in columns_trained:
            if col not in X_encoded.columns:
                X_encoded[col] = 0
        X_encoded = X_encoded[columns_trained]
    
    return X_encoded

def predict_probability(model, X_new):
    """
    Predict probability of class 1 (not relapsing) for new patients.
    """
    y_prob = model.predict_proba(X_new)[:, 1]
    return y_prob

def train(X, y, n_splits=5, random_state=42):
    """
    Train HistGradientBoostingClassifier with cross-validation.
    
    Parameters:
        X: DataFrame with features (alleles)
        y: Series or array with target values (0 or 1)
        n_splits: number of folds for KFold CV
        random_state: for reproducibility
    
    Returns:
        model_trained: classifier trained on all data
        columns: one-hot encoded columns (for preprocessing new patients)
        avg_logloss: mean log-loss over CV folds
    """
    # One-hot encoding
    X_encoded = preprocess_one_hot(X)
    
    # Cross-validation
    kf = KFold(n_splits=n_splits, shuffle=True, random_state=random_state)
    logloss_scores = []
    
    for train_idx, val_idx in kf.split(X_encoded):
        X_train, X_val = X_encoded.iloc[train_idx], X_encoded.iloc[val_idx]
        y_train, y_val = y.iloc[train_idx], y.iloc[val_idx]
        
        model_cv = HistGradientBoostingClassifier(random_state=random_state)
        model_cv.fit(X_train, y_train)
        
        # Log-loss correcte amb totes les probabilitats
        y_prob_all = model_cv.predict_proba(X_val)
        logloss_scores.append(log_loss(y_val, y_prob_all))
    
    avg_logloss = np.mean(logloss_scores)
    print(f"Cross-Validation Log-Loss (average over {n_splits} folds): {avg_logloss:.4f}")
    
    # Entrenar model final sobre totes les dades
    model_trained = HistGradientBoostingClassifier(random_state=random_state)
    model_trained.fit(X_encoded, y)
    
    return model_trained, X_encoded.columns, avg_logloss
