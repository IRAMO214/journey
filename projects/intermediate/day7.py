class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

class Student(Person):
    count = 0
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade
        Student.count += 1
    def introduce(self):
        print(f"Hello, my name is {self.name}, I am {self.age} years old and my grade is {self.grade}.")
    @classmethod
    def total_students(cls):
        return cls.count

class Teacher(Person):
    def __init__(self, name, age, subject, salary):
        super().__init__(name, age)
        self.subject = subject
        self.salary = salary
    
    def introduce(self):
        print(f"Hello, my name is {self.name}, I am {self.age} years old, I teach {self.subject} and I earn {self.salary} dollars.")
    
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance
    
    def deposit(self, amount):
        self.__balance += amount
        print(f"Deposited {amount} dollars. New balance: {self.__balance} dollars.")
    
    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient funds.")
        else:
            self.__balance -= amount
            print(f"Withdrew {amount} dollars. New balance: {self.__balance} dollars.")

    def get_balance(self):
        return self.__balance

class Math:
    @staticmethod
    def add(a, b):
        return a + b
    
    @staticmethod
    def subtract(a, b):
        return a - b
    
    @staticmethod
    def multiply(a, b):
        return a * b
    
    @staticmethod
    def divide(a, b):
        if b == 0:
            print("Cannot divide by zero.")
            return None
        return a / b
    
class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return (celsius * 9/5) + 32
    
    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        return (fahrenheit - 32) * 5/9



student1 = Student("Yassine", 20, 85.5)
student2 = Student("Iramo", 22, 90.0)
student3 = Student("Sara", 19, 92.0)

print(Student.total_students())