n = int(input("Enter the value of n: "))

print("Prime numbers between 1 and", n, "are:")

for num in range(2, n + 1):
    is_prime = True

    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(num, end=" ")