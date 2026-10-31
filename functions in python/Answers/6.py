def count_even(numbers):
    count = 0

    for i in numbers:
        if i % 2 == 0:
            count = count + 1

    return count


numbers = [1, 2, 3, 4, 6]

result = count_even(numbers)

print("Count of even numbers:", result)