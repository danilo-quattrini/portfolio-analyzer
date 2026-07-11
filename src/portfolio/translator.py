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
Check if a specific string it's in the 
dictionary as key, and return its value

:param string: the string to check if is int the translator-dictionary
"""    
def check_dictionary(string):
    dictionary = open_dictionary("transactions-dictionary.json") 
    
    for name, abbreviation in dictionary.items():
        if string.startswith(tuple(abbreviation)):
            return name