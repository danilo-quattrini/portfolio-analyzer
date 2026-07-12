from .cleaner import clean_data
from collections import defaultdict
from transactions import set_category
transactions = defaultdict(int)

def struct_data():
    data = clean_data()    
    
    for name, price in data:
        proper_name = check_dictionary(name)
        
        if proper_name:
            name = proper_name
        
        if not price or price == "null":
            continue
    
        transactions[name] += float(price)
        
    set_category(transactions.keys())
    return transactions