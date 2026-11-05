def is_palindrome(text):
    cleaned_text = "".join(character.lower() for character in text if character.isalnum())
    return cleaned_text == cleaned_text[::-1]


user_text = input("Enter a string: ")
if is_palindrome(user_text):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
