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

    # You can add additional validation here if needed

    return True