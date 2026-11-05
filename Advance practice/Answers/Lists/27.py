try:
    numbers = [int(value.strip()) for value in input("Enter integers separated by commas: ").split(",") if value.strip()]
    even_numbers = [number for number in numbers if number % 2 == 0]
    odd_numbers = [number for number in numbers if number % 2 != 0]

    print("Even numbers:", even_numbers)
    print("Odd numbers:", odd_numbers)
except ValueError:
    print("Please enter valid integers.")
