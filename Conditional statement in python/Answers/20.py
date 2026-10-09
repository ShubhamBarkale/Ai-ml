# Find whether a number is within a given range.


num = int(input("Enter a number: "))
start = int(input("Enter range start: "))
end = int(input("Enter range end: "))

if start <= num <= end:
    print("Number is within the range")
else:
    print("Number is outside the range")

