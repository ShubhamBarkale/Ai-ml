file_name = input("Enter the text file path: ")

try:
    with open(file_name, "r", encoding="utf-8") as file:
        contents = file.read()

    print("Number of lines:", len(contents.splitlines()))
    print("Number of words:", len(contents.split()))
    print("Number of characters:", len(contents))
except FileNotFoundError:
    print("File not found:", file_name)
except OSError as error:
    print("Could not read the file:", error)
