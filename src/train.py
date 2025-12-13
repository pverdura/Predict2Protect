import pandas as pd                                         # For managing data
from sklearn.ensemble import HistGradientBoostingClassifier # For training and managing the model
from skl2onnx import to_onnx                                # For storing the data

import model
import params


def __main__():
    # Read and process the data
    df = pd.read_csv(params.path+"/"+params.file, sep=",")

    ids = ''
    for i in df:
        ids = i

    print(df)
    y = df[ids]
    X = df.drop(columns=[ids])
    
    # We train the model with the data
    reg, cols, loss = model.train(X, y)
'''
    # We store the trained model
    name = params.file[:-4]
    print(name)
    onx = to_onnx(reg, X[:1])
    with open(path+"/.models/"+name, "wb") as f:
        f.write(onx.SerializeToString())'''




__main__()
