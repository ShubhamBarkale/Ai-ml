file_name = input("Enter the file path to read: ")

try:
    with open(file_name, "r", encoding="utf-8") as file:
        contents = file.read()
    print(contents)
except FileNotFoundError:
    print("File not found:", file_name)
