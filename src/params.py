path          = "../data"  # Relative path of the file
train_allele  = "data.csv" # Name of the file used to train the model
train_patient = "patients.csv"
valid_file    = "data.csv" # Name of the file used to validate the model
model_dir     = ".model"   # Folder for storing the trained models
csv_sep       = ","

# We standardize the paths
if path[-1] == '/':
    path = path[:-1]

if model_dir[-1] == '/':
    model_dir = model_dir[:1-]

path_model = path + "/"+model_dir+"/"

