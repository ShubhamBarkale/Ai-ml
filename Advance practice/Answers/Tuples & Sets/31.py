first_set = {value.strip() for value in input("Enter the set to check, separated by commas: ").split(",") if value.strip()}
second_set = {value.strip() for value in input("Enter the other set, separated by commas: ").split(",") if value.strip()}

if first_set.issubset(second_set):
    print("The first set is a subset of the second set.")
else:
    print("The first set is not a subset of the second set.")
