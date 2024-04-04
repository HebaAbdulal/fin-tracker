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