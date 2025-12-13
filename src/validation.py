import onnx


import params

def __main__():
    name = params.valid_file[:-4]

    onnx_model = onnx.load(params.path_model+name+".onnx")

__main__()
