import pandas as pd                                         # For managing data
from sklearn.ensemble import HistGradientBoostingClassifier # For training and managing the model
import pickle                                               #  For storing the data

import model
import params


def __main__():
    # Read and process the data
    df = pd.read_csv(params.path+"/"+params.train_file, sep=",")

    ids = ''
    for i in df:
        ids = i

    y = df[ids]
    X = df.drop(columns=[ids])
    
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
