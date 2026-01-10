# config.py - Python script to configure the environment. Modifies the file 
#             src/params.py and creates the folders if they don't exist

import os

# Functions for coloring text
class font:
    GREEN = '\033[92m'  # For printing green text
    RED = '\033[91m'    # For printing red text
    BOLD = '\033[1m'    # For prining bold text
    END = '\033[0m'     # For printing default text

def bold(string):
    return f"{font.BOLD}" + string + f"{font.END}"

def red(string):
    return f"{font.RED}" + string + f"{font.END}"

def green(string):
    return f"{font.GREEN}" + string + f"{font.END}"


# Functions that manage the inputs
def agree(confirm):
    return len(confirm) == 0 or confirm == 'y' or confirm == 'Y'

def manage_directory(directory):
    if not os.path.isdir(directory):
        confirm = input(red("Warning: The directory " + directory + " does not exist!\n") +
                    "Do you want to create the directory '" + directory + "'? [Y/n] ")
        if agree(confirm):
            os.makedirs(directory)
            print(green("The directory " + directory + " was created successfully!\n"))

def standardize_path(_path):
    if _path[-1] == '/':
        _path = _path[:-1]
    return _path


### PATH INPUT ###

introduced = False

while not introduced:
    path = input(bold("PATH") + " of the folder that contains the data:\n")
    
    # We check if the user typed any path
    if len(path) == 0:
        # If empty we ask if the default option is wanted
        confirm = input(red("Warning: No path introduced!\n") + 
                        "Do you want the default path: './data'? [Y/n] ")
        if agree(confirm):
            path = './data'
            introduced = True
    else:
        introduced = True

# We check if the directory exists
manage_directory(path)



### ALLELE INPUT ###

introduced = False

while not introduced: 
    allele_data = input(f"Name of of the file with the " + bold("ALLELE DATA") + ":\n")

    # We check if the user typed any input
    if len(allele_data) == 0:
        # If empty we ask if the default option is wanted
        confirm = input(red("Warning: No file introduced!\n") + 
                            "Do you want the default option: 'allele.csv'? [Y/n] ")
        if agree(confirm):
            allele_data = 'allele.csv'
            introduced = True
    else:
        introduced = True



### PATIENT INPUT ###

introduced = False

while not introduced:
    patient_data = input(f"\nName of the file with the " + bold("PATIENT DATA") + ":\n")
    
    # We check if the user typed any input
    if len(patient_data) == 0:
        # If empty we ask if the default option is wanted
        confirm = input(red("Warning: No file introduced!\n") +
                        "Do you want the default option: 'patients.csv'? [Y/n] ")
        if agree(confirm):
            patient_data = 'patients.csv'
            introduced = True
    else:
        introduced = True
        


### MODEL DIRECTORY ###

introduced = False

while not introduced:
    model_dir = input("Type the folder that will contain the trained model:\n")
    
    # We check if the user typed any path
    if len(model_dir) == 0:
        # If empty we ask if the default option is wanted
        confirm = input(red("Warning: No path introduced!\n") + 
                        "Do you want the default path: './model'? [Y/n] ")
        if agree(confirm):
            model_dir = './model'
            introduced = True
    else:
        introduced = True

# We check if the directory exists
manage_directory(model_dir)



### CSV SEPARATOR ###

introduced = False

while not introduced:
    csv_sep = input("Type of csv separator:\n")

    # We check if the user typed any input
    if len(csv_sep) == 0:

        # If empty we ask if the default option is wanted
        confirm = input(red("Warning: No separator introduced!\n") +
                        "Do you want the separator ','? [Y/n] ")
        if agree(confirm):
            csv_sep = ','
            introduced = True
    else:
        introduced = True



### WE WRITE THE DATA IN './src/params.py' ###

# We standardize the paths
path = standardize_path(path)
model_dir = standardize_path(model_dir)

with open("./src/params.py", "w") as params:
    params.write("# src/params.py - Environment parameters\n\n" +
                 "path         = \"" + path +
                 f"\"\t# Relative path of the file\n" +
                 "allele_data  = \"" + allele_data +
                 f"\"\t# Name of the file that contains the allele data\n" +
                 "patient_data = \"" + patient_data +
                 f"\"\t# Name of the file that contains the patient data\n" +
                 "valid_file   = \"" + allele_data +
                 f"\"\t# Name of the file used to validate the model\n" +
                 "model_dir    = \"" + model_dir +
                 f"\"\t# Folder for storing the trained models\n" +
                 "csv_sep      = \"" + csv_sep +
                 f"\"\t# Character that separates the CSV elements\n"
                )

print(green("All parameters are written in 'src/params.py'"))
