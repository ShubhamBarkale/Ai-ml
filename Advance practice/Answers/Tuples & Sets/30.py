first_set = {value.strip() for value in input("Enter the first set, separated by commas: ").split(",") if value.strip()}
second_set = {value.strip() for value in input("Enter the second set, separated by commas: ").split(",") if value.strip()}

print("Union:", first_set | second_set)
print("Intersection:", first_set & second_set)
print("Difference (first set - second set):", first_set - second_set)
