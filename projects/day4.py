def greet(name):
    print("Hello", name, "!")


greet("Iramo")


def add(a, b):
    return a + b

result = add(5, 4)
print(result)

def square(num):
    return num ** 2

def cube(num):
    return num ** 3

num = 3
print("square of "+ str(num) + " is:" + str(square(num)))
print("cube of "+ str(num) + " is:" + str(cube(num)))