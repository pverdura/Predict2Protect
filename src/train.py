import pandas as pd
import numpy as np
from sklearn.ensemble import HistGradientBoostingClassifier as gb

import model


def __main__():
    df = pd.read_csv("../data/data.csv", sep=",")
    
    gb = model.train(df)

    


__main__()
