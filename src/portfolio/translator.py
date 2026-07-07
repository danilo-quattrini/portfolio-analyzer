import json
""" 
Open a file that will be converted into a dictionary with json.load(file)
"""
def open_dictionary(dictionary):
    try:
        with open(dictionary, "r") as file:
            return json.load(file)
    except FileNotFoundError:      
        print(f"Error: '{dictionary}' file was not found.")

""" 
Check if a specific string it's in the dictionary
as key, and return its value
"""    
def check_dictionary(string):
    dictionary = open_dictionary("transactions-dictionary.json") 
    
    print(string.startswith(tuple(dictionary.keys())))
    """ if string.startswith(tuple(dictionary.values())):
        return True """

print(check_dictionary("ut."))