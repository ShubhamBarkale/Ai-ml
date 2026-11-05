# Question 17: Write a program to check whether two strings are anagrams of each other.

# Solution

first = input("Enter the first string: ")
second = input("Enter the second string: ")

first_clean = first.lower().replace(" ", "")
second_clean = second.lower().replace(" ", "")

if sorted(first_clean) == sorted(second_clean):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")
