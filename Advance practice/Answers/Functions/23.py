def find_second_largest(numbers):
    distinct_numbers = sorted(set(numbers))
    if len(distinct_numbers) < 2:
        return None
    return distinct_numbers[-2]


try:
    numbers = [int(value.strip()) for value in input("Enter integers separated by commas: ").split(",") if value.strip()]
    result = find_second_largest(numbers)
    if result is None:
        print("Enter at least two distinct numbers.")
    else:
        print("Second-largest number:", result)
except ValueError:
    print("Please enter valid integers.")
