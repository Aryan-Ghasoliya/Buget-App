# Buget-App

# The Budget Tracker Application 
- It is a simple Python program that allows users to track their income and expenses. It provides an intuitive command-line interface for adding, viewing, and summarizing transactions. The app uses the pandas library to store and analyze transaction data.

## Features
#### 1.  Add Income

   - Add a new income transaction with details such as category, amount, and description.
   - Updates the current balance automatically.
#### 2.Add Expense

- Record a new expense transaction with details such as category, amount, and description.
- Deducts the expense amount from the current balance.
#### 3.View Transactions

- Displays a table of all recorded transactions, including type, category, amount, and description.
#### 4.View Summary

- Provides a summarized view of:
  - Total Income
  - Total Expenses
  - Current Balance
#### 5.Exit Application

- Allows the user to exit the application.
## Requirements
- Python 3.6 or higher
- pandas library
### Installation
- Install Python:
  - Download and install Python from python.org.

- Install pandas:
  - Run the following command to install the pandas library:

  ```
  pip install pandas
  ```
## How to Run the Application
- Save the code to a file named budget_tracker.py.
- Open a terminal or command prompt in the directory where the file is saved.
- Run the application using the following command:
  ```
  python budget_tracker.py
  ```
## Usage
1. Start the Program
  - Launch the program to see the menu options.

2. Choose an Option
- Enter the corresponding number for the desired action (e.g., "1" to add income).

3. Follow Prompts
- Enter details like category, amount, and description when prompted.

4. View Data
- Use options to view transactions or a summary of your budget.

## Example Walkthrough
#### Add Income:
```
--- Budget Tracker Menu ---
1. Add Income
2. Add Expense
3. View Transactions
4. View Summary
5. Exit
Choose an option: 1
Enter income category (e.g., Salary, Investment): Salary
Enter income amount: 2000
Enter a description: Monthly salary
Transaction added! Current balance: $2000.00
```
#### Add Expense:
```
--- Budget Tracker Menu ---
Choose an option: 2
Enter expense category (e.g., Food, Rent, Utilities): Rent
Enter expense amount: 800
Enter a description: Monthly rent
Transaction added! Current balance: $1200.00
```
#### View Transactions:
```
--- Budget Tracker Menu ---
Choose an option: 3

--- Transactions ---
      Type Category Amount       Description
0   Income   Salary  2000.0   Monthly salary
1  Expense     Rent   800.0     Monthly rent
```

#### View Summary:
```
--- Budget Tracker Menu ---
Choose an option: 4

--- Budget Summary ---
Total Income: $2000.00
Total Expenses: $800.00
Current Balance: $1200.00
```

Enjoy using the Budget Tracker to manage your finances effectively! 🎉
