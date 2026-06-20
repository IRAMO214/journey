with open('notes.txt', 'w') as notes:
    notes.write("Hello World!\n")

with open('notes.txt', 'a') as notes:
    notes.write("Python is fun.\n")

with open('notes.txt', 'r') as notes:
    content = notes.read()
    print(content)

try:
    number = int(input("Enter a number: "))
except ValueError:
    print("Please enter a valid integer.")

student = {
    "name": "Iramo",
    "age":25,
}

import json

with open('student.json', 'w') as file:
    json.dump(student, file)

with open('student.json', 'r') as file:
    student = json.load(file)
print(student["name"])

