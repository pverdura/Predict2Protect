# src/train.py - Trains and stores the medication model

import pandas as pd                                         # For managing data
from sklearn.ensemble import HistGradientBoostingClassifier # For training and managing the model
import pickle                                               # For storing the data

import model    # Trains the model
import params   # General metadata


### INTERSECTS BOTH DATASETS ###
def join_df(df_allele, df_patient):
    # We change the data frame index to ID
    df_allele  = df_allele.rename(columns={df_allele.columns[0]: "ID"})
    df_allele  = df_allele.set_index('ID')

    # We are interested in 'RM profunda' (treatment) and
    # TODO: duration
    df_patient = df_patient.set_index('ID')
    df_patient = df_patient.loc[:, ['RM profunda (BCR/ABL < 001%)']]
    
    # We intersect the databases
    df_allele = pd.merge(df_allele, df_patient, how='left', on="ID")

    # We divide the dataset between input and output
    y = df_allele[["RM profunda (BCR/ABL < 001%)"]]
    X = df_allele.drop(columns=["RM profunda (BCR/ABL < 001%)"])

    return X, y


### MAIN FUNCTION ###
def __main__():
    # Read and process the data
    df_allele = pd.read_csv(params.path+"/"+params.train_allele, sep=params.csv_sep)
    df_patient = pd.read_csv(params.path+"/"+params.train_patient, sep=params.csv_sep)

    X, y = join_df(df_allele, df_patient)


if 0:
    # TODO:
    # We train the model with the data
    reg, cols, loss = model.train(X, y)

    X_encoded = model.preprocess_one_hot(X, columns_trained=cols)
    y_prob = model.predict_probability(reg, X_encoded)

    df_pred = X.copy()  # inclou les columnes originals
    df_pred['pred_prob_class_1'] = y_prob
    df_pred['pred_class'] = (y_prob >= 0.5).astype(int)

    df_pred.to_csv("prediccions.csv", index=False)
    print("CSV de prediccions generat a: prediccions.csv")

    # We store the trained model in <path_model+name>
    filename = params.path_model+params.train_file[:-4]+".sav"

    pickle.dump(reg, open(filename, 'wb'))



__main__()
