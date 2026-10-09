# Determine ticket price based on age category.

age = int(input("Enter your age: "))

if age < 0:
    print("Invalid age")
elif age < 5:
    print("Ticket price: Free")
elif age <= 12:
    print("Ticket price: ₹50")
elif age <= 59:
    print("Ticket price: ₹100")
else:
    print("Ticket price: ₹60")
