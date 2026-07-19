
books = {
    # "Atomic Habits": {
    #     "author": "James Clear",
    #     "year": 2018,
    #     "available": True,
    #     "borrowed_by": None
    # },
}
members  = {
    # "Nahor": {
    #     "borrowed": ["Atomic Habits" ]
    # }
}

def view_book():
    for book, descriptions in books.items():
        print(book)
        print()
        for key,value in descriptions.items():
            print(f'{key}:{value}')
            print()
    
        
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
        elif options == 11:
            print('thank you')
            break    
main()