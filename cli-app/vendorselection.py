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


def food_search(target_food):

    # binary search data
    def binary_search(food_data, target):
        low, high = 0, len(food_data) - 1

        while low <= high:
            mid = (low + high) // 2
            current_food = food_data[mid]["Nama Makanan"].lower().strip()

            if current_food == target.lower().strip():
                return food_data[mid]
            elif current_food < target.lower().strip():
                low = mid + 1
            else:
                high = mid - 1

        return None

    # load data ke memori & sortir data
    def load_data(csv_file):
        with open(csv_file, newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            sorted_data = sorted(reader, key=lambda x: x["Nama Makanan"].lower().strip())
            return sorted_data

    food_data = load_data("vendordata/Semua Vendor.csv")
    result = binary_search(food_data, target_food)
    if not result == None:
        return [result]
    else:
        return None
