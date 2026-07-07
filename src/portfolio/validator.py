from validator_collection import validators

""" 
Function that validate user information

:param name: the name of the user to validate as a string
:param budge: the budge to validate as a floating point number
:param starting_currency: the start currency to validate as a floating point number

:return: an error message str or a dictionary with user information
"""
def validated_user(name, budget, starting_currency):
    if not string(name, 6, 12):
        return {
            "error": True,
            "message": "The name of the user it's incorrect!",
        }
    
    if not float_number(budget):
        return {
            "error": True,
            "message": "Budget value it's incorrect, must be a number!!",
        }
    
    if not float_number(starting_currency):
        return {
            "error": True,
            "message": "Start currency it's incorrect format, must be a number!",
        }
   
def string(str, min_char, max_char): 
    try:
        validators.string(str, False, False, min_char, max_char, False)
        return True
    except:
        return False

def float_number(number): 
    try:
        validators.float(number)
        return True
    except:
        return False