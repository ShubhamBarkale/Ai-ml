# Question 16: Write a program to find the frequency of each character in a string.

# Solution

text = input("Enter a string: ")
frequencies = {}

for character in text:
    if character in frequencies:
        frequencies[character] += 1
    else:
        frequencies[character] = 1

print("Character frequencies:", frequencies)
