def count_vowels_and_consonants(text):
    vowels = "aeiou"
    vowel_count = 0
    consonant_count = 0

    for character in text.lower():
        if character.isalpha():
            if character in vowels:
                vowel_count += 1
            else:
                consonant_count += 1

    return vowel_count, consonant_count


user_text = input("Enter a string: ")
vowels, consonants = count_vowels_and_consonants(user_text)
print("Vowels:", vowels)
print("Consonants:", consonants)
