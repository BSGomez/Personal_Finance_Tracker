transactions = []

def add_income():
    amount = input("Enter income amount: ")
    transactions.append(amount)
    print("income added.")

def add_expense():
    print("Add expense selected.")

def view_transactions():
    print(transactions)

def exit_program():
    print("Exiting...")

print("=================================")
print("   PERSONAL FINANCE TRACKER")
print("=================================")

while True:
    print()
    print("1. Add Income")
    print("2. Add Expense")
    print("3. View Transactions")
    print("4. Exit")

    option = input("Select an option: ")

    if option == "1":
        add_income()
    elif option == "2":
        add_expense()
    elif option == "3":
        view_transactions()
    elif option == "4":
        exit_program()
        break
    else:
        print("Invalid option. Please try again.")

