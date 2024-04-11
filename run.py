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

def get_income_data():

    """
    Get income data from the user
    """

    while True:
        print("Please enter income data.")
        print("Data should be three values: amount, description, date.")
        print("Example: 2000, Salary, 2024-04-01")

       data_str = input("Enter your data here: ")

        income_data = data_str.split(",")

        if validate_data(income_data):
            print("Data is valid!")
            break

    return income_data 

def validate_data(values):
    """
    Validate the income or expense data.
    Checks if there are exactly 3 values and if the first value (amount) can be converted to a float.
    """

    if len(values) != 3:
        print("Invalid data: Exactly 3 values required.")
        return False
    
    try:
        float(values[0])  # Check if amount is a valid number
    except ValueError:
        print("Invalid data: Amount must be a number.")
        return False

    return True

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