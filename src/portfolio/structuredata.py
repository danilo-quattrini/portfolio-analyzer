from .cleaner import clean_data
from .translator import check_dictionary, open_dictionary
from collections import defaultdict
from transactions import set_category
transactions = defaultdict(int)

""" 
From a list of cleaned data into a format [[name, price],...]
it will structure them into a dictionary grouping them for the key name
and as its value the total.
"""
def struct_data():
    data = clean_data()    
    dictionary = open_dictionary("transactions-dictionary.json")
     
    for name, price in data:
        proper_name = check_dictionary(name, dictionary)
        
        if proper_name:
            name = proper_name
        
        if not price or price == "null":
            continue
    
        transactions[name] += float(price)
        
    set_category(transactions.keys())
    return transactions