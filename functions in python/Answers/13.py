def count_vowels(s):
    count = 0

    for i in s:
        if i.lower() in "aeiou":
            count = count + 1

    return count


text = input("Enter a string: ")

result = count_vowels(text)

print("Number of vowels:", result)