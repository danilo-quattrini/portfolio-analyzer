from validator import validated_user

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
    
    name = input("What's your name?\n=> ")
    budget = float(input("What's your budget for this month?\n=> "))
    starting_currency = float(input("What's your initial balance?\n=> "))

    