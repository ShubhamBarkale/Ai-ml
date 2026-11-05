# Question 2: Write a program to find the largest of three numbers.

# Solution

first = float(input("Enter the first number: "))
second = float(input("Enter the second number: "))
third = float(input("Enter the third number: "))

largest = first
if second > largest:
    largest = second
if third > largest:
    largest = third

print("The largest number is:", largest)
