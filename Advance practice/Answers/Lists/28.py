first_list = [value.strip() for value in input("Enter the first list, separated by commas: ").split(",") if value.strip()]
second_list = [value.strip() for value in input("Enter the second list, separated by commas: ").split(",") if value.strip()]

common_elements = []
for value in first_list:
    if value in second_list and value not in common_elements:
        common_elements.append(value)

print("Common elements:", common_elements)
