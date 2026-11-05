# Question 15: Write a function that accepts a list of numbers and returns a list containing only the even numbers.

# Solution

def even_numbers(numbers):
    result = []
    for number in numbers:
        if number % 2 == 0:
            result.append(number)
    return result


values = [int(value) for value in input("Enter numbers separated by spaces: ").split()]
print("Even numbers:", even_numbers(values))
