first_list = [value.strip() for value in input("Enter the first list, separated by commas: ").split(",") if value.strip()]
second_list = [value.strip() for value in input("Enter the second list, separated by commas: ").split(",") if value.strip()]

merged_list = []
for value in first_list + second_list:
    if value not in merged_list:
        merged_list.append(value)

print("Merged list without duplicates:", merged_list)
