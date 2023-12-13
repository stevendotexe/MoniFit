from datetime import date
import os
import json


def main():
    while True:
        try:
            selection = int(input("Pilih mode: \n1. Registrasi\n2. Login\nPilihan: "))
        except ValueError:
            print("Mohon pilih nomor antara 1 atau 2.")
        if selection == 1:
            register()
            break
        elif selection == 2:
            login()
            break
        else: pass

# registrasi user baru
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
    usernames = [user.rstrip('.json') for user in os.listdir("userinfo")] # list semua username di folder userinfo
    while True: # loop untuk input username & passowrd
        username = input("Username: ")
        if username in usernames:
            with open(f'userinfo/{username}.json', 'r') as file:
                data = json.load(file)
            # cek validitas password
            while True:
                pwinput = input("Password: ")
                if pwinput == data["password"]:
                    return True
                else:
                    while True:
                        try:
                            selection = int(input("1. Coba lagi\n2. Keluar dan registrasi\n\n Pilihan: "))
                            if selection == 1:
                                break # break jika user mau mencoba memasukkan password lagi
                            elif selection == 2:
                                exit()
                            else:
                                raise ValueError("Mohon pilih antara 1 dan 2.")
                        except ValueError:
                            print("Mohon pilih antara 1 dan 2.")

        else:
            print(f"Username dengan nama {username} tidak ditemkuan. Apakah anda ingin keluar dan registrasi?")
            while True:
                try:
                    selection = int(input("1. Coba lagi\n2. Keluar dan registrasi"))
                    if selection == 1:
                        break # break jika user mau mencoba memasukkan password lagi
                    elif selection == 2:
                        exit()
                    else:
                        raise ValueError
                except ValueError:
                    print("Mohon pilih antara 1 dan 2.")

if __name__ == '__main__':
    main()