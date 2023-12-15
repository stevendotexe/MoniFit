import login
from pyfiglet import Figlet
from time import sleep
import json
import pandas as pd

def main():
    username = user_login()

    print(figlet_render("MoniFit", font='nancyj'))
    print(figlet_render(f"Selamat datang,  {username}", 'mini'))

    with open(f'userinfo/{username}.csv', 'r') as file: # membuka data user sebagai dictionary
        user_data = json.load(file)
    
"""
user dictionary example
{
    "username": "username",
    "password": "username",
    "email": "email@email.com",
    "registration_date": "2023-12-13",
    "height": "80",
    "gender": "0",
    "activity_level": "3",
    "weight_history": {"2023-12-13":80}
}
"""

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
    
def figlet_render(text, font='drpepper'):
    fig = Figlet(font = font)
    return fig.renderText(text)

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