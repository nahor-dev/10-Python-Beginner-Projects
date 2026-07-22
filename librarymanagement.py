books = {
    "Atomic Habits": {
        "author": "James Clear",
        "year": 2018,
        "available": False,
        "borrowed_by": 'nahor'
    }
}
members  = {
     "john": {
        "phone": "0912345678",
        "borrowed_books": [
            "Atomic Habits",
            "Clean Code"
        ]
    }
}
# print(members)

def view_book():
    if not books:
        print('No books found.')
    else:
        for i,(book, descriptions )in enumerate(books.items(), 1):
            print(f'{i}. {book}')
            print()
            print(f'author:{descriptions['author']}')
            print(f'year:{descriptions['year']}')
            
            if descriptions['borrowed_by']:
                if not descriptions['available'] :
                    print(f'status:borrowed') 
                print(f'borrowed_by:{descriptions['borrowed_by']}')
            else:
                if descriptions['available'] :
                    print(f'status:available') 
                       
def add_book():
    current_year = 2026
    book_title = input('Book title: ').title().strip()
    if not book_title:
        print('book title cannot be empty')
        return
    if not book_title in books:
        author = input('Author: ').strip()
        try:
            year = int(input('Publication year: '))
        except ValueError:
            print('enter valid number only!')
            return
        if not 1000 <year < current_year:
            print(f'Enter a valid publication year.')
            return
        
        books[book_title]= {
            'author' : author ,
            'year' : year,
            "available" : True,
            "borrowed_by": None
        }
        
        print('saved successfully!')
    else:
        print('this book already exist! ')
        return

def search_book():
    search = input('Enter book title or author: ').strip().lower()
    

    found = False

    for book in books:
        if search in book.lower() or search in books[book]["author"].lower():
            view_book()
            found = True

    if not found:
        print('This book does not exist.')
    
def register_member():

    members_name = input('Enter member name: ').title().strip()
    if members_name in members:
        print('this name already exist')
        return
    
    else:
        
        members_phone = input('Enter phone: ')
        if isinstance(members_phone, int) or members_phone[0] =='+' :
        
            members[members_name] = {
                'phone' :members_phone ,
                'borrowed_books':[]
            }
            
            print('Member registered successfully!')
        else:
            print('phone number only contain numbers data type')
            return
  
def view_members():
    if not members:
        print('there\'s no member')
        return
    
    for i,(name,properties) in enumerate(members.items(), 1):
        print(f'{i}. {name}')
        print(f'phone : {properties['phone']}')
        print(f'Borrowed_books : {len(properties['borrowed_books'])}')
        print()   


def borrow_book():
    borrower_name = input('Enter your name: ').lower().strip()
    for name in members:
        if not borrower_name in name.lower():
            print('Member not found.')
            return
    
    wanted_book = input('Enter book title or author:  ').lower().strip()
    for book in books:
        if not wanted_book in book.lower():
            print('Book not found.')
            return

    


def main():
    while True:
        print('==============================\nLIBRARY MANAGEMENT SYSTEM\n==============================\n1. View Books \n2. Add Book\n3. Remove Book\n4. Search Book\n5. Register Member\n6. Borrow Book\n7. Return Book\n8. View Members\n9. View Borrowed Books\n10. Library Statistics\n11. Exit')
        try:
            options = int(input('Choose an option: '))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        
        if options ==1:
            view_book()
        elif options ==2:
            add_book()
        elif options ==4:
            search_book()
        elif options ==5:
            register_member()
        elif options ==6:
            borrow_book()
        elif options ==8:
            view_members()
        elif options == 11:
            print('thank you')
            break  
        
if __name__ =="__main__":
    main()