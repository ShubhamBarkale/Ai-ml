# Question 11: Write a program to remove duplicate elements from a list.

# Solution

items = input("Enter items separated by spaces: ").split()
unique_items = []

for item in items:
    if item not in unique_items:
        unique_items.append(item)

print("List without duplicates:", unique_items)
