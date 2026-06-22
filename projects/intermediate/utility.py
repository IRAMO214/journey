grade = []
def add_student():
    global grade
    print("What is the name?")
    name = str(input("Name: "))
    print("What is the grade?")
    try:
        student_grade = float(input("Grade: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    student = {
        "name": name,
        "grade": student_grade
    }

    grade.append(student["grade"])

def avg_grade():
    if not grade:
        print("No grades available.")
        return
    average = sum(grade) / len(grade)
    print("The average grade is:", average)

def highest_grade():
    if not grade:
        print("No grades available.")
        return
    highest = max(grade)
    print("The highest grade is:", highest)

def menu():
    while True:
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. Average Grade")
        print("3. Highest Grade")
        print("4. Exit")

        try:
            choice = int(input("Enter your choice (1-4): "))
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 4.")
            continue

        if choice == 1:
            add_student()
        elif choice == 2:
            avg_grade()
        elif choice == 3:
            highest_grade()
        elif choice == 4:
            print("Exiting the Student Management System. Goodbye!")
            break
        else:
            print("Invalid choice! Please select a valid option.")