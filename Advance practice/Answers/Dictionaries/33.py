keys = [value.strip() for value in input("Enter keys separated by commas: ").split(",") if value.strip()]
values = [value.strip() for value in input("Enter values separated by commas: ").split(",") if value.strip()]

if len(keys) != len(values):
    print("The number of keys and values must be the same.")
else:
    result = dict(zip(keys, values))
    print("Dictionary:", result)
