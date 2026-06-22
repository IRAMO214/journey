fruits = ["apple", "banana", "orange"]

print(fruits[0])  # Output: apple

fruits.append("mango")

fruits.remove("banana")

print(len(fruits))

for fruit in fruits:
    print(fruit)

squares = [x ** 2 for x in range (1, 11)]

print(squares)

evens = [x for x in range(1, 21) if x % 2 == 0]
print(evens)

cordinates = (1, 10)

print(cordinates[0])  # Output: 1


#cordinates[0] = 5

numbers = {1, 2, 2, 3, 4, 4, 5, 6, 7}

print(numbers)

numbers.add(10)
print(numbers)
numbers.remove(3)
print(numbers)

student = {
    "name": "Yassine",
    "age": 20,
    "grade": 85.5
}

print(student["name"])
student["grade"] = 90.0
print(student["grade"])
student["city"] = "Ifrane"
print(student)

for key, value in student.items():
    print(value)
    