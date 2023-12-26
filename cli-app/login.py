from datetime import date
from time import sleep
import os
import csv
from tabulate import tabulate

def main():
    while True:
        try:
            selection = int(input("Pilih mode: \n1. Registrasi\n2. Login\n3. Ubah data\nPilihan (Ctrl+C untuk keluar): "))
        except ValueError:
            print("Mohon pilih nomor antara 1 atau 2.")
        if selection == 1:
            register()
            break
        elif selection == 2:
            login()
            break
        elif selection == 3:
            change_data(input("Username: "))
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
                        raise ValueError # raise ValueError dan meminta user untuk memasukkan data kembali jika tidak input 1 atau 2
                except ValueError:
                    print("Mohon pilih antara 1 dan 2.")

def register():
    email = input("Masukkan email: ")
    usernames = [user.rstrip('.csv') for user in os.listdir("userinfo")]

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

def change_data(username):
    print("Mencari data user...")
    sleep(0.3)
    userdata = []
    try:
        with open(f'userinfo/{username}/userdata.csv') as file:
            reader = csv.reader(file)
            for row in reader:
                userdata.append(row)
    except FileNotFoundError:
        print("Username tidak ditemukan.")
        exit(1) # main.py seharusnya dapat menangkap username yang tidak ditemukan.
        
    userdata = userdata[0]

    userdict = [{ # dict agar bisa menggunakan tabulate()
    'Username'      : username,
    'Password'      : userdata[1],
    'Email'         : userdata[2],
    'Reg. Date'     : userdata[3],
    'Berat'         : userdata[4],
    'Tinggi'        : userdata[5],
    'Gender'        : userdata[6],
    'Umur'          : userdata[7],
    'L. Aktivitas'  : convert_activity_level(userdata[8], mode='reg')
    }]
    
    sleep(1)
    print(tabulate(userdict, headers='keys', tablefmt='grid'))

    while True:
        try:
            print("NB: Anda dapat mengubah berat dengan menambahkan sejarah berat.")
            selection = int(input("Apa yang ingin diubah?\n1. Password\n2. Email\n3. Tinggi\n4. Gender\n5. Umur\n6. L. Aktivitas\n7. Cancel\nPilihan: "))
            
            if not 0 < selection < 8:
                raise ValueError
            
            if selection == 1: # change password
                while True:
                    password_baru = input("Password baru: ")
                    if len(password_baru) < 8:
                        print("Mohon masukkan lebih dari 8 karakter untuk password.")
                    else:
                        break
                userdict[0]['Password'] = password_baru
            elif selection == 2: # change email
                userdict[0]['Email'] = input("Email baru: ")
            elif selection == 3: # change height
                while True:
                    try:
                        userdict[0]['Tinggi'] = int(input("Tinggi baru: "))
                        break
                    except ValueError:
                        print("Tinggi harus angka nilai bulat.")
            elif selection == 4: # change gender
                while True:
                    gender_baru = input("Gender baru: (L/P): ").lower()
                    print(gender_baru)
                    if gender_baru == 'p' or gender_baru == 'l':
                        userdict[0]['Gender'] = gender_baru 
                        break
                    else:
                        print("Mohon masukkan antara 'L' atau 'P'.")                      
            elif selection == 5: # change age
                while True:
                    try:
                        userdict[0]['Umur'] = int(input("Umur baru: "))
                        break
                    except ValueError:
                        print("Umur harus angka nilai bulat.")
            elif selection == 6: # change act. level
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
                        userdict[0]['L. Aktivitas'] = activity
                        break
                    else:
                        print("Mohon pilih antara 1, 2, 3, 4, 5, atau 6.")
            else:
                break
            
            print(tabulate(userdict, headers='keys', tablefmt='grid'))
            sel = input("Ubah data lain? (Y/N): ")
            if sel == 'N' or sel == 'n':
                print(tabulate(userdict, headers='keys', tablefmt='grid'))
                select = input("Konfirmasi Perubahan? (Y/N): ")
                if select == 'N' or select == 'n':
                    pass
                else:
                    with open(f'userinfo/{username}/userdata.csv', 'w') as file:
                        file.write(f"{userdict[0]['Username']},{userdict[0]['Password']},{userdict[0]['Email']},{userdict[0]['Reg. Date']},{userdict[0]['Berat']},{userdict[0]['Tinggi']},{userdict[0]['Gender']},{userdict[0]['Umur']},{convert_activity_level(userdict[0]['L. Aktivitas'], mode='rev')}")
                        print("Data telah diubah.")
                break
           
            else: # confirm data
                pass
        except ValueError:
            print("Mohon gunakan nomor 1 - 7.")

def convert_activity_level(level, mode='reg'): # convert level aktivitas untuk 'readability' user
    if mode == 'reg':
        levels = {'1.2': '1', '1.375': '2', '1.55': '3', '1.55': '4', '1.725': '5',  '1.9': '6'}
        return levels[level]
    elif mode == 'rev':
        levels = {'1': '1.2', '2': '1.375', '3': '1.55', '4': '1.55', '5': '1.725', '6': '1.9'}
        return levels[level]

if __name__ == '__main__':
        try:
            main()
        except KeyboardInterrupt:
            print("\nExiting application...")
            sleep(.3)
            exit()
