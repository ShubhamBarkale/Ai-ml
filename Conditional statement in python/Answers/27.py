# Calculate discount based on purchase amount.


amount = float(input("Enter purchase amount: "))

if amount < 0:
    print("Invalid amount")
elif amount >= 5000:
    discount = amount * 0.20
elif amount >= 3000:
    discount = amount * 0.10
elif amount >= 1000:
    discount = amount * 0.05
else:
    discount = 0

if amount >= 0:
    print("Discount: ₹", discount)
    print("Final amount: ₹", amount - discount)

