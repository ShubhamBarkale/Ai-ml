try:
    numbers = [int(value.strip()) for value in input("Enter integers separated by commas: ").split(",") if value.strip()]
    distinct_numbers = sorted(set(numbers))

    if len(distinct_numbers) < 2:
        print("Enter at least two distinct numbers.")
    else:
        print("Second-smallest element:", distinct_numbers[1])
        print("Second-largest element:", distinct_numbers[-2])
except ValueError:
    print("Please enter valid integers.")
