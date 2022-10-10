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
SHEET = GSPREAD_CLIENT.open('python_project')


def get_sales_data():
    """
    Get sales data from user 
    """
    print("Enter sales data from.")
    print("Data should be seven numbers, seperated by commas.")
    print("Example: 20,30,40,50,60,70,80\n")

    sale_input = input("Enter sales here: ")
    print(f"The data provided is {sale_input}")



get_sales_data()

