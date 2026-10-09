# Check if a person is eligible for a driving license (age and eyesight condition).


age = int(input("Enter your age: "))
eyesight = input("Is your eyesight normal? (yes/no): ").lower()

if age >= 18 and eyesight == "yes":
    print("Eligible for driving license")
else:
    print("Not eligible for driving license")

