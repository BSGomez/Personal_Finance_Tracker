import json
from datetime import date

INCOME = "Income"
EXPENSE = "Expense"

def load_transactions():
    try:
        with open("transactions.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

transactions = load_transactions()

def add_transaction(transaction_type):
    current_date = date.today().isoformat()
    while True:
        print()
        try:
            amount = float(input(f"Enter {transaction_type} amount: "))
            if amount > 0:
                break
            else:
                print("Invalid amount. Please enter a number greater than 0.")
                
        except ValueError:
            print("Invalid amount. Please enter a number.")
            
    description = input("Enter description: ")
    transaction = {"type": transaction_type, "amount": amount, "description": description, "date":current_date}
    transactions.append(transaction)
    save_transactions()
    print(f"{transaction_type} added.")

def add_income():
    add_transaction(INCOME)

def add_expense():
    add_transaction(EXPENSE)

def view_transactions():
    print()
    print("\nTransactions")
    print("-" * 70)

    print(
        f"{'#':<4}"
        f"{'Date':<12}"
        f"{'Type':<10}"
        f"{'Description':<22}"
        f"{'Amount':>12}"
    )

    print("-" * 70)
    
    if not transactions:
        print("No transactions recorded.")
        print("-"*70)
        print()
    else:
        for index, transaction in enumerate(transactions, start=1):
            if len(transaction['description']) > 20:
                description = transaction['description'][:17]+"..."
            else:
                description = transaction['description']
                
            print(
                f"{index:<4}"
                f"{transaction['date']:<12}"
                f"{transaction['type']:<10}"
                f"{description:<22}"
                f"${transaction['amount']:>11.2f}"
            )
        print("-"*70)
            
def view_balance():
    balance = 0
    for transaction in transactions:
        if transaction["type"] == INCOME:
            balance += transaction["amount"]
        elif transaction["type"] == EXPENSE:
            balance -= transaction["amount"]
    print()
    print(f"Current Balance: ${balance:.2f}")

def save_transactions():
    with open("transactions.json", "w") as file:
        json.dump(transactions, file, indent=4)

def exit_program():
    print()
    print("Exiting...")
    print()

print("=================================")
print("   PERSONAL FINANCE TRACKER")
print("=================================")

while True:
    print()
    print("1. Add Income")
    print("2. Add Expense")
    print("3. View Transactions")
    print("4. View Balance")
    print("5. Exit")
    
    print()
    option = input("Select an option: ")

    if option == "1":
        add_income()
    elif option == "2":
        add_expense()
    elif option == "3":
        view_transactions()
    elif option == "4":
        view_balance()
    elif option == "5":
        exit_program()
        break
    else:
        print("Invalid option. Please try again.")

