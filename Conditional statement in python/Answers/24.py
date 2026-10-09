# Find the number of days in a month.


month = int(input("Enter month number (1-12): "))

if month == 2:
    print("28 or 29 days")
elif month in [4, 6, 9, 11]:
    print("30 days")
elif 1 <= month <= 12:
    print("31 days")
else:
    print("Invalid month")
