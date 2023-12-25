from figletrender import figlet_render
from time import sleep
from datetime import date
from cool import coolStuff
import login
import rekomendasiMakanan as rec
import csv
from tabulate import tabulate
import perhitungan as calc
import os
import vendorselection as vsel


def main():
    username = user_login()
    user = f'userinfo/{username}/userdata.csv'
    coolStuff(); sleep(0.5)
    print(figlet_render("MoniFit", font='nancyj'))
    sleep(1)
    print(figlet_render(f"Selamat datang,  {username}", 'mini'))

    with open(user) as user: # hold user data here
        data = csv.reader(user)
        for row in data:
            username = row[0]
            weight = int(row[4])
            height = int(row[5])
            gender = row[6]
            age = int(row[7])
            activity_level = float(row[8])


        # print(f"Username: {username} | Weight: {weight} | Height: {height} | Gender: {gender.upper()} | Activity Level: {activity_level}")

    mainmenu(username, height, weight, gender, age, activity_level) # display main menu

def mainmenu(username, height, weight, gender, age, activity_level):
   
    while True:
        print("1. Cek BMR (kalori), BMI, RDA Protein, RDA Lemak, RDA Karbohidrat")
        print("2. Lihat Rekomendasi Makanan (WIP)")
        print("3. Ubah data user")
        print("4. Lihat restoran di sekitar")
        print("5. Tambah sejarah berat hari ini")
        possibilities = [1, 2, 3, 4, 5]
        try:
            selection = int(input("Pilihan: "))
            if selection in possibilities:
                if selection == 1: bmrbmirda(username, height, weight, gender, age, activity_level)
                elif selection == 2: food_reccomendation(username)
                elif selection == 3: login.change_data(username)
                elif selection == 4: vendor_selection()
                else: add_weight(username)
            else:
                raise ValueError
        except ValueError:
            print("Mohon pilih nomor 1, 2, 3, 4, dan 5.")

def bmrbmirda(username, height, weight, gender, age, activity_level): # done
    
    calories = calc.bmr(gender, weight, height, age, activity_level)
    bmi = calc.bmi(weight, height)
    carbsRDA, fatRDA, proteinRDA = calc.rda(gender, weight, height, age, activity_level)

    print("Perhitungan untuk", username)
    user_data = [
        {'Calories': calories, 'Body Mass Index': f'{bmi:.2f}kg/m²', 'Carbohydrates RDA': carbsRDA, 'Fat RDA': fatRDA, 'Protein RDA': proteinRDA}
    ]

    print(tabulate(user_data, headers='keys', tablefmt='grid'))

def vendor_selection():
    print("Nama-nama vendor: ")
    for index, vendor in enumerate(vsel.vendor_names()):
        if not vendor == 'Semua Vendor':
            print(f"{index + 1}. {vendor}")
    print("Lihat Semua Vendor - (ketik 'A')")

    while True:
        vendor_select = input("Pilih nama vendor: ")
        if vendor_select == 'Semua Vendor':
            pass
        else:
            vendor_name = vsel.vendor_foods(vendor_select)
            if vendor_name == -1: 
                print("Vendor dengan nama", vendor_select, "tidak ditemukan.")
            else: 
                break

    print(tabulate(vendor_name, headers='keys', tablefmt='pretty'))

def add_weight(username):
    while True:
        try:    
            new_weight = int(input("Masukkan berat hari ini: "))
            break
        except ValueError:
            print("Berat harus nomor. Coba lagi.")

    today_date = f"{date.today()}"

    try:
        with open(f'userinfo/{username}/weight_history.csv') as file:

            reader = csv.reader(file)

            last_weight_addition = None

            for row in reader:
                last_weight_addition = row[0]
            
            if last_weight_addition.strip() == today_date:
                raise SystemError
                      
        with open(f'userinfo/{username}/weight_history.csv', 'a') as file:
            file.write(f"\n{today_date},{new_weight}")

        # update user info
        userinfo = []
        with open(f'userinfo/{username}/userdata.csv') as file:
            reader = csv.reader(file)
            for row in reader:
                userinfo.append(row)
        userinfo[0][4] = new_weight
        
        with open(f'userinfo/{username}/userdata.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            for row in userinfo:
                writer.writerow(row)
        print("Berat berhasil ditambahkan.")
    except SystemError: sleep(1); print("Berat badan untuk hari ini sudah ditambahkan. Coba lagi besok."); sleep(2); 
    i = 3; 
    while i > 0:
        print(f"Kembali ke menu utama dalam {i}"); sleep(1)
        i -= 1

def food_reccomendation(username):
    print("Generating food recommendations....")
    sleep(1)
    todays_date = date.today()
    food_list, food_rec = rec.rekomendasiMakanan()
    food_rec.to_csv(f"userinfo/{username}/{todays_date}-foodrec")
    print(food_rec)

    while True:
        try:
            selection = int(input("1. Ubah makananan\n2. Lanjut\nPilihan: "))
            if selection < 1 or selection > 2:
                raise ValueError
            else: break
        except ValueError:
            print("Mohon pilih antara 1, atau 2.")
    
    if selection == 1:
        sel = [1, 2, 3]
        try:
            selection = int(input("Ubah makanan 1, 2, atau 3? "))
            if selection not in sel:
                raise ValueError
        except ValueError:
            print("Mohon pilih antara 1, 2, atau 3.")
    else: pass

    if selection == 1:
        print(food_list)

def user_login(): # lupa_password to be completed
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
        sleep(0.5); print("Exiting application..."); sleep(1); exit()

def user_selection(): # main menu login
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
                raise ValueError("Mohon pilih nomor 1, 2, 3, dan 4.")
        except ValueError:
            print("Mohon pilih nomor 1 atau 2.")

if __name__ == '__main__':
    while True:
        try:
            main()
        except KeyboardInterrupt:
            s = (input("\nExit application? (Y/N): ").lower())
            if s == 'y' or s == 'yes':
                print("\nExiting application..."); sleep(.1); exit()
            else:
                pass