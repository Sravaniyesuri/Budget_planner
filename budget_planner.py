class BudgetPlanner:
    def __init__(self):
        self.monthly_income = 0
        self.monthly_expenses = {}

    def add_income(self, income):
        self.monthly_income += income

    def add_expenses(self, category, amount):

        if category in self.monthly_expenses:
            self.monthly_expenses[category] += amount
        else:
            self.monthly_expenses[category] = amount

    def get_total_expenses(self):
        return sum(self.monthly_expenses.values())

    def get_balance(self):
        return self.monthly_income - self.get_total_expenses()

    def get_expenses_by_category(self):
        return self.monthly_expenses

    def reset_budget(self):
        self.monthly_income = 0
        self.monthly_expenses = {}

if __name__ == "__main__":
    planner = BudgetPlanner()
    while True:
        print("\nPersonal Budget Planner")
        print("1. Add Income")
        print("2. Add Expenses")
        print("3. View Total Expenses")
        print("4. View Balance")
        print("5. View Expenses by Category")
        print("6. Reset Budget")
        print("7. Quit")

        choice = input("Enter your choice :")

        if choice == "1":
            try:
                income = float(input("Enter Income amount :"))
                planner.add_income(income)
                print("Income added successfully.")
            except ValueError:
                print("Invalid amount. Please enter a number.")
        elif choice == "2":
            category = input("Enter expense category :")
            try:
                amount = float(input("Enter expense amount:"))
                planner.add_expenses(category, amount) # Corrected from add_expense
                print("Expense added successfully.")
            except ValueError:
                print("Invalid amount. Please enter a number.")
        elif choice == "3":
            total_expense = planner.get_total_expenses()
            print(f"Total Expenses : {total_expense}") # Corrected variable name
        elif choice == "4":
            balance = planner.get_balance()
            print(f"Balance :{balance}")
        elif choice == "5":
            expenses_by_category = planner.get_expenses_by_category()
            print("Expenses by category :")
            if expenses_by_category:
                for category, amount in expenses_by_category.items():
                    print(f"- {category}: {amount}")
            else:
                print("No expenses added yet.")
        elif choice == "6":
            planner.reset_budget()
            print("Budget reset successfully.")
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")