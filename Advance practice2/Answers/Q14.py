# Question 14: Write a program to sort a list without using sort() or sorted().

# Solution

numbers = [float(value) for value in input("Enter numbers separated by spaces: ").split()]

for i in range(len(numbers)):
    for j in range(0, len(numbers) - i - 1):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

print("Sorted list:", numbers)
