print("=====================================")
print("          CONTACT BOOK")
print("=====================================")

contacts = {}

while True:

    try:
        option = int(input("""
1. View Contacts
2. Add Contact
3. Search Contact
4. Edit Contact
5. Delete Contact
6. Exit

Choose an option: """))
    except ValueError:
        print("Please enter a number between 1 and 6.")
        continue

    # ================= VIEW =================

    if option == 1:

        if not contacts:
            print("\nNo contacts found.\n")
        else:
            print("\n========== CONTACTS ==========")

            for i, (name, details) in enumerate(contacts.items(), start=1):
                print(f"\n{i}. {name}")
                print(f"   Phone : {details['phone']}")
                print(f"   Email : {details['email']}")

    # ================= ADD =================

    elif option == 2:

        name = input("Enter name: ").strip()

        if name in contacts:
            print("Contact already exists.")
        else:
            phone = input("Enter phone number: ").strip()
            email = input("Enter email: ").strip()

            contacts[name] = {
                "phone": phone,
                "email": email
            }

            print("Contact added successfully!")

    # ================= SEARCH =================

    elif option == 3:

        name = input("Enter contact name: ").strip()

        if name in contacts:

            print("\nContact Found")
            print(f"Name  : {name}")
            print(f"Phone : {contacts[name]['phone']}")
            print(f"Email : {contacts[name]['email']}")

        else:
            print("Contact not found.")

    # ================= EDIT =================

    elif option == 4:

        name = input("Enter contact name to edit: ").strip()

        if name in contacts:

            phone = input("Enter new phone number: ").strip()
            email = input("Enter new email: ").strip()

            contacts[name]["phone"] = phone
            contacts[name]["email"] = email

            print("Contact updated successfully!")

        else:
            print("Contact not found.")

    # ================= DELETE =================

    elif option == 5:

        name = input("Enter contact name to delete: ").strip()

        if name in contacts:

            del contacts[name]

            print("Contact deleted successfully!")

        else:
            print("Contact not found.")

    # ================= EXIT =================

    elif option == 6:

        print("Thank you for using Contact Book!")
        break

    # ================= INVALID =================

    else:
        print("Please choose a number between 1 and 6.")