def menu():
    print("1. Add contact")
    print("2. View contacts")
    print("3. Edit contact")
    print("4. Delete contact")
    print("5. Exit")

contacts = {}

def add_contact():
    print("What is the name?")
    name = str(input("Name: "))
    print("What is the phone number?")
    phone_number = str(input("Phone Number: "))

    contacts[name] = phone_number

def view_contacts():
    for name, phone_number in contacts.items():
        print(f"Name: {name}, Phone Number: {phone_number}")

def edit_contact():
    print("What is the name of the contact you want to edit?")
    name = str(input("Name: "))
    if name in contacts:
        print("What is the new phone number?")
        phone_number = str(input("Phone Number: "))
        contacts[name] = phone_number
    else:
        print("Contact not found.")

def delete_contact():
    print("What is the name of the contact you want to delete?")
    name = str(input("Name: "))
    if name in contacts:
        del contacts[name]
        print("Contact deleted.")
    else:
        print("Contact not found.")

def contact_book():
    while True:
        menu()
        try:
            choice = int(input("Enter your choice (1-5): "))
            if choice < 1 or choice > 5:
                print("Invalid choice. Please enter a number between 1 and 5.")
                continue
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == 1:
            add_contact()
        elif choice == 2:
            view_contacts()
        elif choice == 3:
            edit_contact()
        elif choice == 4:
            delete_contact()
        elif choice == 5:
            print("Exiting the contact book. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

contact_book()