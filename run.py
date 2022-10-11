import gspread
from google.oauth2.service_account import Credentials
from pprint import pprint
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
    Run a while loop to collect a valid string of data from the user
     via the terminal, which must be a string of seven numbers seperated by commas.
     The loop will repeatedly request data, until it is valid.
    """
    while True:

        print("Enter sales data from.")
        print("Data should be seven numbers, seperated by commas.")
        print("Example: 20,30,40,50,60,70,80\n")

        sales_input = input("Enter sales here: ")

        sales_data = sales_input.split(",")
        
        if validate_data(sales_data):
            print("Valid")
            break
    
    return sales_data


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
        return False

    return True


def update_sales_worksheet(data):
    """
    Updates sales worksheet, and add new row with the list data provided
    """
    print("Updating sales worksheet...\n")
    sales_worksheet = SHEET.worksheet("sales")
    sales_worksheet.append_row(data)
    print("sales worksheet updated successfully.\n")



def calculate_surplus_data(sales_row):
    """
    Compare sales with stock and calculate the surplus for each item

    Positive numbers = waste
    Minus numbers = extra made when stock ran out
    """
    print("Calculate surplus data...\n")
    stock = SHEET.worksheet("stock").get_all_values()
    stock_row = stock[-1]
    print(f' stock row: {stock_row}')
    print(f' sales row: {sales_row}')

    surplus_data = []
    for stock, sales in zip(stock_row, sales_row):
        surplus = int(stock) - sales
        surplus_data.append(surplus)
    
    return surplus_data

def update_surplus_worksheet(data):
    """
    Updates sales worksheet, and add new row with the list data provided
    """
    print("Updating surplus worksheet...\n")
    surplus_worksheet = SHEET.worksheet("surplus")
    surplus_worksheet.append_row(data)
    print("surplus worksheet updated successfully.\n")



def main():
    """
    Run all program functions
    """
    data = get_sales_data()
    sales_data = [int(num) for num in data]
    update_sales_worksheet(sales_data)
    new_surplus_data = calculate_surplus_data(sales_data)
    update_surplus_worksheet(new_surplus_data)
    


print("Welcome to Data Automation")
main()