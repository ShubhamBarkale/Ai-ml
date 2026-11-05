# Question 12: Write a program to count how many times each element appears in a list using a dictionary.

# Solution

items = input("Enter items separated by spaces: ").split()
counts = {}

for item in items:
    if item in counts:
        counts[item] += 1
    else:
        counts[item] = 1

print("Element counts:", counts)
