with open('note.txt', 'w') as file:
    file.write('Python\n')
    file.write('Cybersecurity\n')
    file.write('Networking\n')


#with open('note.txt', 'r') as file:
#   content = file.read()
#    print(content)


with open('note.txt', 'r') as file:
    for line in file:
        print(line.strip())


with open('note.txt', 'a') as file:
    file.write("Socket")

print("------------------")

with open('note.txt', 'r') as file:
    for line in file:
        print(line.strip())


try:
    with open('script.txt', 'r') as file:
        content = file.read()
except FileNotFoundError:
    print("No such file in directory.\n")

