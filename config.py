# config.py - Python script to configure the environment. Modifies the file 
#             src/params.py and creates the folders if they don't exist

import os

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

def agree(confirm):
    return len(confirm) == 0 or confirm == 'y' or confirm == 'Y'


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
if not os.path.isdir(path):
    confirm = input(red("Warning: The folder " + path + " does not exist!\n") +
                    "Do you want to create the directory '" + path + "'? [Y/n] ")
    if agree(confirm):
        os.mkdir(path)
        print(green("Directory " + path + " created successfully"))



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
                        "Do you want the default option: 'patient.csv'? [Y/n] ")
        if agree(confirm):
            patient_data = 'patient.csv'
            introduced = True
    else:
        introduced = True
        


### CSV SEPARATOR ###

introduced = False

while not introduced:
    csv_sep = input("Type of csv separator:\n")

    # We check if the user typed any input
    if len(csv_sep) == 0:

        # If empty we ask if the default option is wanted
        confirm = input(red("Warning: No separator introduced!\n") +
                        "Do you want the separator ';'? [Y/n] ")
        if agree(confirm):
            csv_sep = ';'
            introduced = True
    else:
        introduced = True



### WE WRITE THE DATA IN './src/params.py' ###

# We standardize the paths
if path[-1] == '/':
    path = path[:-1]

# If the path is not an absolute path (starts with '/' or '~')
# we will edit the path so code inside './src' can read it
if path[0] != '/' and path[0] != '~':
    path = "../" + path

with open("./src/params.py", "w") as params:
    params.write("path         = \"" + path +
                 f"\"\t# Relative path of the file\n" +
                 "allele_data  = \"" + allele_data +
                 f"\"\t# Name of the file that contains the allele data\n" +
                 "patient_data = \"" + patient_data +
                 f"\"\t# Name of the file that contains the patient data\n" +
                 "valid_file   = \"" + allele_data +
                 f"\"\t# Name of the file used to validate the model\n" +
                 "model_dir    = \"" + "../model" +
                 f"\"\t# Folder for storing the trained models\n" +
                 "csv_sep      = \"" + csv_sep +
                 f"\"\t# Character that separates the CSV elements\n"
                 )

print(green("All parameters are written in 'src/params.py'"))
