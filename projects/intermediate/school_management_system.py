class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade
    def introduce(self):
        print(f"Hello, my name is {self.name}, I am {self.age} years old and my grade is {self.grade}.")

class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject
    
    def introduce(self):
        print(f"Hello, my name is {self.name}, I am {self.age} years old, I teach {self.subject}.")

class Course:
    def __init__(self, name, teacher):
        self.name = name
        self.teacher = teacher
        self.students = []

    
    def add_student(self, student):
        self.students.append(student)
    
    def remove_student(self, student):
        self.students.remove(student)

    def display_students(self):
        print(f"Students in {self.name}:")
        for student in self.students:
            print(student.name)

class School:
    def __init__(self, name):
        self.name = name
        self.courses = []
        self.teachers = []
    
    def add_course(self, course):
        self.courses.append(course)
    
    def add_teacher(self, teacher):
        self.teachers.append(teacher)
    
    def add_student(self, student, course):
        course.add_student(student)
    
    def remove_student(self, student, course):
        course.remove_student(student)

    def display_everything(self):
        print(f"School: {self.name}")
        print("Courses:")
        for course in self.courses:
            print(f"  - {course.name}")
        print("Teachers:")
        for teacher in self.teachers:
            print(f"  - {teacher.name}")