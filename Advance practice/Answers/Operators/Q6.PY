num = int(input("Enter a number: "))

if num % 4 == 0 and num % 6 == 0:
    print(num, "is divisible by both 4 and 6")
else:
    print(num, "is not divisible by both 4 and 6")