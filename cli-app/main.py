from figletrender import figlet_render
from time import sleep
import login
import pandas as pd # prep for pandas implementation
import csv
from tabulate import tabulate
import perhitungan as calc
import os


def main():
    username = user_login()
    user = f'userinfo/{username}/userdata.csv'
    print(figlet_render("MoniFit", font='nancyj'))
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

    selection = mainmenu(username, height, weight, gender, age, activity_level) # display main menu


def mainmenu(username, height, weight, gender, age, activity_level):
    print("1. Cek BMR (kalori), BMI, RDA Protein, RDA Lemak, RDA Karbohidrat")
    print("2. Lihat Rekomendasi Makanan (WIP)")
    print("3. Ubah data user (WIP)")
    print("4. Lihat restoran di sekitar")
    possibilities = [1, 2, 3, 4]
    while True:
        try:
            selection = int(input("Pilihan: "))
            if selection in possibilities:
                if selection == 1: bmrbmirda(username, height, weight, gender, age, activity_level)
                elif selection == 2: print("Work in progress.")
                elif selection == 3: print("Work in progress.")
                else: print("Work in progress.")
            else:
                raise ValueError
        except ValueError:
            print("Mohon pilih nomor 1, 2, 3, atau 4.")
        
def select_food(vendor): # to be completed
    data = []
    with open(vendor) as file:
        readfile = csv.DictReader(file)
        for row in readfile:
            data.append(row)
    
    return tabulate(data, headers="keys", tablefmt='grid')

def bmrbmirda(username, height, weight, gender, age, activity_level): # done
    
    calories = calc.bmr(gender, weight, height, age, activity_level)
    bmi = calc.bmi(weight, height)
    carbsRDA, fatRDA, proteinRDA = calc.rda(gender, weight, height, age, activity_level)

    print(username)
    user_data = [
        {'Calories': calories, 'Body Mass Index': f'{bmi:.2f}kg/m²', 'Carbohydrates RDA': carbsRDA, 'Fat RDA': fatRDA, 'Protein RDA': proteinRDA}
    ]

    print(tabulate(user_data, headers='keys', tablefmt='grid'))

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
                raise ValueError("Mohon pilih nomor 1 atau 2.")
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