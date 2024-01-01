import csv
import os
from tabulate import tabulate

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
        return -1

    return data

def vendor_search():
    vendor_data = []  # list vendor_data menyimpan data vendor ke memori
    with open('vendordata/Semua Vendor.csv') as file:
        reader = csv.DictReader(file)
        for row in reader:
            vendor_data.append(row)

    m = []
    for items in vendor_data:
        m.append(items['Nama Makanan'])

    return m

def binary_search(food_data, target):
    low, high = 0, len(food_data) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if food_data[mid] == target:
            return mid
        elif food_data[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    
    return -1  # item tidak ditemukan


    

vendordata = vendor_search()
print(vendordata)
# print(tabulate(vendordata, headers='keys', tablefmt='fancy_grid'))