dictionary = {}
entries = input("Enter key:value pairs separated by commas (for example, apple:3, pear:1): ")

try:
    for entry in entries.split(","):
        key, separator, value = entry.partition(":")
        if not separator or not key.strip():
            raise ValueError
        dictionary[key.strip()] = float(value.strip())

    sorted_dictionary = dict(sorted(dictionary.items(), key=lambda item: item[1]))
    print("Dictionary sorted by value:", sorted_dictionary)
except ValueError:
    print("Please enter each item as a key followed by a numeric value (key:value).")
