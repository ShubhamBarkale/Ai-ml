balance = 5000

while True:
    print("\n===== ATM MENU =====")
    print("1. Withdraw")
    print("2. Deposit")
    print("3. Balance")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        amount = float(input("Enter withdrawal amount: "))

        if amount <= 0:
            print("Enter a valid amount")
        elif amount <= balance:
            balance -= amount
            print("Withdrawal successful!")
        else:
            print("Insufficient balance")

    elif choice == 2:
        amount = float(input("Enter deposit amount: "))

        if amount > 0:
            balance += amount
            print("Deposit successful!")
        else:
            print("Enter a valid amount")

    elif choice == 3:
        print("Current Balance: Rs.", balance)

    elif choice == 4:
        print("Thank you for using ATM!")
        break

    else:
        print("Invalid choice! Please try again.")