def find_factors(number):
    return [value for value in range(1, number + 1) if number % value == 0]


try:
    number = int(input("Enter a positive integer: "))
    if number <= 0:
        print("Please enter a positive integer.")
    else:
        print("Factors:", find_factors(number))
except ValueError:
    print("Please enter a valid integer.")
