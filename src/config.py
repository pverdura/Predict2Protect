# config.py - Python script to configure the environment. Modifies the file 
#             src/params.py and creates the folders if they don't exist

__PATH__ = "path"
__FILE__ = "file"
__CHAR__ = "character"


'''
' Pre: A string that contains a line of a file
'  - line: A non empty string
'
' Post: Returns an array defining the parameter of the line
'  - param_id: ID of the parameter
'  - param_type: Type of parameter
'  - param: Content of that parameter
'''
def get_param(line):
    param_name = line.split(' ')[0]
    param_id = param_name.split('_')[0].lower()
    param = line.split('"')[1]

    if (param_name == "DATA_DIR"): param_type = __PATH__
    elif (param_name == "ALLELE_DATA"): param_type = __FILE__
    elif (param_name == "PATIENT_DATA"): param_type = __FILE__
    elif (param_name == "MODEL_DIR"): param_type = __PATH__
    elif (param_name == "CSV_SEP"): param_type = __CHAR__
    else:
        # We stop the program if we detect an unidentified
        # parameter in the file 
        print("Error: Unidintified parameter " + param_name)
        exit()
    
    return param_id, param_type, param


'''
' Pre: A line from a file
'  - 'line': A string
'
' Post: Returns a boolean that informs if the line contains a parameter
'''
def is_param(line):
    return len(line) > 0 and line[0] != '#'


'''
' Pre: The answer from the user
'  - 'response': A string
'
' Post: Checks if the user agrees with the question
'''
def agree(response):
    return len(response) == 0 or response == 'y' or response == 'Y'


'''
' Pre: A path
'  - path: A string
'
' Post: Returns the path standardized for the application
'''
def standardize_path(path):
    if (path[-1] == '/'):
        path = path[:-1]
    return path


'''
' Main function of the program
'''
def __main__():
    # We read the contents of the file with the parameters
    with open('./src/params.py') as file:
        lines = [line.rstrip() for line in file]
    
    # We create an empty buffer where we will store the
    # new content of the file
    file_content = ""

    # For each line we check if it contains a parameter and
    # ask if the user wants to change it
    for line in lines:
        # We add a new line to the file
        if file_content != "":
            file_content += "\n"

        if is_param(line):
            param_id, param_type, param = get_param(line)

            # We ask if the user wants to modify the parameter
            if (param_type == __PATH__):
                print("The name of the path that contains the "
                      + param_id + " is '" + param + "'")
            elif (param_type == __FILE__):
                print("The name of the file that contains the "
                      + param_id + " data is '" + param + "'")
            elif (param_type == __CHAR__):
                print("The separator used in the "
                      + param_id + " files is '" + param + "'")
            else:
                print("Error: Undefined parameter")
                exit()
        
            # We ask if the user wants to change the parameter
            response = input("Do you want to change it? [Y/n] ")

            # We check if the user agrees and update the file
            if agree(response):
                response = ""
                
                # We keep requesting the response until the user types it
                while response == "":
                    response = input("Enter the new " + param_type + ": ")

                # If the parameter is a directory we format the path
                # (if needed) for the application
                if (param_type == __PATH__):
                    response = standardize_path(response)

                # We update the line
                file_content += (line.split('=')[0] + '= "' + response + '"')

            # Otherwise we keep it as it was
            else:
                file_content += line

        # If the line does not contain a parameter we keep it as it was
        else:
            file_content += line

    
    # We update the content of the file
    with open("./src/params.py", "w") as params:
        params.write(file_content)

    print("\nAll parameters were updated successfully!")


__main__()
