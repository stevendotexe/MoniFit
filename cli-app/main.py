import login
from figletrender import figlet_render
from time import sleep
import json
import pandas as pd
import csv

def main():
    username = user_login()

    print(figlet_render("MoniFit", font='nancyj'))
    print(figlet_render(f"Selamat datang,  {username}", 'mini'))

    with open(f'userinfo/{username}.csv', 'r') as file: # membuka data user sebagai dictionary
        user_data = csv.DictReader(file, fieldnames = [])

def user_login():
    selection = user_selection()
    if selection == 1:
        username = login.register()
        return username
    elif selection == 2:
        username = login.login()
        return username
    elif selection == 3:
        pass # lupaPassword to be completed
    else:
        sleep(0.5); print("Exiting application..."); sleep(2); exit()
        

def user_selection():
    print("Selamat datang di\n"+figlet_render("MoniFit\n")+"Pilih opsi:")
    print("1. Registrasi")
    print("2. Login")
    print("3. Lupa password")
    print("4. Keluar")
    print("Untuk keluar aplikasi dalam stage apapun, mohon tekan CTRL + C")
    print()
    possibilities = [1, 2, 3, 4]
    while True:
        try:
            selection = int(input("Pilihan: "))
            if selection in possibilities:
                return selection
            else:
                raise ValueError("Mohon pilih nomor 1 atau 2.")
        except ValueError:
            print("Mohon pilih nomor 1 atau 2.")


if __name__ == '__main__':
    while True:
        try:
            main()
        except KeyboardInterrupt:
            s = (input("\nExit application? (Y/N): ").lower())
            if s == 'y' or s == 'yes':
                print("\nExiting application..."); sleep(1); exit()
            else:
                pass