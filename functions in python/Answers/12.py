def is_palindrome(s):
    if s == s[::-1]:
        return True
    else:
        return False


text = input("Enter a string: ")

result = is_palindrome(text)

print(result)