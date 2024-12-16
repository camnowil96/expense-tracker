# This is a program that tracks expenses
# Add an expense
# View expenses
# Calculate total expenses
# Save and view data

#import all the good stuff
import json 
from datetime import datetime

#view tracker function
def viewTracker():
    try:
        # Load all expenses from the JSON file
        with open("tracker.json", "r") as f:
            tracker = json.load(f)  # Load the JSON array
        if not tracker:
            print("No expenses to display. Add an expense first!")
            return
        print("Expense Tracker:")
        for entry in tracker:
            print(json.dumps(entry, indent=4))  # Nicely formatted output    
        #tracker menu options                      
        trackerMenu = input('1 - View tracker options\n2 - Return to main menu\n')
        if trackerMenu == '1':
            subMenu = input('1 - Filter\n2 - Calculate total\n')
            if subMenu == '1':
                print('Filter tracker by:\n')
                menu_options = input('1 - Date\n2 - Category\n3 - Cost\n4 - Exit\n')
                if menu_options == '1':
                    with open('tracker.json') as f:
                        data = json.load(f)
                # Flatten the data into a list of details, adding the date to each entry
                        flattened_expenses = []
                        for expense in data:
                            for date, details in expense.items():
                                details["Date"] = date  # Add the date as part of the details
                                flattened_expenses.append(details)
                        # Sort the flattened list by "Category"
                        sorted_expenses = sorted(flattened_expenses, key=lambda k: datetime.strptime(k["Date"], "%m-%d-%Y"))
                        # Display the sorted expenses
                        print("Expenses sorted by date:")
                        for expense in sorted_expenses:
                            print(f"Date: {expense['Date']}, Category: {expense['Category']}, Cost: ${expense['Cost']}, Description: {expense['Description']}")
                elif menu_options == '2':
                    with open('tracker.json') as f:
                        data = json.load(f)
                # Flatten the data into a list of details, adding the date to each entry
                    flattened_expenses = []
                    for expense in data:
                        for date, details in expense.items():
                            details["Date"] = date  # Add the date as part of the details
                            flattened_expenses.append(details)
                    # Sort the flattened list by "Category"
                    sorted_expenses = sorted(flattened_expenses, key=lambda k: k["Category"])
                    # Display the sorted expenses
                    print("Expenses sorted by category:")
                    for expense in sorted_expenses:
                        print(f"Date: {expense['Date']}, Category: {expense['Category']}, Cost: ${expense['Cost']}, Description: {expense['Description']}")
                elif menu_options == '3':
                       with open('tracker.json') as f:
                        data = json.load(f)
                # Flatten the data into a list of details, adding the date to each entry
                        flattened_expenses = []
                        for expense in data:
                            for date, details in expense.items():
                                details["Date"] = date  # Add the date as part of the details
                                flattened_expenses.append(details)
                        # Sort the flattened list by "Category"
                        sorted_expenses = sorted(flattened_expenses, key=lambda k: k["Cost"])
                        # Display the sorted expenses
                        print("Expenses sorted by cost:")
                        for expense in sorted_expenses:
                            print(f"Date: {expense['Date']}, Category: {expense['Category']}, Cost: ${expense['Cost']}, Description: {expense['Description']}")
                else:
                    print('Returning to tracker...')
                    viewTracker()
            elif subMenu == '2':
                print('Calculating total...')
                with open('tracker.json', 'r') as f:
                    data = json.load(f)
                total = 0
                for expense in data:
                    for date, details in expense.items():
                        total += details["Cost"]
                now = datetime.now()
                dateOnly = now.strftime('%m-%d-%Y')
                print('Your total as of ' + str(dateOnly) + ' is: $' + str(round(total, 2)))
                print('Returning to tracker...')
                viewTracker()
        else: 
            main_menu()       
    except FileNotFoundError:
        print('No expenses found. Add an expense first')  
    except json.JSONDecodeError:
        print('The tracker file is empty or corrupted. Add an expense. ')

#Function to add a new expense
def new_expense():
    expense = {} 
    # global confirm_expense 
    num_entries = int(input('How many expenses would you like to log?: '))
    for i in range(num_entries):
        expenseDate = input('Enter expense date (mm-dd-yyyy): ')
        expenseDate_new = datetime.strptime(expenseDate, '%m-%d-%Y').strftime('%m-%d-%Y')
        expenseCategory = input('Enter the expense category: ')
        expenseCost = float(input('Enter the cost: $'))
        expenseDescription = input('Enter a description: ')
        expense[expenseDate_new] = {
            "Category": expenseCategory.capitalize(), 
            "Cost": expenseCost, 
            "Description": expenseDescription.capitalize()
        }
        print('New Expenses: ' , expense)
    confirm_expense = input('Save entry? Select Y to continue, N to start over, or Exit to return to the main menu: ')
    return confirm_expense, expense
#main menu function
print('Hello there. Welcome to your Expense Tracker. ')
def main_menu():   
    menuOption = input('Choose from the following:\nView tracker -1\nAdd Expense  -2\n')     
    if menuOption == '1': 
    #insert view tracker function
        viewTracker()
    elif menuOption == '2':
        confirm_expense, expense = new_expense()
        if confirm_expense.lower() == 'y':
            save_to_json(expense)
        elif confirm_expense.lower() == 'n':
            new_expense()
    else:
        x = 0
        while x < 1: 
            print("Sorry. I didn't catch that. \n")
            x += 1
        else:
            main_menu()  
def save_to_json(expense):
    try:
        # Try to load existing data
        with open('tracker.json', 'r') as f:
            try:
                data = json.load(f)  # Load the JSON array
            except json.JSONDecodeError:
                print("The tracker file is corrupted. Initializing a new tracker.")
                data = []  # If corrupted, start fresh
    except FileNotFoundError:
        # Initialize as an empty list if the file doesn't exist
        data = []
    # Add the new expense(s) to the list
    data.append(expense)
    # Write the updated list back to the file
    with open('tracker.json', 'w') as f:
        json.dump(data, f, indent=4)  # Pretty-print with indentation
    print("Expenses saved!")
#call main menu function      
main_menu()

