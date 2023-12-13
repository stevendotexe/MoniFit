from datetime import date
from time import sleep
import os
import json


def main():
    while True:
        try:
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
            else: pass
        except KeyboardInterrupt:
            print("\nExiting application..."); sleep(2); exit()

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
                    print("Logging in...")
                    sleep(1)
                    return username
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
                    selection = int(input("1. Coba lagi\n2. Keluar dan registrasi\nPilihan: "))
                    if selection == 1:
                        break # break jika user mau mencoba memasukkan password lagi
                    elif selection == 2:
                        exit()
                    else:
                        raise ValueError
                except ValueError:
                    print("Mohon pilih antara 1 dan 2.")

# registrasi user baru
def register():
    email = input("Masukkan email: ")
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
                    print("Sedang me-register akun...."); sleep(1)
                    print("Registrasi sukses!")
                    new_user(username, email, password)   
                    return username
                else:
                    print("Password harus lebih dari 8 karakter.")
            
def new_user(username, email, password): # untuk memasukkan data user baru
    day = date.today()

    print("Selamat datang di MoniFit! Agar data kami sesuai dengan perhitungan, mohon masukkan data-data.")
    while True:
        try:
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
        else: print("Mohon masukkan antara 'L' atau 'P'.")

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
    possibilities = ['1', '2', '3', '4', '5', '6']
    while True:
        activity_level = input("Pilihan: ")
        if activity_level in possibilities:
            break
        else:
            print("Mohon pilih antara 1, 2, 3, 4, 5, atau 6.")
        
    with open(f'userinfo/{username}.json', 'w') as file:
        file.write("{\n")
        file.write(f'"username": "{username}",\n')
        file.write(f'"password": "{password}",\n')
        file.write(f'"email": "{email}",\n')
        file.write(f'"registration_date": "{day}",\n')
        file.write(f'"height": "{height}",\n')
        file.write(f'"gender": "{gender}",\n')
        file.write(f'"activity_level": "{activity_level}",\n')
        file.write('"weight_history": ' + '{'+f'"{day}":' +  f'{weight}' + '}\n')
        file.write("}\n")
        
if __name__ == '__main__':
    main()