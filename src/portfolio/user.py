from .validator import validated_user

def presentation_menu():
    print("""
|------------------------------------------------------------|
|   Welcome to Portfolio Analyzer!                           |
|   An easy script to track and                              |
|   analyze your daily expenses,income                       |
|------------------------------------------------------------|
""")

def user_initialization():
    presentation_menu()
    
    while True:
        name = input("What's your name?\n=> ")
        budget = input("What's your budget for this month?\n=> ")
        starting_currency = input("What's your initial balance?\n=> ")
        
        error = validated_user(name, budget, starting_currency)
        
        if error and error.get("error"):
            print(error.get("message"))
        else:
            return {
                "name": name, 
                "budget": float(budget), 
                "starting_currency": float(starting_currency)
            }