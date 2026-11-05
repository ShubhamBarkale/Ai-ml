# Question 9: Write a program to find the sum of all elements in a list.

# Solution

numbers = [float(value) for value in input("Enter numbers separated by spaces: ").split()]
total = 0

for number in numbers:
    total += number

print("Sum:", total)
