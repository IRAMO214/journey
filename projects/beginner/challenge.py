numbers = [1,2,3,4,5,6,7,8,9,10]

squares = [x ** 2 for x in numbers]

even = [x for x in numbers if x % 2 == 0]

num_square = {x: x ** 2 for x in numbers}

print(num_square)