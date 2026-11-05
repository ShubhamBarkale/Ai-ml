# Question 19: Write a program that takes a sentence and finds the longest word.

# Solution

words = input("Enter a sentence: ").split()

if not words:
    print("The sentence contains no words.")
else:
    longest_word = words[0]
    for word in words[1:]:
        if len(word) > len(longest_word):
            longest_word = word
    print("Longest word:", longest_word)
