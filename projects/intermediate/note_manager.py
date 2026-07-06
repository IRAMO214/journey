def menu():
    print("1. add note")
    print("2. view notes")
    print("3. Exit")

def add_note():
    note = (input("Enter your note:"))
    with open('note.txt', 'a') as file:
        file.write(note + "\n")

def view_notes():
    print("Here are your notes:")
    with open('note.txt', 'r') as file:
        print(file.read())

def note_manager():
    print("Welcome to Note Manager.")
    try:
        with open('note.txt', 'r') as file:
            pass
    except FileNotFoundError:
        with open('note.txt', 'x') as file:
            pass
    
    while True:
        menu()
        try:
            choice = int(input("Please Enter your choice:\n"))
        except ValueError:
            print("Please enter a valid choice (1, 2, or 3)\n")
            continue
        
        if choice == 1:
            add_note()
            print()
        elif choice == 2:
            view_notes()
            print()
        elif choice == 3:
            print("Exit program\nBye bye!")
            break
        else:
            print("Invalid choice. Please try again.\n")


note_manager()
