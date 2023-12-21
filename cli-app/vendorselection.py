import csv
import os
from tabulate import tabulate
from figletrender import figlet_render

def vendor_names():
    a = os.listdir("vendordata")
    vlist = []
    for i in a:
        if i.endswith('.csv'):
            vlist.append(i)
    vlist = [i.rstrip('.csv') for i in vlist]
    return vlist

def vendor_foods(vendorname):
    # Nama Makanan, Harga, Protein, Karbohidrat, Lemak, Kalori
    try:     
        with open(f'vendordata/{vendorname}.csv', 'r') as file:
            reader = csv.DictReader(file)
            data = [row for row in reader]
    except FileNotFoundError:
        print(f"Restoran dengan nama {vendorname} tidak ditemukan.")

    return data

vendor_name = 'DAPUR QUEEN'
print(figlet_render(vendor_name))
print(tabulate(vendor_foods(vendor_name), headers='keys', tablefmt='pretty'))