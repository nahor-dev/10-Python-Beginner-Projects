import json


books = {
     "Atomic Habits": {
        "author": "James Clear",
        "year": 2018,
        "available": True,
        "borrowed_by": None
    },
}
members  = {}
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
    borrower_name = input('Enter your name: ').title().strip()
    if borrower_name not in members:
            print('Member not found.')
            return
    
    wanted_book = input('Enter book title:  ').title().strip()
    if wanted_book not in books:
            print('Book not found.')
            return

    if not books[wanted_book]['available']:
            print(f'This book is already borrowed by {books[wanted_book]['borrowed_by']}.')
            return
    books[wanted_book]['available'] = False
    books[wanted_book]['borrowed_by'] = borrower_name
    members[borrower_name]['borrowed_books'].append(wanted_book)
    
def return_book():
    borrower_name = input('Enter your name: ').title().strip()
    if borrower_name not in members:
            print('Member not found.')
            return
    wanted_book = input('Enter book title:  ').title().strip()
    if wanted_book not in books:
            print('Book not found.')
            return
        
    if books[wanted_book]['available']:
            print(f'This book was not borrowed.')
            return
        
    if books[wanted_book]["borrowed_by"] != borrower_name:
        print(f"This book was borrowed by {books[wanted_book]['borrowed_by']}, not {borrower_name}.")
        return
    books[wanted_book]['available'] = True
    books[wanted_book]['borrowed_by'] = None
    members[borrower_name]['borrowed_books'].remove(wanted_book)
    print("Book returned successfully!")
    
    
    
def remove_book():
    book_title = input('Book title: ').title().strip()
    if not book_title in books:
        print('the book does not exist')
    if not books[book_title]['available']:
        print('the book is currently borrowed')
    del books[book_title]
    print('deleted successfully')


def view_borrowed_books():
    for i,(book, descriptions )in enumerate(books.items(), 1):
        if not descriptions['available']:
            print(f'{i}. {book}')
            print(f'borrowed_by: {descriptions['borrowed_by']}')
        else:
            print('there is no book borrowed')
            return
  
  
  
def save_books():
    with open("books.json", "w") as file:
        json.dump(books, file,indent=4)          
save_books()        
def library_statistics():
    print('===== Library Statistics =====\n')
    book_len = len(books)
    print(f'Total Books: {book_len}')
    book_len_avl = 0
    for book,descriptions in books.items():
        
        if descriptions['available']:
            
            book_len_avl+=1
    print(f"Available Books: {book_len_avl}")
    book_len_bor = 0
    for book,descriptions in books.items():
        
        if not descriptions['available']:
            
            book_len_bor+=1
    print(f"Borrowed Books: {book_len_bor}")
    member_len = len(members)
    print(f'Total Books: {member_len}')
    


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
        elif options ==3:
            remove_book()
        elif options ==4:
            search_book()
        elif options ==5:
            register_member()
        elif options ==6:
            borrow_book()
        elif options==7:
            return_book()
        elif options ==8:
            view_members()
        elif options==9:
            view_borrowed_books()
        elif options==10:
            library_statistics()
        elif options == 11:
            print('thank you')
            break  
        
if __name__ =="__main__":
    main()