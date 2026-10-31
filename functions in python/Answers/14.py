def second_largest(numbers):
    largest = float('-inf')
    second = float('-inf')

    for i in numbers:
        if i > largest:
            second = largest
            largest = i
        elif i > second and i != largest:
            second = i

    return second


numbers = [10, 25, 5, 40, 15]

result = second_largest(numbers)

print("Second largest number is:", result)