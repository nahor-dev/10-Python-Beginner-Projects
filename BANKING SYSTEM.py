print("=" * 35)
print("       BANKING SYSTEM")
print("=" * 35)

account = {}

while True:

    try:
        choice = int(input("""
1. Create Account
2. Deposit Money
3. Withdraw Money
4. Check Balance
5. Transaction History
6. Exit

Choose an option: """))
    except ValueError:
        print("Please enter a number between 1 and 6.")
        continue

    # ============== CREATE ACCOUNT ==============

    if choice == 1:

        if account:
            print("An account already exists.")
        else:
            name = input("Enter your name: ").strip()

            account = {
                "name": name,
                "balance": 0.0,
                "history": []
            }

            print("Account created successfully!")

    # ============== DEPOSIT ==============

    elif choice == 2:

        if not account:
            print("Please create an account first.")
            continue

        try:
            amount = float(input("Enter amount to deposit: "))

            if amount <= 0:
                print("Amount must be greater than 0.")
            else:
                account["balance"] += amount
                account["history"].append(f"Deposit: ${amount:.2f}")

                print("Deposit successful!")

        except ValueError:
            print("Invalid amount.")

    # ============== WITHDRAW ==============

    elif choice == 3:

        if not account:
            print("Please create an account first.")
            continue

        try:
            amount = float(input("Enter amount to withdraw: "))

            if amount <= 0:
                print("Amount must be greater than 0.")

            elif amount > account["balance"]:
                print("Insufficient balance.")

            else:
                account["balance"] -= amount
                account["history"].append(f"Withdraw: ${amount:.2f}")

                print("Withdrawal successful!")

        except ValueError:
            print("Invalid amount.")

    # ============== BALANCE ==============

    elif choice == 4:

        if not account:
            print("Please create an account first.")
        else:
            print("\nAccount Holder :", account["name"])
            print(f"Current Balance : ${account['balance']:.2f}")

    # ============== HISTORY ==============

    elif choice == 5:

        if not account:
            print("Please create an account first.")

        elif not account["history"]:
            print("No transactions found.")

        else:
            print("\nTransaction History")
            print("-" * 25)

            for i, transaction in enumerate(account["history"], start=1):
                print(f"{i}. {transaction}")

    # ============== EXIT ==============

    elif choice == 6:

        print("Thank you for using our bank!")
        break

    else:
        print("Please choose a number between 1 and 6.")