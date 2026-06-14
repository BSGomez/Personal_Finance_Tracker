# Personal Finance Tracker

## Description

Personal Finance Tracker is a Python console application that helps users manage their personal finances by recording income and expenses, calculating balances, and generating monthly financial summaries.

The application stores transaction data in a JSON file, allowing information to persist between executions.

---

## Features

* Add income transactions
* Add expense transactions
* View all recorded transactions
* View current balance
* View monthly financial summaries
* Automatic transaction date generation
* Persistent storage using JSON
* Input validation for transaction amounts
* Error handling for missing or corrupted data files

---

## Technologies Used

* Python 3
* JSON
* Standard Python Libraries:

  * json
  * datetime

---

## Project Structure

```text
personal-finance-tracker/
│
├── main.py
├── finance_tracker.py
├── transactions.json
├── .gitignore
└── README.md
```

---

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/BSGomez/Personal_Finance_Tracker.git
```

### 2. Navigate to the project folder

```bash
cd personal-finance-tracker
```

### 3. Run the application

```bash
python main.py
```

---

## Menu Options

```text
1. Add Income
2. Add Expense
3. View Transactions
4. View Balance
5. View Monthly Summary
6. Exit
```

---

## Data Persistence

All transactions are stored in:

```text
transactions.json
```

The application automatically:

* Loads existing transactions when it starts
* Saves new transactions after they are added

Example transaction:

```json
{
    "type": "Income",
    "amount": 1000.0,
    "description": "Salary",
    "date": "2026-08-05"
}
```

---

## Reports

### Transactions Report

Displays all recorded transactions in a tabular format including:

* Date
* Type
* Description
* Amount

### Current Balance

Calculates:

```text
Total Income - Total Expenses
```

### Monthly Summary

Groups transactions by month and displays:

* Total Income
* Total Expenses
* Net Balance

Example:

```text
Month             Income     Expense         Net
------------------------------------------------------------
2026-06          $500.00     $250.00     $250.00
2026-07         $1000.00     $300.00     $700.00
```

---

## Error Handling

The application handles:

### Invalid Amounts

Examples:

```text
abc
-100
0
```

### Missing Transaction File

If `transactions.json` does not exist, the application automatically creates an empty transaction list.

### Corrupted JSON File

If the JSON file contains invalid data, the application displays a warning and starts with an empty transaction list.

---

## Author

Bryan Steven Gómez Arévalo

Personal Finance Tracker Project
