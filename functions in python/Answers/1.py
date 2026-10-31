def is_even(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"


num = int(input("Enter a number: "))

result = is_even(num)

print("The number is", result)