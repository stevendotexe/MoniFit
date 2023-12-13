import login
from pyfiglet import Figlet
from time import sleep
import json

def main():
    try:
        selection = user_selection()

        if selection == 1:
            username = login.register()
        elif selection == 2:
            username = login.login()
        elif selection == 3:
            pass # lupaPassword to be completed
        else:
            sleep(0.5); print("Exiting application..."); sleep(2); exit()
    except KeyboardInterrupt:
        print("\nExiting application..."); sleep(2); exit()
    
    # line below applies if user have logged in.

    print(figlet_render("MoniFit", font='nancyj'))
    print(figlet_render(f"Selamat datang,  {username}", 'mini'))

    with open(f'userinfo/{username}.json', 'r') as file: # membuka data user sebagai dictionary
        user_data = json.load(file)

def figlet_render(text, font='drpepper'):
    fig = Figlet(font = font)
    return fig.renderText(text)

def user_selection():
    print("Selamat datang di\n"+figlet_render("MoniFit\n")+"Pilih opsi:")
    print("1. Registrasi")
    print("2. Login")
    print("3. Lupa password")
    print("4. Keluar")
    print("Untuk keluar aplikasi dalam stage apapun, mohon tekan CTRL + C")
    print()
    possibilities = [1, 2, 3, 4]
    try:
        while True:
            try:
                selection = int(input("Pilihan: "))
                if selection in possibilities:
                    return selection
                else:
                    raise ValueError("Mohon pilih nomor 1 atau 2.")
            except ValueError:
                print("Mohon pilih nomor 1 atau 2.")
    except KeyboardInterrupt:
        print("\nExiting application..."); sleep(2); exit()
    
if __name__ == '__main__':
    main()