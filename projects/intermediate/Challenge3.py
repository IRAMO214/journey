class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

users = []

admin = User("admin", "AdminPassword")
user1 = User("user1", "User1Password")
users.append(admin)
users.append(user1)

def get_username():
    username = input("Username:\n")
    return username

def check_username(username):
    for user in users:
        if username == user.username:
            return True
    return False

def get_password():
    password = input("Password:\n")
    return password

def check_password(username, password):
    for user in users:
        if user.username == username and user.password == password:
            return True
    return False

def log_in():
    attempt = 3
    while attempt > 0:
        username = get_username()
        if check_username(username):
            password = get_password()
            if check_password(username, password):
                print("Logged in\n")
                break
            else:
                print("Incorecct password\n")
                attempt -= 1
                print("Attempts left : "+str(attempt))
                
        else:
            print("Invalid credential\n")
            attempt -= 1
            print("Attempts left : "+str(attempt))
            
    if attempt <= 0:
        print("Blocked")

log_in()

