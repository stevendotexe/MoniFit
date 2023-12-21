from figletrender import figlet_render
from time import sleep
import login
import pandas as pd # prep for pandas implementation
import csv
import tabulate
import perhitungan as calc


def main():
    username = user_login()
    user = f'userinfo/{username}/userdata.csv'
    print(figlet_render("MoniFit", font='nancyj'))
    print(figlet_render(f"Selamat datang,  {username}", 'mini'))

    with open(user) as user: # hold user data here
        data = csv.reader(user)
        for row in data:
            username = row[0]
            weight = row[4]
            gender = row[5]
            activity_level = row[6]

    selection = mainmenu() # display main menu



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
        
def select_food(vendor): # to be completed
    data = []
    with open(vendor) as file:
        readfile = csv.DictReader(file)
        for row in readfile:
            data.append(row)
    
    return tabulate(data, headers="keys", tablefmt='grid')

def bmrbmirda(username, weight, gender, activity_level):
    # get user data: gender, weight, height, age, activity level
    pass

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

def mainmenu():
    print("1. Cek BMR (kalori), BMI, RDA Protein, RDA Lemak, RDA Karbohidrat")
    print("2. Lihat Rekomendasi Makanan (WIP)")
    print("3. Ubah data user (WIP)")
    print("4. Lihat restoran di sekitar")
    possibilities = [1, 2, 3]
    while True:
        try:
            selection = int(input("Pilihan: "))
            if selection in possibilities:
                return selection
            else:
                raise ValueError
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