# Determine the season based on the month number.


month = int(input("Enter month number (1-12): "))

if month < 1 or month > 12:
    print("Invalid month")
elif month in [3, 4, 5]:
    print("Summer")
elif month in [6, 7, 8, 9]:
    print("Monsoon")
elif month in [10, 11]:
    print("Autumn")
else:
    print("Winter")

