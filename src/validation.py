import pandas as pd
from sklearn.ensemble import HistGradientBoostingClassifier
import pickle

import params


def __main__():
    # Read validation data
    df = pd.read_csv(params.path + "/" + params.valid_file, sep=",")

    # Load trained model
    filename = params.path_model + params.valid_file[:-4] + ".sav"
    model = pickle.load(open(filename, 'rb'))

    # Predict probability of the positive class
    y_proba = model.predict_proba(df)[:, 1]

    # Save probabilities to CSV
    output_file = params.path + "/predictions_" + params.valid_file
    pd.DataFrame({"proba_positive_class": y_proba}).to_csv(output_file, index=False)


__main__()


