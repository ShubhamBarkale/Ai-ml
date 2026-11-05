try:
    numbers = [int(value.strip()) for value in input("Enter integers separated by commas: ").split(",") if value.strip()]
    positions = int(input("Rotate left by how many positions? "))

    if not numbers:
        print("The list is empty; there is nothing to rotate.")
    else:
        positions %= len(numbers)
        rotated_list = numbers[positions:] + numbers[:positions]
        print("Rotated list:", rotated_list)
except ValueError:
    print("Please enter valid integers.")
