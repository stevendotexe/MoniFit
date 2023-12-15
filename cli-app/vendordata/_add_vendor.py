import csv
import os
from _figletrender import figlet_render

vendor_list = [vendor.strip('.csv') for vendor in os.listdir()]

def main():
    print(figlet_render("MoniFit"))
    print("1. Tambah vendor baru\n2. Tambah data makanan ke vendor\n3. Edit data vendor\n")
    possibilities = ['1', '2', '3']
    while True:
        selection = input("Pilihan: ")
        if selection in possibilities:
            if selection == '1':
                while True:
                    s = add_vendor()
                    if s == 0:
                        print("Vendor telah berhasil ditambahkan.")
                        break
                    else:
                        print("Vendor dengan nama tersebut sudah ada.")

            elif selection == '2':
                vendorname = input("Nama vendor: ")
                if vendorname in vendor_list:
                    add_food(vendorname)
                else:
                    print(f"Nama vendor {vendorname} tidak ditemukan. ")

            else:
                vendorname = input("Nama vendor: ")
                if vendorname in vendor_list:
                    edit_vendor(vendorname)
                else:
                    print(f"Nama vendor {vendorname} tidak ditemukan. ")


def add_vendor():
    vendor_name = input("Nama vendor baru: ")
    vendor_location = input("Lokasi vendor: ")
    if vendor_name not in vendor_list:
        with open(f"{vendor_name}.csv", 'w') as vendor:
            writer = csv.writer(vendor)
            writer.writerow([vendor_name, f"{vendor_location}"])
        return 0
    return 1
    

def add_food(vendor_name):
    nama_makanan = input("Nama makanan: ")
    protein = input("Protein makanan: ")
    fat = input("Lemak makanan: ")
    kalori = input("Kalori makanan: ")
    gula = input("Gula makanan: ")

    with open(f'{vendor_name}.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([nama_makanan, protein, kalori, fat, gula])

    print(f"Data makanan untuk vendor {vendor_name} berhasil ditambahkan.")


def edit_vendor(vendor_name):
    new_vendor_name = input("Enter the new vendor name: ")
    new_vendor_location = input("Enter the new vendor location: ")

    # read data vendor
    with open(f'{vendor_name}.csv', 'r') as file:
        reader = csv.reader(file)
        vendor_data = list(reader)

    # update data vendor
    vendor_data[0] = [new_vendor_name, new_vendor_location]

    # write kembali data baru
    with open(f'{vendor_name}.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerows(vendor_data)

    print(f"Nama dan data {vendor_name} berhasil diubah menjadi {new_vendor_name} yang berlokasi di {new_vendor_location}.")


if __name__ == '__main__':
    while True:
        try:
            main()
        except KeyboardInterrupt:
            s = (input("\nExit application? (Y/N): ").lower())
            if s == 'y' or s == 'yes':
                print("\nExiting application..."); exit()
            else:
                pass