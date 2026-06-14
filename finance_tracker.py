import json
from datetime import date

INCOME = "Income"
EXPENSE = "Expense"
TABLE_SEPARATOR = "-" * 70

def load_transactions():
    try:
        with open("transactions.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Warning: transactions.json is corrupted.")
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
    print("\nTransactions")
    print(TABLE_SEPARATOR)

    print(
        f"{'#':<4}"
        f"{'Date':<12}"
        f"{'Type':<10}"
        f"{'Description':<22}"
        f"{'Amount':>12}"
    )

    print(TABLE_SEPARATOR)
    
    if not transactions:
        print("No transactions recorded.")
        print(TABLE_SEPARATOR)
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
        print(TABLE_SEPARATOR)
            
def view_balance():
    balance = 0
    for transaction in transactions:
        if transaction["type"] == INCOME:
            balance += transaction["amount"]
        elif transaction["type"] == EXPENSE:
            balance -= transaction["amount"]
    print()
    print(TABLE_SEPARATOR)
    print(f"Current Balance: ${balance:.2f}")
    print(TABLE_SEPARATOR)

def view_monthly_summary():
    summary = {}
    
    print()
    print("\nMonthly Summary")
    print(TABLE_SEPARATOR)

    print(
        f"{'Month':<12}"
        f"{'Income':>12}"
        f"{'Expense':>12}"
        f"{'Net':>12}"
    )
    
    print(TABLE_SEPARATOR)
    
    if not transactions:
        print("No transactions recorded.")
        print(TABLE_SEPARATOR)
        print()
    else:
        for transaction in transactions:
            month = transaction["date"][:7]
            if month not in summary:
                summary[month] = {
                    INCOME: 0,
                    EXPENSE: 0 
                }
            
            if transaction["type"] == INCOME:
                summary[month][INCOME] += transaction["amount"]
            elif transaction["type"] == EXPENSE:
                summary[month][EXPENSE] += transaction["amount"]
            
        for summary_month in sorted(summary):
            data = summary[summary_month]
            
            income = f"${data[INCOME]:.2f}"
            expense = f"${data[EXPENSE]:.2f}"
            net = f"${data[INCOME] - data[EXPENSE]:.2f}"

            print(
                f"{summary_month:<12}"
                f"{income:>12}"
                f"{expense:>12}"
                f"{net:>12}"
            )
        print(TABLE_SEPARATOR)
            
def save_transactions():
    with open("transactions.json", "w") as file:
        json.dump(transactions, file, indent=4)

def exit_program():
    print()
    print("Exiting...")
    print()



while True:
    print()
    print("=================================")
    print("   PERSONAL FINANCE TRACKER")
    print("=================================")
    print()
    print("1. Add Income")
    print("2. Add Expense")
    print("3. View Transactions")
    print("4. View Balance")
    print("5. View Monthly Summary")
    print("6. Exit")
    
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
        view_monthly_summary()
    elif option == "6":
        exit_program()
        break
    else:
        print("Invalid option. Please try again.")

