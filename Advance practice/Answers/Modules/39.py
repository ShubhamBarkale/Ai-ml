import random
import string

try:
    length = int(input("Enter the password length: "))
    if length <= 0:
        print("Password length must be a positive integer.")
    else:
        characters = string.ascii_letters + string.digits + string.punctuation
        password = "".join(random.choice(characters) for _ in range(length))
        print("Generated password:", password)
except ValueError:
    print("Please enter a valid integer.")
