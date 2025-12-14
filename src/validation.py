import pandas as pd                                         # For managing data
from sklearn.ensemble import HistGradientBoostingClassifier # For training and managing the model
import pickle                                               # For storing the data

import params


def __main__():
    # We read the file with the data to validate
    df = pd.read_csv(params.path+"/"+params.valid_file, sep=",")

    # We load the pre-trained model 
    filename = params.path_model+params.valid_file[:-4]+".sav"
    
    model = pickle.load(open(filename, 'rb'))



__main__()
