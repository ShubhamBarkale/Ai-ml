# Check whether a password meets minimum conditions (length, digits, etc.).


password = input("Enter your password: ")

if (len(password) >= 8 and
    any(ch.isdigit() for ch in password) and
    any(ch.isupper() for ch in password) and
    any(ch.islower() for ch in password) and
    any(not ch.isalnum() for ch in password)):
    print("Valid password")
else:
    print("Invalid password")

