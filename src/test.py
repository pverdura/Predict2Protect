import pandas as pd
from model import *  # importa la teva funció train(X, y) i helpers

# -----------------------------
# Llegir X i y
# -----------------------------
X = pd.read_csv("X.csv")       # Assegura't que X.csv està al mateix directori
y = pd.read_csv("y.csv").squeeze()  # .squeeze() converteix DataFrame en Series

# -----------------------------
# Entrenar el model
# -----------------------------
model_trained, columns, avg_logloss = train(X, y)

# Mostrar resultats
print("Columns used for one-hot encoding:")
print(columns)
print("\nAverage cross-validation log-loss:", avg_logloss)

# -----------------------------
# Preprocessar X i obtenir prediccions de probabilitat
# -----------------------------
X_encoded = preprocess_one_hot(X, columns_trained=columns)
y_prob = predict_probability(model_trained, X_encoded)  # probabilitat de no recaure

# Afegir les prediccions al DataFrame original
X_with_predictions = X.copy()
X_with_predictions["predicted_prob_not_relapsing"] = y_prob

# Mostrar les primeres 10 prediccions
print("\nPredictions for the first 10 patients:")
print(X_with_predictions.head(10))

# -----------------------------
# Opcional: ordenar per risc de recaiguda
# -----------------------------
X_sorted = X_with_predictions.sort_values(by="predicted_prob_not_relapsing")
print("\nTop 10 patients with highest risk of relapse:")
print(X_sorted.head(10)[["predicted_prob_not_relapsing"]])
