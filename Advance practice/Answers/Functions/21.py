def calculate_interest(principal, annual_rate, time_in_years):
    simple_interest = principal * annual_rate * time_in_years / 100
    compound_interest = principal * (1 + annual_rate / 100) ** time_in_years - principal
    return simple_interest, compound_interest


try:
    principal = float(input("Enter the principal amount: "))
    annual_rate = float(input("Enter the annual interest rate (%): "))
    time_in_years = float(input("Enter the time in years: "))

    if principal < 0 or annual_rate < 0 or time_in_years < 0:
        print("Please enter non-negative values.")
    else:
        simple, compound = calculate_interest(principal, annual_rate, time_in_years)
        print(f"Simple interest: {simple:.2f}")
        print(f"Compound interest (compounded yearly): {compound:.2f}")
except ValueError:
    print("Please enter valid numbers.")
