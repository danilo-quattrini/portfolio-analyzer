
transaction_categories = set()

def get_categories():
    return transaction_categories

def set_category(category):
    transaction_categories.update(category)
    