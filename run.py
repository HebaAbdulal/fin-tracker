from rich.console import Console
from rich.table import Table
from rich.style import Style
import os
from datetime import datetime
import gspread
from google.oauth2.service_account import Credentials


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('fin-tracker')

console = Console()

def clear_terminal():
    """
    Clears the terminal window prior to new content.
    """
    os.system('cls' if os.name == 'nt' else 'clear')

def get_amount():
    """
    Get the amount of income and validate that it is a positive number.
    """
    while True:
        amount_str = input("Enter the amount of income: ")
        try:
            amount = float(amount_str)
            if amount <= 0:
                print("Invalid amount: Amount must be a positive number.")
            else:
                return amount
        except ValueError:
            print("Invalid amount: Please enter a valid number.")

def get_description():
    """
    Get the description of income and validate that it contains only letters.
    """
    while True:
        description = input("Enter the description of income: ")
        if description.isalpha():
            return description
        else:
            print("Invalid description: Description must contain only letters.")

def get_date():
    """
    Get the date of income and validate that it is in the correct format.
    """
    while True:
        date_str = input("Enter the date of income (YYYY-MM-DD): ")
        try:
            datetime.strptime(date_str, '%Y-%m-%d')
            return date_str
        except ValueError:
            print("Invalid date format. Please enter the date in the format 'YYYY-MM-DD'.")

def get_income_data():
    """
    Get income data from the user
    """

    print("Please enter income data.")

    # Get amount
    amount = get_amount()

    # Get description
    description = get_description()

    # Get date
    date = get_date()

    income_data = [amount, description, date]

    return income_data

def update_income_worksheet(data):
    """
    Update income worksheet, add new row with the income data provided.
    """
    print("Updating incomee worksheet...\n")
    income_worksheet = SHEET.worksheet("income")
    income_worksheet.append_row(data)
    print("Income worksheet updated successfully.\n")

def calculate_total_income():
    """
    Calculate the total incomes recorded in the income worksheet.
    """
    income_worksheet = SHEET.worksheet("income")
    incomes = income_worksheet.get_all_values()
    total_incomes = 0
    for row in incomes[1:]:  # Skip header row
        try:
            total_incomes += float(row[0])  # Assuming Amount is in the first column
        except ValueError:
            print(f"Skipping non-numeric value: {row[0]}")
    return total_incomes

def display_income_data():
    """
    Display all income data from the income worksheet.
    """
    print("Displaying income data...\n")
    income_worksheet = SHEET.worksheet("income")
    incomes = income_worksheet.get_all_values()
    for row in incomes:
        print(row)

def calculate_incomes():
    """
    Calculate incomes by displaying total incomes and income data.
    """
    total_incomes = calculate_total_income()
    print(f"Total Incomes: ${total_incomes:.2f}\n")
    display_income_data()

def get_expense_amount():
    """
    Get the amount of expenses and validate that it is a positive number.
    """
    while True:
        amount_str = input("Enter the amount of expenses: ")
        try:
            amount = float(amount_str)
            if amount <= 0:
                print("Invalid amount: Amount must be a positive number.")
            else:
                return amount
        except ValueError:
            print("Invalid amount: Please enter a valid number.")

def get_expense_description():
    """
    Get the description of expenses and validate that it contains only letters.
    """
    while True:
        description = input("Enter the description of expenses: ")
        if description.replace(' ', '').isalpha():
            return description
        else:
            print("Invalid description: Description must contain only letters.")

def get_expense_date():
    """
    Get the date of expenses and validate that it is in the correct format.
    """
    while True:
        date_str = input("Enter the date of expenses (YYYY-MM-DD): ")
        try:
            datetime.strptime(date_str, '%Y-%m-%d')
            return date_str
        except ValueError:
            print("Invalid date format. Please enter the date in the format 'YYYY-MM-DD'.")

def get_expenses_data():
    """
    Get expenses data from the user
    """

    print("Please enter expenses data.")

    # Get amount
    amount = get_expense_amount()

    # Get description
    description = get_expense_description()

    # Get date
    date = get_expense_date()

    expenses_data = [amount, description, date]

    return expenses_data

def update_expenses_worksheet(data):
    """
    Update expense worksheet, add new row with the expense data provided.
    """
    print("Updating expense worksheet...\n")
    expenses_worksheet = SHEET.worksheet("expenses")
    expenses_worksheet.append_row(data)
    print("Expense worksheet updated successfully.\n")

def calculate_total_expenses():
    """
    Calculate the total expenses recorded in the expenses worksheet.
    """
    expense_worksheet = SHEET.worksheet("expenses")
    expenses = expense_worksheet.get_all_values()
    total_expenses = 0
    for row in expenses[1:]:  # Skip header row
        try:
            total_expenses += float(row[0])  # Assuming Amount is in the first column
        except ValueError:
            print(f"Skipping non-numeric value: {row[0]}")
    return total_expenses

