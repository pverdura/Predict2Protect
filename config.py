# config.py - Python script to configure the environment. Modifies the file 
#             src/params.py and creates the folders if they don't exist

import os

class font:
    CYAN = '\033[96m'   # For printing cyan text
    GREEN = '\033[92m'  # For printing green text
    RED = '\033[91m'    # For printing red text
    BOLD = '\033[1m'    # For prining bold text
    END = '\033[0m'     # For printing default text


### PATH INPUT ###

introduced = False

while not introduced:
    path = input(f"{font.BOLD}PATH{font.END} of the folder that contains the data:\n")
    
    # We check if the user typed any path
    if len(path) == 0:
        # If empty we ask if wants the default path
        confirm = input(f"{font.RED}Warning: No path introduced.{font.END}\n" + 
                        "Default path: '../data'? [Y/n] ")
        if len(confirm) == 0 or confirm == 'y' or confirm == 'Y':
            path = '../data'
            introduced = True

        print(f"{font.GREEN}Folder set to '" + path + f"'.{font.END}\n")

        # We check id the directory exists
        if not os.path.isdir(path):
            confirm = input(f"{font.RED}Warning: The folder " + path + " does not exist!\n" +
                            f"{font.END}Do you want to create the folder " + path + "? [Y/n] ")
            if len(confirm) == 0 or confirm == 'y' or confirm == 'Y':
                os.mkdir(path)
                print(f"{font.GREEN}Directory " + path + f" created successfully.{font.END}")
                introduced = True
        else:
            introduced = True




### ALLELE INPUT ###

allele_data = ""

while len(allele_data) == 0:
    allele_data = input(f"Name of the CSV file that contains the {font.BOLD}ALLELE DATA{font.END}:\n")
    print(f"{font.RED}Warning: No file introduced!{font.END}")


### PATIENT INPUT ###

patient_data = ""

while len(patient_data) == 0:
    patient_data = input(f"\nName of the CSV file that contains the {font.BOLD}PATIENT DATA{font.END}:\n")
    print(f"{font.RED}Warning: File required!{font.END}")

### CSV SEPARATOR ###

csv_sep = ""
introduced = False

while not introduced:
    csv_sep = input(f"\CSV separator for the CSV files:\n")
    if len(csv_sep) == 0:
        confirm = input(f"{font.RED}Warning: No separator introduced!{font.END}\n" +
                        "Do you want the separator ';'? [Y/n] ")
        if len(confirm) == 0 or confirm == 'y' or confirm == 'Y':
            csv_sep = ';'
            introduced = True
    else:
        introduced = True

### WE WRITE THE DATA IN './src/params.py' ###




