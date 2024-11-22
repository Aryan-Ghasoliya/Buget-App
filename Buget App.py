import pandas as pd

class BudgetApp:
    def __init__(self):
        # Initialize an empty DataFrame to store transactions
        self.data = pd.DataFrame(columns=["Type", "Category", "Amount", "Description"])
        self.balance = 0  # Track the total balance

    def add_transaction(self, trans_type, category, amount, description):
        # Add a new transaction
        new_transaction = {
            "Type": trans_type,
            "Category": category,
            "Amount": amount,
            "Description": description
        }
        self.data = pd.concat([self.data, pd.DataFrame([new_transaction])], ignore_index=True)

        # Update the balance based on the transaction type
        if trans_type == "Income":
            self.balance += amount
        elif trans_type == "Expense":
            self.balance -= amount

        print(f"Transaction added! Current balance: ${self.balance:.2f}")

    def view_transactions(self):
        # Display all transactions
        if self.data.empty:
            print("No transactions available.")
        else:
            print("\n--- Transactions ---")
            print(self.data)

    def view_summary(self):
        # Summarize the data
        print("\n--- Budget Summary ---")
        income = self.data[self.data["Type"] == "Income"]["Amount"].sum()
        expense = self.data[self.data["Type"] == "Expense"]["Amount"].sum()
        print(f"Total Income: ${income:.2f}")
        print(f"Total Expenses: ${expense:.2f}")
        print(f"Current Balance: ${self.balance:.2f}")

    def run(self):
        while True:
            print("\n--- Budget Tracker Menu ---")
            print("1. Add Income")
            print("2. Add Expense")
            print("3. View Transactions")
            print("4. View Summary")
            print("5. Exit")
            choice = input("Choose an option: ")

            if choice == "1":
                category = input("Enter income category (e.g., Salary, Investment): ")
                amount = float(input("Enter income amount: "))
                description = input("Enter a description: ")
                self.add_transaction("Income", category, amount, description)
            elif choice == "2":
                category = input("Enter expense category (e.g., Food, Rent, Utilities): ")
                amount = float(input("Enter expense amount: "))
                description = input("Enter a description: ")
                self.add_transaction("Expense", category, amount, description)
            elif choice == "3":
                self.view_transactions()
            elif choice == "4":
                self.view_summary()
            elif choice == "5":
                print("Exiting Budget Tracker. Goodbye!")
                break
            else:
                print("Invalid option. Please try again.")

# Run the application
if __name__ == "__main__":
    app = BudgetApp()
    app.run()
