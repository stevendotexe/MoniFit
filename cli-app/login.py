from datetime import date
import os
import json

def main():
    while True:
        try:
            selection = input("Pilih mode: \n1. Registrasi\n2. Login\n")
        except ValueError:
            print("Mohon pilih nomor antara 1 atau 2.")
        if selection == 1:
            register()
            break
        elif selection == 2:
            login()
            break
        else: pass

# Function to register a new user
def register():
    email = input("Masukkan email: ")
    day = date.today()
    usernames = [user.rstrip('.json') for user in os.listdir("userinfo")]
    print(usernames)

    while True:
        username = input("Masukkan username: ")
        if username in usernames or not username.isalnum():
            print(f"Username dengan nama {username} sudah ada atau tidak alfanumerik.")
        else:
            while True:
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
            break
def login():
    usernames = [user.rstrip('.json') for user in os.listdir("userinfo")]
    while True:
        username = input("Username: ")
        if username in usernames:
            with open(f'{username}.json', 'r'):
                pass
        else:
            print(f"Username dengan nama {username} tidak ditemkuan. Apakah anda ingin registrasi?")

if __name__ == '__main__':
    register()