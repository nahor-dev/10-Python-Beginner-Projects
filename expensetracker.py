
expenses = {
    'food':{
        'title':'burger',
        'amount':20,
        'date':20
    },
    'transport':{
        'title':'',
        'amount':20,
        'date':''
    },
    'entertainment':{
        'title':'',
        'amount':20,
        'date':''
    },
    'shopping':{
        'title':'',
        'amount':20,
        'date':''
    },
    'bills':{
        'title':'',
        'amount':20,
        'date':''
    },
    'education':{
        'title':'',
        'amount':20,
        'date':''
    },
    'health':{
        'title':'',
        'amount':40,
        'date':''
    }
}



def add_expense():
    
    
    print('\n========================\nEXPENSE TRACKER\n========================\n\n1. food\n2. transport\n3. entertainment\n4. shopping\n5. bills\n6. education\n7. health\n8. other\n')
    category = int(input('enter category : '))
    if not isinstance(category,int):
        print('only number allowed ')
        return
    title = input('insert title : ').lower().strip()
    amount = int(input('insert amount : '))
    if not isinstance(category,int):
            print('only number allowed ')
            return
    date = int(input('insert date : '))
    if not isinstance(category,int):
            print('only number allowed ')
            return
    
    if category ==1:
        expenses['food']['title'] = title
        expenses['food']['amount'] = amount
        expenses['food']['date'] = date
    elif category ==2:
        expenses['transport']['title'] = title
        expenses['transport']['amount'] = amount
        expenses['transport']['date'] = date
    elif category ==3:
        expenses['entertainment']['title'] = title
        expenses['entertainment']['amount'] = amount
        expenses['entertainment']['date'] = date
    elif category ==4:
        expenses['shopping']['title'] = title
        expenses['shopping']['amount'] = amount
        expenses['shopping']['date'] = date
    elif category ==5:
        expenses['bills']['title'] = title
        expenses['bills']['amount'] = amount
        expenses['bills']['date'] = date
    elif category ==6:
        expenses['education']['title'] = title
        expenses['education']['amount'] = amount
        expenses['education']['date'] = date
    elif category ==7:
        expenses['health']['title'] = title
        expenses['health']['amount'] = amount
        expenses['health']['date'] = date
    elif category==8:
        category = input('create category : ').lower().strip()
        expenses[category]={
            'title':title,
            'amount': amount,
            'date': date
        }

    print('successfully added')
    

def view_expenses():
    for i, category  in enumerate(expenses, start=1):
        print(f'{i}. {category}')
        print(f'title: {expenses[category]['title']}')
        print(f'amount: {expenses[category]['amount']}')
        print(f'date: {expenses[category]['date']}')

    
def search_expense():
    
    for category  in expenses:
        print(f'{category}')
    print('others? type below')
    category = input('enter category: ') 
    print()
    print(f'category: {category}')   
    print(f'title: {expenses[category]['title']}')   
    print(f'amount: {expenses[category]['amount']}')   
    print(f'date: {expenses[category]['date']}')   
            
            
            
def remove_expense():
    for category in expenses:
        print(f'{category}')
    print('others? type below')
    category = input('enter category: ') 
    
    del expenses[category]
    
    print('successfully deleted')
    
def total_expenses():
    total = 0
    for category, descriptions in expenses.items():
        total +=descriptions['amount']
        
    print(f'total expense: {total}')
        
def monthly_report():
    ...
def category_summary():
    ...
def highest_expense():
    ...
 
def lowest_expense():
    ...
def save_data():
    ...

    
    
    
    




while True:
    print('\n========================\nEXPENSE TRACKER\n========================\n\n1. Add Expense\n2. View Expenses\n3. Search Expense\n4. Remove Expense\n5. Total Expenses\n6. Monthly Report\n7. Category Report\n8. Highest Expense\n9. Lowest Expense\n10. Save\n11. Exit\n')
    try:
        options = int(input('enter your choice number : '))
        if options > 11:
            print('enter number b/n 1 to 11 only')

    except ValueError:
        print('only number allowed')
        
    if options==1:
        add_expense()
    elif options==2:
        view_expenses()
    elif options==3:
        search_expense()
    elif options==4:
        remove_expense()
    elif options==5:
        total_expenses()
    elif options==6:
        monthly_report()
    elif options==7:
        category_summary()
    elif options==8:
        highest_expense()
    elif options==9:
        lowest_expense()
    elif options==10:
        save_data()
    elif options==11:
        print('thank you ')
        break
