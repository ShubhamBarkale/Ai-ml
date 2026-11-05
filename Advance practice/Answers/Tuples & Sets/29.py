elements = tuple(value.strip() for value in input("Enter tuple elements separated by commas: ").split(",") if value.strip())
frequencies = {}

for element in elements:
    frequencies[element] = frequencies.get(element, 0) + 1

print("Tuple:", elements)
print("Element frequencies:", frequencies)
