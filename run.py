import rich
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
        amount_str = input("Enter the amount of income:\n")
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
        description = input("Enter the description of income:\n")
        if description.isalpha():
            return description
        else:
            print("Description must contain only letters.")


def get_date():
    """
    Get the date of income and validate that it is in the correct format.
    """
    while True:
        date_str = input("Enter the date of income (YYYY-MM-DD):\n")
        try:
            datetime.strptime(date_str, '%Y-%m-%d')
            return date_str
        except ValueError:
            print("Please enter the date in the format 'YYYY-MM-DD'.")


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
    print("Updating income worksheet...\n")
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
            total_incomes += float(row[0])
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


def get_expense_amount():
    """
    Get the amount of expenses and validate that it is a positive number.
    """
    while True:
        amount_str = input("Enter the amount of expenses:\n")
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
        description = input("Enter expense description:\n")
        if description.replace(' ', '').isalpha():
            return description
        else:
            print("Description must contain only letters.")


def get_expense_date():
    """
    Get the date of expenses and validate that it is in the correct format.
    """
    while True:
        date_str = input("Enter the date of expenses (YYYY-MM-DD):\n")
        try:
            datetime.strptime(date_str, '%Y-%m-%d')
            return date_str
        except ValueError:
            print("Please enter the date in the format 'YYYY-MM-DD'.")


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
    expense_worksheet = SHEET.worksheet("expenses")  # Update this line
    expenses = expense_worksheet.get_all_values()
    total_expenses = 0
    for row in expenses[1:]:  # Skip header row
        try:
            total_expenses += float(row[0])
        except ValueError:
            print(f"Skipping non-numeric value: {row[0]}")
    return total_expenses


def display_expense_data():
    """
    Display all expense data from the expense worksheet in a table format.
    """
    print("Displaying expense data...\n")
    expense_worksheet = SHEET.worksheet("expenses")  # Update this line
    expenses = expense_worksheet.get_all_values()

    # Create a table to display the expense data
    table = Table(title="Expense Data")
    table.add_column("Amount", justify="right")
    table.add_column("Description", justify="right")
    table.add_column("Date", justify="right")

    # Skip the header row
    for row in expenses[1:]:
        table.add_row(*row)

    console.print(table)


def analyze_expenses():
    """
    Analyze expenses by displaying total expenses and expense data in a table.
    """

    total_expenses = calculate_total_expenses()

    table = Table(title="Expense Summary")
    table.add_column("Total Expenses", justify="right")
    table.add_row(f"${total_expenses:.2f}")

    console.print(table)
    display_expense_data()


def calculate_remaining_amount():
    """
    Calculate ramaining amount after taking off all expenses.
    """
    total_incomes = calculate_total_income()
    total_expenses = calculate_total_expenses()
    remaining_amount = total_incomes - total_expenses
    print(f"Remaining Amount: ${remaining_amount:.2f}\n")


def print_remaining_amount():
    """
    Print the remaining amount after calculating it.
    """
    print("\nRemaining Amount Calculated.\n")


def set_budget():
    """
    Set budget for different expense categories.
    """
    print("Setting budget...")
    descriptions = ["Groceries", "Utilities", "Entertainment"]
    budget_data = {}
    for description in descriptions:
        while True:
            budget_input = input(f"Enter budget for {description}:\n")
            if budget_input.replace('.', '', 1).isdigit():
                budget = float(budget_input)
                if budget < 0:
                    print("Budget cannot be negative.")
                else:
                    budget_data[description] = budget
                    break
            else:
                print("Invalid input. Budget must be a positive number.")
    return budget_data


def notify_budget_exceed(description, remaining_amount):
    """
    Notify the user when the budget for a category is exceeded.
    """
    message = (
        f"Budget for {description} has been exceeded! "
        f"Remaining amount: ${remaining_amount:.2f}"
    )
    print(message)


def track_expenses_with_budget(budget_data):
    """
    Track expenses while considering budget limits.
    """
    print("Tracking expenses with budget...")
    while True:
        expenses_data = get_expenses_data()
        update_expenses_worksheet(expenses_data)
        calculate_remaining_amount()

        # Check if any budget is exceeded
        for description, budget_amount in budget_data.items():
            if description in expenses_data:
                total_expenses = calc_expenses(description)
                remaining_amount = budget_amount - total_expenses
                if remaining_amount < 0:
                    notify_budget_exceed(description, remaining_amount)

        choice = input("Do you want to add another expense? (yes/no):\n")
        if choice.lower() != 'yes':
            break  # Exit the loop if the user chooses not to add more expenses

    # Calculate remaining amount
    calculate_remaining_amount()

    return total_incomes


