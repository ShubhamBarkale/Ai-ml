# Question 4: Write a program to print the Fibonacci series up to n terms.

# Solution

terms = int(input("How many terms? "))
first = 0
second = 1

for _ in range(terms):
    print(first, end=" ")
    first, second = second, first + second
print()
