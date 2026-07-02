# ===============================
# Python ATM System
# ===============================

# Default PIN and Balance
pin = 1234
balance = 10000

print("====================================")
print("       WELCOME TO PYTHON ATM")
print("====================================")

# PIN Verification
entered_pin = int(input("Enter your 4-digit PIN: "))

if entered_pin == pin:

    while True:

        print("\n========== ATM MENU ==========")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Change PIN")
        print("5. Exit")

        choice = int(input("Enter your choice: "))

        # Check Balance
        if choice == 1:
            print("Your Current Balance is: ₹", balance)

        # Deposit Money
        elif choice == 2:
            amount = int(input("Enter amount to deposit: ₹"))

            if amount > 0:
                balance = balance + amount
                print("Deposit Successful!")
                print("Updated Balance: ₹", balance)
            else:
                print("Invalid Amount!")

        # Withdraw Money
        elif choice == 3:
            amount = int(input("Enter amount to withdraw: ₹"))

            if amount <= balance:
                balance = balance - amount
                print("Please Collect Your Cash.")
                print("Remaining Balance: ₹", balance)
            else:
                print("Insufficient Balance!")

        # Change PIN
        elif choice == 4:
            old_pin = int(input("Enter Old PIN: "))

            if old_pin == pin:
                new_pin = int(input("Enter New PIN: "))
                pin = new_pin
                print("PIN Changed Successfully!")
            else:
                print("Wrong Old PIN!")

        # Exit
        elif choice == 5:
            print("Thank You for Using Python ATM.")
            break

        else:
            print("Invalid Choice!")

else:
    print("Wrong PIN! Access Denied.")