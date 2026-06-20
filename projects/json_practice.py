import json

student = {
    "name": "Iramo",
    "age": 25,
    "grade": 17.5
}

with open('student.json', 'w') as file:
    json.dump(student, file)

with open('student.json', 'r') as file:
    loaded_student = json.load(file)

print(loaded_student)
print("-------------")
print(loaded_student["name"])