import login


def main():
    selection = user_selection()

    if selection == 1:
        login.register()
    elif selection == 2:
        login.login()


def user_selection():
    print("Selamat datang di MoniFit. Pilih opsi:")
    print("1. Registrasi")
    print("2. Login")
    print()
    
    while True:
        try:
            selection = int(input("Pilihan: "))
            if selection == 1 or selection == 2:
                return selection
            else:
                pass
        except ValueError:
            print("Mohon pilih nomor 1 atau 2.")
    
if __name__ == '__main__':
    main()