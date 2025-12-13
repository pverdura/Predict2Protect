import pandas as pd                                         # For managing data
from sklearn.ensemble import HistGradientBoostingClassifier # For training and managing the model
from skl2onnx import to_onnx                                # For storing the data
from skl2onnx import convert_sklearn
from skl2onnx.common.data_types import FloatTensorType

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

    # We store the trained model in <path_model+name>
    name = params.train_file[:-4]

    initial_type = [('input', FloatTensorType([None, X.shape[1]]))]

    onx = convert_sklearn(reg, initial_types=initial_type)

    with open(params.path_model+name+".onnx", "wb") as f:
        f.write(onx.SerializeToString())




__main__()
