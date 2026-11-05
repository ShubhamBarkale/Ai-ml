# Question 10: Write a program to find the largest and smallest element in a list without using max() or min().

# Solution

numbers = [float(value) for value in input("Enter numbers separated by spaces: ").split()]

if not numbers:
    print("The list is empty.")
else:
    largest = numbers[0]
    smallest = numbers[0]

    for number in numbers[1:]:
        if number > largest:
            largest = number
        if number < smallest:
            smallest = number

    print("Largest:", largest)
    print("Smallest:", smallest)
