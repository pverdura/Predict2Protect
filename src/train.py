# src/train.py - Trains and stores the medication model

import pandas as pd                                         # For managing data
from sklearn.ensemble import HistGradientBoostingClassifier # For training and managing the model
import pickle                                               # For storing the data
import os                                                   # For managing storage

import model    # Trains the model
import params   # General metadata


def get_days(start_day, end_day):
    # We remove the patients that miss data
    days = pd.merge(start_day.dropna(),
                    end_day.dropna(),
                    how = 'inner', on = 'ID')
    
    # We rename the columns
    cols = days.columns
    days = days.rename(columns={cols[0]: "start", cols[1]: "end"})

    # We calculate how many samples we removed
    num_removed = start_day.shape[0] - days.shape[0]

    # We convert the data type from string to datetime
    start = pd.to_datetime(days['start'], format="%d/%m/%Y")
    end = pd.to_datetime(days['end'], format="%d/%m/%Y")


    # We calculate the time interval
    days = end.subtract(start)

    # We restore the patients that contain missing data
    days = pd.concat([start_day, days], axis=1).iloc[:,1].dt.days

    # We assign a negative number to the patients that lack data
    days = days.fillna(-1)

    return days


### INTERSECTS BOTH DATASETS ###
def join_df(df_allele, df_patient):
    # We change the data frame index to ID
    df_allele  = df_allele.rename(columns={df_allele.columns[0]: "ID"})
    df_allele  = df_allele.set_index('ID')

    df_patient = df_patient.set_index('ID') 

    # We calculate how many days the patients spent with their first stage treatment
    df_patient['days_treatment'] = get_days(df_patient['INICIO ITC 1Âª LINEA'],
                                            df_patient['FIN ITC 1Âª LINEA'])

    # We are interested in 'RM profunda' (treatment) and 
    # the duration of the treatment
    df_patient = df_patient.loc[:, ['RM profunda (BCR/ABL < 001%)']]
    
    # We intersect the databases
    df_allele = pd.merge(df_allele, df_patient, how='left', on="ID")

    # We remove the patients that contain no data
    df_allele = df_allele.dropna()

    # We divide the dataset between input and output
    y = df_allele[["RM profunda (BCR/ABL < 001%)"]]
    X = df_allele.drop(columns=["RM profunda (BCR/ABL < 001%)"])

    return X, y



### CREATES A NEW FILENAME TO NOT OVERWRITE PREVIOUS DATA ###
def new_savename(filename, extension):
    new_name = filename
    counter = 1

    # We try not to overwrite previous models so we want to compare them
    while os.path.isfile(new_name + extension):
        new_name = filename + "-" + str(counter)
        counter += 1

    return new_name + extension



### MAIN FUNCTION ###
def __main__():
    # Read and process the data
    df_allele = pd.read_csv(params.DATA_DIR+"/"+params.ALLELE_DATA, sep=params.CSV_SEP)
    df_patient = pd.read_csv(params.DATA_DIR+"/"+params.PATIENT_DATA, sep=params.CSV_SEP)
    
    X, y = join_df(df_allele, df_patient)

    # TODO:
    # We train the model with the data
    reg, cols, loss = model.train(X, y)

    X_encoded = model.preprocess_one_hot(X, columns_trained=cols)
    y_prob = model.predict_probability(reg, X_encoded)

    df_pred = X.copy()  # inclou les columnes originals
    df_pred['pred_prob_class_1'] = y_prob
    df_pred['pred_class'] = (y_prob >= 0.5).astype(int)

    # We store the predicted data
    filename = new_savename(model_dir + "/" + "predictions", ".csv")
    df_pred.to_csv(filename, index=True)
    print("Predictions generated at: " + model_dir + "predictions.csv")

    # We store the trained model
    filename = new_savename(params.model_dir + '/' + "model", ".sav")

    pickle.dump(reg, open(filename, 'wb'))



__main__()
