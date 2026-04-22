from services.atm_service import *

while True:
    print("\n====== ATM MENU ======")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Statement")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        check_balance()
    elif choice == "2":
        deposit()
    elif choice == "3":
        withdraw()
    elif choice == "4":
        show_statement()
    elif choice == "5":
        print("Thank you for using ATM!")
        break
    else:
        print("Invalid choice! Try again.")