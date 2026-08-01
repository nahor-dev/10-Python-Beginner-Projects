class Expense:
    def __init__(self,title,amount,category,date):
        self.title = title
        self.amount = amount
        self.category = category
        self.date = date
        
        


        
class ExpenseTracker:
    def __init__(self):
        self.expenses = []
    
    def add_expense(self,expense):
        self.expenses.append(expense)
    
    def view_expense(self):
        
        if not self.expenses:
            print('No expenses found.')
            return
        else:
            for i, expense in enumerate(self.expenses , start=1):
                print(f'expense # {i}.')
                print(f'title: {expense.title}')
                print(f'amount: {expense.amount}')
                print(f'category: {expense.category}')
                print(f'date: {expense.date}')

    def search_expense(self):
        
        title = input('enter title: ').strip().lower()
        found = False
        for item in self.expenses:
            if title == item.title:
                found = True
                print(f'title: {item.title}')
                print(f'amount: {item.amount}')
                print(f'category: {item.category}')
                print(f'date: {item.date}')
        if not found:
            print("Expense not found.")
    
    def delete_expense(self):
        title = input('enter title: ').strip().lower()
        
        for item in self.expenses:
            if title == item.title:
                self.expenses.remove(item)
                found = True
                print('expense deleted successfully')
                return
        if not found:
            print('Expense not found.')
        
    def edit_expense(self):
        title = input('enter title: ').strip().lower()
        
        for item in self.expenses:
            if title == item.title:
                item.title = input('enter new title: ').strip().lower()
                item.amount = int(input('enter new amount: '))
                item.category = input('enter new category: ').strip().lower()
                item.date = input("Enter new date (YYYY-MM-DD): ").strip()
                print('Expense updated successfully.')
                return
        else:
            print('Expense not found.')   
    
    def total_expense(self):
        total = 0
        for item in self.expenses:
            total += item.amount
        print(f'total expense: {total}')
    
    def highest_expense(self):
        if self.expenses:
            highest = max(self.expenses, key= lambda item: item.amount)
            print(f'title: {highest.title}')
            print(f'amount: {highest.amount}')
            print(f'category: {highest.category}')
            print(f'date: {highest.date}')
            return
        else:
            print('No expenses found.')
    
    def lowest_expense(self):
        if self.expenses:
            lowest = min(self.expenses, key= lambda item: item.amount)
            print(f'title: {lowest.title}')
            print(f'amount: {lowest.amount}')
            print(f'category: {lowest.category}')
            print(f'date: {lowest.date}')
            return
        else:
            print('No expenses found.')



def main():
   
   
    tracker = ExpenseTracker()
    while True:
        print('\n========================\nEXPENSE TRACKER\n========================\n\n1. Add Expense\n2. View Expenses\n3. Search Expense\n4. Remove Expense\n5. Edit expense\n6. Total Expenses\n7. Highest Expense\n8. Lowest Expense\n11. Exit\n')
        try:
            options = int(input('enter your choice number : '))
        except ValueError:
            print('only number allowed ')
            continue
        if options==1:
            title = input('enter title: ').strip().lower()
            try:
                amount = int(input('enter amount: '))
            except ValueError:
                print('amount can only be number.')
            category = input('enter category: ').strip().lower()
            date = input("Enter date (YYYY-MM-DD): ").strip()
            expense = Expense(title,amount,category,date)
            tracker.add_expense(expense)
            print('expense added successfully')
            
        elif options==2:
            tracker.view_expense()
        elif options==3:
            tracker.search_expense()
            
        elif options==4:
            tracker.delete_expense()
        elif options==5:
            tracker.edit_expense()
        elif options==6:
            tracker.total_expense()
        elif options==7:
            tracker.highest_expense()  
        elif options==8:
            tracker.lowest_expense()  
            
        elif options==11:
            print('thank you ')
            return
        

if __name__ == "__main__":
    main()
                