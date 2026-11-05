# Question 7: Write a program to check whether a string is a palindrome.

# Solution

text = input("Enter a string: ")
normalized_text = text.lower().replace(" ", "")
reversed_text = ""

for character in normalized_text:
    reversed_text = character + reversed_text

if normalized_text == reversed_text:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
