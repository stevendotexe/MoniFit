import login
from pyfiglet import Figlet

def main():
    selection = user_selection()

    if selection == 1:
        login.register()
    elif selection == 2:
        login.login()
    elif selection == 3:
        pass # LupaPassword to be completed
    else:
        print("")
        exit()

def figlet_render(text, font='doh'):
    fig = Figlet(font = font)
    return fig.renderText(text)

def user_selection():
    print("Selamat datang di\n"+figlet_render("MoniFit\n")+"Pilih opsi:")
    print("1. Registrasi")
    print("2. Login")
    print("3. Lupa password")
    print("4. Keluar")
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
    main()