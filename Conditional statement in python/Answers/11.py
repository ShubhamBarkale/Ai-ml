# Check if a character is uppercase or lowercase.

ch = input("Enter a character: ")

if len(ch) == 1 and ch.isupper():
    print("Uppercase")
elif len(ch) == 1 and ch.islower():
    print("Lowercase")
else:
    print("Not an alphabet")
