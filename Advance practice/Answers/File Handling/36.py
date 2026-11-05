from pathlib import Path

source_name = input("Enter the source file path: ")
destination_name = input("Enter the destination file path: ")

try:
    if Path(source_name).resolve() == Path(destination_name).resolve():
        print("Source and destination must be different files.")
    else:
        with open(source_name, "r", encoding="utf-8") as source_file:
            lines = source_file.readlines()

        with open(destination_name, "w", encoding="utf-8") as destination_file:
            for line_number, line in enumerate(lines, start=1):
                if line_number % 2 == 0:
                    destination_file.write(line)

        print("Copied the even-numbered lines to", destination_name)
except FileNotFoundError:
    print("Source file not found:", source_name)
except OSError as error:
    print("Could not copy the file:", error)
