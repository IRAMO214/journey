def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Syntax Error!")
    return a / b

def calculator():
    print("Welcome to the Simple Calculator!")
    
    while True:
        print("\nSelect an operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        try:
            choice = int(input("Enter your choice (1-5): "))
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 5.")
            continue

        while choice < 1 or choice > 5:
            print("Invalid choice! Please select a valid operation.")
            try:
                choice = int(input("Enter your choice (1-5): "))
            except ValueError:
                print("Invalid input! Please enter a number between 1 and 5.")
                break

        if choice == 5:
            print("Exiting the calculator. Goodbye!")
            return

        if choice < 1 or choice > 4:
            continue

        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid input! Please enter numeric values.")
            continue

        if choice == 1:
            result = add(num1, num2)
            operation = "Addition"
        elif choice == 2:
            result = subtract(num1, num2)
            operation = "Subtraction"
        elif choice == 3:
            result = multiply(num1, num2)
            operation = "Multiplication"
        elif choice == 4:
            try:
                result = divide(num1, num2)
                operation = "Division"
            except ValueError as e:
                print(e)
                continue

        print("The result of", operation, " is:", result)


calculator()