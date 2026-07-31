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



def main():
   
    
    tracker = ExpenseTracker(expense)
    while True:
        print('\n========================\nEXPENSE TRACKER\n========================\n\n1. Add Expense\n2. View Expenses\n3. Exit\n')
        try:
            options = int(input('enter your choice number : '))
        except ValueError:
            print('only number allowed ')
            continue
        if options==1:
            title = input('enter title: ').strip().lower()
            amount = int(input('enter amount: '))
            category = input('enter category: ').strip().lower()
            date = input("Enter date (YYYY-MM-DD): ").strip()
            expense = Expense(title,amount,category,date)
            
        elif options==2:
            tracker.view_expense()
        elif options==3:
            print('thank you ')
            return
        
        
        
        
main()   
                