

print('=====================================')
print('       CONTACT BOOK')
print('=====================================')

contacts = {
 
   
    
}
while True:

    option = int(input('''
    1. View Contacts
    2. Add Contact
    3. Search Contact
    4. Edit Contact
    5. Delete Contact
    6. Exit

    Choose an option:'''))
    
    
    if option ==1:
        if contacts:
            for i,(name , details) in enumerate(contacts.items(), start=1):
                print(f'{i}. {name}')
                for key, value in details.items():
                    print(f'{key}:{value}')
        else:
            print('No contacts found.')
    
    elif option ==2:
       while True:
           name = input('Enter name(type done to finish):  ')
           if name.lower() =='done':
               print('Contact added successfully!')
               break
           global phone
           global email
           phone = int(input(f'Enter phone number for {name}: '))
           email = input(f'Enter email for {name}: ')
           
           contacts[name] = {
               'phone' : phone,
               'email' : email
           }
    elif option==3:
        cont_name = input('Enter contact name: ')
        if cont_name in contacts.keys():
           cont_info = contacts.get(cont_name)
           print(f'name: {cont_name}')
           for key, value in cont_info.items():
               print(f'{key}: {value}')
        else:
            print('Contact not found.')
    elif option==4:
        while True:
            cont_name = input('Enter contact name(type done to finish): ')
            if cont_name.lower() =='done':
               print('Contact updated successfully!')
               break      
            if cont_name in contacts.keys():
                phone_up = int(input(f'Enter phone number for {cont_name}: '))
                email_up = input(f'Enter email for {cont_name}: ')
                contacts[cont_name]['phone'] = phone_up
                contacts[cont_name]['email'] = email_up
            else:
                print('contact not found ')
    elif option==5:
        while True:
            cont_name = input('Enter contact name(type done to finish): ')
            if cont_name.lower() =='done':
               print('Contact deleted successfully!')
               break     
            if cont_name in contacts.keys():
                del contacts[cont_name]   
            else:
                print('contact not found ')
    elif option ==6:
        print('thank you !')
        break
    
    
    
    
    
    
    
    
    
    
    
