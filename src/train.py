import pandas as pd                                         # For managing data
from sklearn.ensemble import HistGradientBoostingClassifier # For training and managing the model
import pickle                                               #  For storing the data

import model
import params

def join_df(df_allele, df_person):
    # We change the data frame index to ID
    df_allele = df_allele.rename(columns={df_allele.columns[0]: "ID"})
    df_allele = df_allele.set_index('ID')
    df_person = df_person.set_index('ID')

    df_allele = pd.merge(df_allele, df_person, how='left', on="ID")

    y = df_allele[["RM profunda (BCR/ABL < 001%)"]]
    X = df_allele.drop(columns=["RM profunda (BCR/ABL < 001%)"])

    return X, y


def __main__():
    # Read and process the data
    df_allele = pd.read_csv(params.path+"/"+params.train_allele, sep=";")
    df_person = pd.read_csv(params.path+"/"+params.train_patient, sep=";")

    X, y = join_df(df_allele, df_person)

if 0:
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
