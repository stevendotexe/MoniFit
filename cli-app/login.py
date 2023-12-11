from datetime import date
import os
import json

# Function to register a new user
def register():
    email = input("Masukkan email: ")
    day = date.today()
    usernames = [user.rstrip('.json') for user in os.listdir("userinfo")]
    while True:
        while True:
            username = input("Masukkan username: ")
            if username in usernames and not username.isalnum():
                print(f"Username dengan nama {username} sudah ada atau tidak alfanumerik.")
            else:
                break
        password = input("Masukkan password: ")
        if len(password) >= 8:   
            with open(f'userinfo/{username}.json', 'w') as file:
                file.write("{\n")
                file.write(f'"username": "{username}",\n')
                file.write(f'"password": "{password}",\n')
                file.write(f'"email": "{email}",\n')
                file.write(f'"registration_date": "{day}",\n')
                file.write('"weight_history": ' + '{'+f'"{day}":' +  '0' + '}\n')
                file.write("}\n")
            print("Registrasi sukses!")
            break
        else:
            print("Password harus lebih dari 8 karakter.")

def login():
    usernames = [user.rstrip('.json') for user in os.listdir("userinfo")]
    while True:
        username = input("Username: ")
        if username in usernames:
            with open(f'{username}.json', 'r'):
                pass

usernam2es = [user.rstrip('.json') for user in os.listdir("userinfo")]
print(usernam2es)


def lupa_password():
    pass
