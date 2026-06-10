INCOME = "Income"
EXPENSE = "Expense"
transactions = []

def add_transaction(transaction_type):
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
    transaction = {"type": transaction_type, "amount": amount, "description": description}
    transactions.append(transaction)
    print(f"{transaction_type} added.")

def add_income():
    add_transaction(INCOME)

def add_expense():
    add_transaction(EXPENSE)

def view_transactions():
    print()
    print("Transactions")
    
    if not transactions:
        print("No transactions recorded.")
    else:
        for transaction in transactions:
            print(f"{transaction['type']} - {transaction['description']} - ${transaction['amount']:.2f}")
            
def view_balance():
    balance = 0
    for transaction in transactions:
        if transaction["type"] == INCOME:
            balance += transaction["amount"]
        elif transaction["type"] == EXPENSE:
            balance -= transaction["amount"]
    print()
    print(f"Current Balance: ${balance:.2f}")

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

