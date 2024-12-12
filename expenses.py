# This is a program that tracks expenses
# Add an expense
# View expenses
# Calculate total expenses
# Save and view data

#import all the good stuff
import json 
from datetime import datetime

#main menu function
print('Hello there. Welcome to your Expense Tracker. ')
def main_menu():   
    menuOption = input('Choose from the following:\nView tracker -1\nAdd Expense  -2\n')     
    if menuOption == '1': 
    #insert view tracker function
        print('View Tracker')
    elif menuOption == '2':
    #insert Add Expense function
        print('Add Expense')
    else:
        x = 0
        while x < 1: 
            print("Sorry. I didn't catch that. \n")
            x += 1
        else:
            main_menu()
main_menu()  
#Date function 
#declare an empty list 
expense = []

expense_date = input('Enter expense date: ')
expense_date_new = datetime.strptime(expense_date, '%m-%d-%Y')

#converts date to string and adds to expense list
expense.append(expense_date_new.strftime('%m-%d-%Y'))
#converts expense list into a JSON string 
expenseReport = json.dumps(expense)
print(expenseReport)

#declare variables
# expenseCategory = input('Category:')
# expenseDate = input('Date: ')
# expenseCost = input('Cost: ')

#function to add expenses

#function to view expenses

#function to calculate expenses