class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    
    def introduce(self):
        print(f"Hello, my name is {self.name}, I am {self.age}")
        


        
student1 = Student("Yassine", 20, 85.5)
student2 = Student("Iramo", 22, 90.0)

student1.introduce()
student2.introduce()


