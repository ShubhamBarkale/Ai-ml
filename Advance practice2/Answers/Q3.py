# Question 3: Write a program to check whether a given number is prime.

# Solution

number = int(input("Enter a number: "))

if number < 2:
    is_prime = False
else:
    is_prime = True
    divisor = 2
    while divisor * divisor <= number:
        if number % divisor == 0:
            is_prime = False
            break
        divisor += 1

if is_prime:
    print(number, "is prime")
else:
    print(number, "is not prime")
