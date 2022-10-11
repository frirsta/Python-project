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

    sales_input = input("Enter sales here: ")

    sales_data = sales_input.split(",")
    validate_data(sales_data)


def validate_data(values):
    """
    Inside the try, converts string values to integers.
    Raises ValueError if strings cannot be converted to integers,
    or if there are not exacly seven values.
    """
    print(values)
    try:
        [int(value) for value in values]
        if len(values) != 7:
            raise ValueError(
                f"Exacly 7 numbers are required, you provided {len(values)}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, try again.\n")


get_sales_data()

