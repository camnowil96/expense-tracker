# This is a program that tracks expenses
# Add an expense
# View expenses
# Calculate total expenses
# Save and view data

#import all the good stuff
import json 
from datetime import datetime
#declare variables
expense = {} 
#Function to add a new expense
def new_expense():
    global confirm_expense 
    num_entries = int(input('How many expenses would you like to log?: '))
    for i in range(num_entries):
        expenseDate = input('Enter expense date (mm-dd-yyyy): ')
        expenseDate_new = datetime.strptime(expenseDate, '%m-%d-%Y')
        expenseDate_new.strftime('%m-%d-%Y')
        expenseCategory = input('Enter the expense category: ')
        expenseCost = float(input('Enter the cost: $'))
        expenseDescription = input('Enter a description: ')
        expense[expenseDate] = expenseCategory.capitalize(), expenseCost, expenseDescription.capitalize()
        print('New Expenses: ' , expense)
        confirm_expense = input('Save entry? Select Y to continue, N to start over, or Exit to return to the main menu: ')
#main menu function
print('Hello there. Welcome to your Expense Tracker. ')
def main_menu():   
    menuOption = input('Choose from the following:\nView tracker -1\nAdd Expense  -2\n')     
    if menuOption == '1': 
    #insert view tracker function
        print('View Tracker')
    elif menuOption == '2':
    #call new expense function
        new_expense()
    else:
        x = 0
        while x < 1: 
            print("Sorry. I didn't catch that. \n")
            x += 1
        else:
            main_menu()  
#call main menu function      
main_menu()

#Call add expense function 
if confirm_expense.lower() == 'y':
    json_object = json.dumps(expense)
    with open("tracker.json" , "a+") as f:
        json.dump(json_object, f)
elif confirm_expense.lower() == 'n':
    print()
    new_expense()
else:
    main_menu()

#view tracker function
def viewTracker():
    json.loads(json)
    json.dumps()
#function to calculate expenses