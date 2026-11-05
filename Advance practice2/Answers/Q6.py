# Question 6: Write a program to reverse a string without using [::-1].

# Solution

text = input("Enter a string: ")
reversed_text = ""

for character in text:
    reversed_text = character + reversed_text

print("Reversed string:", reversed_text)