def calc_expenses(description):
    """
    Calculate the total expenses for a specific description.
    """
    expense_worksheet = SHEET.worksheet("expenses")
    expenses = expense_worksheet.get_all_values()
    total_expenses = 0
    for row in expenses[1:]:
        if len(row) > 1 and row[1].strip() == description:
            try:
                total_expenses += float(row[0])
            except ValueError as e:
                print(f"Skipping non-numeric value: {row[0]}")
                print(f"Error: {e}")
    return total_expenses


def display_budget(budget_data):
    """
    Display the budget summary.
    """
    table = Table(title="Budget Summary")
    table.add_column("Category", justify="right")
    table.add_column("Budget Amount", justify="right")

    for category, amount in budget_data.items():
        table.add_row(category, f"${amount:.2f}")

    console.print(table)


def update_budget_worksheet(budget_data):
    """
    Update budget worksheet, add new rows with the budget data provided.
    Also update Total Expenses and Budget Status columns.
    """
    print("Updating budget worksheet...\n")
    budget_worksheet = SHEET.worksheet("budget")

    # Iterate over each description in the budget data
    for description, budget_amount in budget_data.items():
        # Find the cell corresponding to the description
        desc_cell = budget_worksheet.find(description)

        # Calculate total expenses for the current description
        total_expenses = calc_expenses(description)

        # Update Total Expenses column for the current description
        exp_cell_off = (desc_cell.row, desc_cell.col + 2)
        budget_worksheet.update_cell(*exp_cell_off, total_expenses)

        # Update Budget for the current description
        budget_cell_offset = (desc_cell.row, desc_cell.col + 1)
        budget_worksheet.update_cell(*budget_cell_offset, budget_amount)

        # Update Budget Status for the current description
        remaining_amount = budget_amount - total_expenses
        budget_status = "Exceeded" if remaining_amount < 0 else "Within Budget"
        budget_status_cell_offset = (desc_cell.row, desc_cell.col + 3)
        budget_worksheet.update_cell(*budget_status_cell_offset, budget_status)

        # Update Notification for the current description
        notification = "Alert" if remaining_amount < 0 else "Encouragement"
        notification_cell_offset = (desc_cell.row, desc_cell.col + 4)
        budget_worksheet.update_cell(*notification_cell_offset, notification)

    print("Budget worksheet updated successfully.\n")


def get_income_index():
    """
    Get the index of the income to update or remove.
    """
    while True:
        index_str = input(
            "Enter the index of the income you want to update/remove:\n")
        try:
            index = int(index_str)
            if index <= 0:
                print("Invalid index: Index must be a positive number.")
            else:
                # Check if the index exists in the income worksheet
                income_worksheet = SHEET.worksheet("income")
                incomes = income_worksheet.get_all_values()
                if index <= len(incomes):
                    return index
                else:
                    print("Index does not exist. Please enter a valid index.")
        except ValueError:
            print("Invalid index: Please enter a valid number.")


def update_income():
    """
    Function to update income.
    """
    display_income_data()
    index = get_income_index()
    updated_income_data = get_income_data()


def remove_income_worksheet(index):
    """
    Remove row from income worksheet based on index.
    """
    print("Removing row from income worksheet...\n")
    income_worksheet = SHEET.worksheet("income")
    income_worksheet.delete_row(index)

    print("Row removed successfully.\n")

    # Retrieve all income data from the worksheet
    income_worksheet = SHEET.worksheet("income")
    incomes = income_worksheet.get_all_values()

    # Check if the index is within the range of the available income data
    if index > 0 and index <= len(incomes):
        # Update the income data at the specified index
        incomes[index - 1] = updated_income_data

        # Update the worksheet with the updated data
        range_name = 'A{}:C{}'.format(index, index)
        income_worksheet.update(
            values=[updated_income_data], range_name=range_name)

        print("Income updated successfully.\n")
    else:
        print("Invalid index. Please enter a valid index.")


def remove_income():
    """
    Function to remove income.
    """
    print("Removing row from income worksheet...\n")
    income_worksheet = SHEET.worksheet("income")

    # Display current income data before removal
    display_income_data()

    index = get_income_index()

    # Retrieve all income data from the worksheet
    incomes = income_worksheet.get_all_values()

    # Check if the index is within the range of the available income data
    if index > 0 and index <= len(incomes):
        # Delete the row at the specified index
        income_worksheet.delete_rows(index)

        print("Income removed successfully.\n")
    else:
        print("Invalid index. Please enter a valid index.")


def get_expense_index():
    """
    Get the index of the expense to update or remove.
    """
    while True:
        index_str = input(
            "Enter the index of the expense you want to update/remove:\n")
        try:
            index = int(index_str)
            if index <= 0:
                print("Invalid index: Index must be a positive number.")
            else:
                return index
        except ValueError:
            print("Invalid index: Please enter a valid number.")


total_incomes = 0  # Initialize total incomes