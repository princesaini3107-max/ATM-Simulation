from models.account import Account

account = Account()

def check_balance():
    print(f"\n Current Balance: ₹{account.balance}")

def deposit():
    amount = int(input("Enter amount to deposit: "))
    
    if amount <= 0:
        print("Invalid amount!")
        return

    account.balance += amount
    account.transactions.append(f"Deposited ₹{amount}")
    print("Deposit successful!")

def withdraw():
    amount = int(input("Enter amount to withdraw: "))
    
    if amount > account.balance:
        print(" Insufficient balance!")
    else:
        account.balance -= amount
        account.transactions.append(f"Withdrew ₹{amount}")
        print("Withdrawal successful!")

def show_statement():
    print("\n Transaction History:")
    
    if not account.transactions:
        print("No transactions yet.")
    else:
        for t in account.transactions:
            print("-", t)