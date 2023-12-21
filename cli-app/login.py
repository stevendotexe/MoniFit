from datetime import date
from time import sleep
import os
import csv

def main():
    while True:
        try:
            selection = int(input("Pilih mode: \n1. Registrasi\n2. Login\nPilihan (Ctrl+C untuk keluar): "))
        except ValueError:
            print("Mohon pilih nomor antara 1 atau 2.")
        if selection == 1:
            register()
            break
        elif selection == 2:
            login()
            break
        else:
            pass

def login():
    usernames = [user.rstrip('.csv') for user in os.listdir("userinfo")]
    while True:
        username = input("Username: ")
        if username in usernames:
            with open(f'userinfo/{username}/userdata.csv', 'r') as file:
                data = csv.reader(file)
                data = list(data)[0]  # ubah csv jadi list
            print(data)

            while True:
                pwinput = input("Password: ")
                if pwinput == data[1]:  # validasi password
                    print("Logging in...")
                    sleep(1)
                    return username
                else:
                    while True:
                        try:
                            selection = int(input("Password salah.\n1. Coba lagi\n2. Keluar dan registrasi\n\n Pilihan: "))
                            if selection == 1:
                                break
                            elif selection == 2:
                                exit()
                            else:
                                raise ValueError
                        except ValueError:
                            print("Mohon pilih antara 1 dan 2.")

        else:
            print(f"Username dengan nama {username} tidak ditemukan. Apakah anda ingin keluar dan registrasi?")
            while True:
                try:
                    selection = int(input("1. Coba lagi\n2. Keluar dan registrasi\nPilihan: "))
                    if selection == 1:
                        break
                    elif selection == 2:
                        exit()
                    else:
                        raise ValueError
                except ValueError:
                    print("Mohon pilih antara 1 dan 2.")

def register():
    email = input("Masukkan email: ")
    usernames = [user.rstrip('.csv') for user in os.listdir("userinfo")]
    print(usernames)

    while True:
        username = input("Masukkan username: ")
        if username in usernames or not username.isalnum():
            print(f"Username dengan nama {username} sudah ada atau tidak alfanumerik.")
        else:
            while True:
                password = input("Masukkan password: ")
                if len(password) >= 8:
                    print("Sedang me-register akun....")
                    sleep(1)
                    print("Registrasi sukses!")
                    new_user(username, email, password)
                    return username
                else:
                    print("Password harus lebih dari 8 karakter.")


def new_user(username, email, password):
    day = date.today()

    print("Selamat datang di MoniFit! Agar data kami sesuai dengan perhitungan, mohon masukkan data-data.")
    while True:
        try:
            age = int(input("Masukkan umur anda: "))
            weight = int(input("Masukkan berat badan anda (dalam kg): "))
            height = int(input("Masukkan tinggi badan anda (dalam cm): "))
            break
        except ValueError:
            print("Mohon masukkan nilai bulat (seperti 50, 176)")
    while True:
        gender = input("Mohon masukkan seks biologis (L/P): ").lower()
        if gender == 'l':
            gender = 'l'
            print()
            break
        elif gender == 'p':
            gender = 'p'
            print()
            break
        else:
            print("Mohon masukkan antara 'L' atau 'P'.")

    print("Level Aktivitas: ")
    print("_____________________________________")
    print("| 1 | Sedikit atau tidak olahraga")
    print("| 2 | 1 - 3 kali per minggu")
    print("| 3 | 4 - 5 kali per minggu")
    print("| 4 | Setiap hari | ATAU | Olahraga intens 3 - 4 kali per minggu")
    print("| 5 | Olahraga intens 6 - 7 kali per minggu")
    print("| 6 | Olahraga intens setiap hari atau pekerjaan fisik")
    print("_____________________________________")
    print("| Olahraga = 15 - 30 menit aktivitas jantung yang naik")
    print("| Olahraga intens = 45 - 120 menit aktivitas jantung yang naik")
    print("| Olahraga sangat intens = 45 - 120 menit aktivitas jantung yang naik")
    print("_____________________________________")
    possibilities = {'1': 1.2, '2': 1.375, '3': 1.55, '4': 1.55, '5': 1.725, '6': 1.9}

    while True:
        activity = input("Pilihan: ") # set the activity level to the appropriate level
        if activity in possibilities:
            activity_level = possibilities[activity]
            break
        else:
            print("Mohon pilih antara 1, 2, 3, 4, 5, atau 6.")

    os.mkdir(f'userinfo/{username}')
    with open(f'userinfo/{username}/userdata.csv', 'w', newline='') as file:
        file.write(f"{username},{password},{email},{day},{weight},{height},{gender},{age},{activity_level}")

    with open(f'userinfo/{username}/weight_history.csv', 'w', newline='') as file:
        file.write(f"{day},{weight}")

    sleep(.3)
    print("Menyimpan data...")
    sleep(1)
    print("Data telah tersimpan! Sedang login...")
    sleep(1)


if __name__ == '__main__':
        try:
            main()
        except KeyboardInterrupt:
            print("\nExiting application...")
            sleep(.3)
            exit()
