from cleaner import clean_data
from collections import defaultdict
from translator import check_dictionary

transactions = defaultdict(int)

def struct_data():
    data = clean_data()    
    
    for name, price in data:
        proper_name = check_dictionary(name)
        
        if proper_name and proper_name.startswith(name):
            name  = proper_name
        
        if not price or price == "null":
            continue
    
        transactions[name] += float(price)

struct_data()
print(transactions)