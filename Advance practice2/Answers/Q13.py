# Question 13: Write a program to find the second-largest number in a list.

# Solution

numbers = [float(value) for value in input("Enter numbers separated by spaces: ").split()]
largest = None
second_largest = None

for number in numbers:
    if largest is None or number > largest:
        if largest != number:
            second_largest = largest
        largest = number
    elif number < largest and (second_largest is None or number > second_largest):
        second_largest = number

if second_largest is None:
    print("There is no second-largest distinct number.")
else:
    print("Second-largest number:", second_largest)
