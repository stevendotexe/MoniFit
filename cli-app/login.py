
def register(): # Register user
    email = input("Masukkan email: ")

    while True:
        password = input("Masukkan password")
        if password >= 8:
            break
        else:
            print("Password harus lebih dari 8 karakter.")

    user_info[email] = password

def login(): # login user
    email = input("Masukkan email: ")
    while True:
        if email not in user_info:
            selection = (input("Email tidak ada dalam database. apakah anda ingin registrasi? (1 coba ulang, 2 lupa password, 3 registrasi)"))
            if selection
