# Calculate income tax based on income slabs.


income = float(input("Enter your annual income: "))

if income < 0:
    print("Invalid income")
elif income <= 300000:
    tax = 0
elif income <= 600000:
    tax = (income - 300000) * 0.05
elif income <= 900000:
    tax = 15000 + (income - 600000) * 0.10
elif income <= 1200000:
    tax = 45000 + (income - 900000) * 0.15
else:
    tax = 90000 + (income - 1200000) * 0.20

if income >= 0:
    print("Income tax: ₹", tax)
