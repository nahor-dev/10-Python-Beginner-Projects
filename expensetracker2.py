class Expense:
    def __init__(self, title, amount, category, date):
        self.title = title
        self.amount = amount
        self.category = category
        self.date = date


class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, expense):
        self.expenses.append(expense)

    def view_expense(self):
        if not self.expenses:
            print("No expenses found.")
            return

        for i, expense in enumerate(self.expenses, start=1):
            print(f"\nExpense # {i}")
            print(f"Title: {expense.title}")
            print(f"Amount: {expense.amount}")
            print(f"Category: {expense.category}")
            print(f"Date: {expense.date}")

    def search_expense(self):
        title = input("Enter title: ").strip().lower()
        found = False

        for item in self.expenses:
            if title == item.title.lower():
                found = True
                print(f"Title: {item.title}")
                print(f"Amount: {item.amount}")
                print(f"Category: {item.category}")
                print(f"Date: {item.date}")

        if not found:
            print("Expense not found.")

    def delete_expense(self):
        title = input("Enter title: ").strip().lower()

        for item in self.expenses:
            if title == item.title.lower():
                self.expenses.remove(item)
                print("Expense deleted successfully.")
                return

        print("Expense not found.")

    def edit_expense(self):
        title = input("Enter title: ").strip().lower()

        for item in self.expenses:
            if title == item.title.lower():
                item.title = input("Enter new title: ").strip().lower()

                try:
                    item.amount = int(input("Enter new amount: "))
                except ValueError:
                    print("Amount can only be a number.")
                    return

                item.category = input("Enter new category: ").strip().lower()
                item.date = input("Enter new date (YYYY-MM-DD): ").strip()

                print("Expense updated successfully.")
                return

        print("Expense not found.")

    def total_expense(self):
        total = 0

        for item in self.expenses:
            total += item.amount

        print(f"Total expense: {total}")

    def highest_expense(self):
        if not self.expenses:
            print("No expenses found.")
            return

        highest = max(self.expenses, key=lambda item: item.amount)

        print(f"Title: {highest.title}")
        print(f"Amount: {highest.amount}")
        print(f"Category: {highest.category}")
        print(f"Date: {highest.date}")

    def lowest_expense(self):
        if not self.expenses:
            print("No expenses found.")
            return

        lowest = min(self.expenses, key=lambda item: item.amount)

        print(f"Title: {lowest.title}")
        print(f"Amount: {lowest.amount}")
        print(f"Category: {lowest.category}")
        print(f"Date: {lowest.date}")

    def category_summary(self):
        if not self.expenses:
            print("No expenses found.")
            return

        summary = {}

        for item in self.expenses:
            if item.category not in summary:
                summary[item.category] = 0

            summary[item.category] += item.amount

        print("\nCategory Summary")

        for category, total in summary.items():
            print(f"{category}: {total}")


def main():
    tracker = ExpenseTracker()

    while True:
        print(
            "\n========================"
            "\nEXPENSE TRACKER"
            "\n========================"
            "\n1. Add Expense"
            "\n2. View Expenses"
            "\n3. Search Expense"
            "\n4. Remove Expense"
            "\n5. Edit Expense"
            "\n6. Total Expenses"
            "\n7. Highest Expense"
            "\n8. Lowest Expense"
            "\n9. Category Summary"
            "\n10. Exit"
        )

        try:
            options = int(input("Enter your choice number: "))
        except ValueError:
            print("Only numbers are allowed.")
            continue

        if options == 1:
            title = input("Enter title: ").strip().lower()

            try:
                amount = int(input("Enter amount: "))
            except ValueError:
                print("Amount can only be a number.")
                continue

            category = input("Enter category: ").strip().lower()
            date = input("Enter date (YYYY-MM-DD): ").strip()

            expense = Expense(title, amount, category, date)
            tracker.add_expense(expense)

            print("Expense added successfully.")

        elif options == 2:
            tracker.view_expense()

        elif options == 3:
            tracker.search_expense()

        elif options == 4:
            tracker.delete_expense()

        elif options == 5:
            tracker.edit_expense()

        elif options == 6:
            tracker.total_expense()

        elif options == 7:
            tracker.highest_expense()

        elif options == 8:
            tracker.lowest_expense()

        elif options == 9:
            tracker.category_summary()

        elif options == 10:
            print("Thank you!")
            break

        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()