# Question 18: Write a program to find all duplicate values in a list.

# Solution

items = input("Enter items separated by spaces: ").split()
seen = []
duplicates = []

for item in items:
    if item in seen and item not in duplicates:
        duplicates.append(item)
    else:
        seen.append(item)

print("Duplicate values:", duplicates)
