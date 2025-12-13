import pandas as pd                                         # For managing data
from sklearn.ensemble import HistGradientBoostingClassifier # For training and managing the model
from skl2onnx import to_onnx                                # For storing the data

import model


def __main__():
    path = "../data"
    file = "data.csv"
    # Read and process the data
    df = pd.read_csv(path+"/"+file, sep=",")

    ids = ''
    for i in df:
        ids = i

    print(df)
    y = df[ids]
    X = df.drop(columns=[ids])
    
    # We train the model with the data
    reg, cols, loss = model.train(X, y)

    # We store the trained model
    name = file[:-4]
    print(name)
    onx = to_onnx(reg, X[:1])
    with open(path+"/.models/"+name, "wb") as f:
        f.write(onx.SerializeToString())




__main__()
