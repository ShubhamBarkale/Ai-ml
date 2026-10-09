# Find the largest among four numbers.


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
d = int(input("Enter fourth number: "))

if a >= b and a >= c and a >= d:
    print("Largest number:", a)
elif b >= a and b >= c and b >= d:
    print("Largest number:", b)
elif c >= a and c >= b and c >= d:
    print("Largest number:", c)
else:
    print("Largest number:", d)

