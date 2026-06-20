def menu():
    print("=========")
    print("Main Menu")
    print("=========")

    print("1. Add Student")
    print("2. view Student")
    print("3. search Student")
    print("4. remove Student")
    print("5. Exit")

    choice = 0
    while True:
        choice = input("Enter your choice (1-5): ")
        if choice == "1":
            Add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            remove_student()
        elif choice == "5":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")
        

        

students = []
def add_student():
    print("What is the name?")
    name = str(input("Name: "))
    print("What is the age?")
    age = int(input("Age: "))
    print("What is the grade?")
    grade = float(input("Grade: "))

    student = {
        "name": name,
        "age": age,
        "grade": grade
    }
    students.append(student)

def search_student():
    name = input("Enter the name of the student: ")

    for student in students:
        if student["name"].lower() == name.lower():
            print("student found:")
            print("name:", student["name"])
            print("age:", student["age"])
            print("grade:", student["grade"])
            return
    print("Student not found.")

def view_students():
    if not students:
        print("No students found.")
        return
    for student in students:
        print("--------------------")
        print("Name:", student["name"])
        print("Age:", student["age"])
        print("Grade:", student["grade"])
        print("--------------------")
    

def remove_student():
    name = input("Enter the name of the student to remove: ")

    for student in students:
        if student["name"].lower() == name.lower():
            students.remove(student)
            print("Student removed.")
            return
    print("Student not found.")



menu()