def find_max(numbers):
    largest = numbers[0]

    for i in numbers:
        if i > largest:
            largest = i

    return largest


numbers = [10, 25, 5, 40, 15]

result = find_max(numbers)

print("Largest number is:", result)