# Check if a year is a century leap year.


year = int(input("Enter a year: "))

if year % 100 == 0 and year % 400 == 0:
    print("Century Leap Year")
else:
    print("Not a Century Leap Year")

