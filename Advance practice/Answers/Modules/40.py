from datetime import datetime

date_format = "%Y-%m-%d"

try:
    first_date = datetime.strptime(input("Enter the first date (YYYY-MM-DD): "), date_format).date()
    second_date = datetime.strptime(input("Enter the second date (YYYY-MM-DD): "), date_format).date()
    print("Number of days between the dates:", abs((second_date - first_date).days))
except ValueError:
    print("Please enter valid dates in YYYY-MM-DD format.")
