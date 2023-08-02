class ExpenseTracker:
    def __init__(self):
        self.transactions = []

    def add_transaction(self, description, amount):
        self.transactions.append({"description": description, "amount": amount})

    def view_transactions(self):
        if not self.transactions:
            print("No transactions found.")
        else:
            print("Date\t\tDescription\t\tAmount")
            print("-------------------------------------------")
            for transaction in self.transactions:
                print(f"{transaction['description']}\t\t${transaction['amount']:.2f}")

def main():
    expense_tracker = ExpenseTracker()

    while True:
        print("\nExpense Tracker")
        print("1. Add Transaction")
        print("2. View Transactions")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            description = input("Enter the transaction description: ")
            amount = float(input("Enter the transaction amount: "))
            expense_tracker.add_transaction(description, amount)
            print("Transaction added successfully.")
        elif choice == '2':
            expense_tracker.view_transactions()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

    print("Thank you for using the Expense Tracker!")

if __name__ == "__main__":
    main()
