# Check whether a number is a three-digit number

num = int(input("Enter a number: "))

if 100 <= abs(num) <= 999:
    print("Three-digit number")
else:
    print("Not a three-digit number")

