import csv
import os
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

# print("Nama-nama vendor: ")
# for index, vendor in enumerate(vendor_names()):
#     print(f"{index + 1}. {vendor}")

# vendor_name = 'DAPUR QUEEN'
# print(figlet_render(vendor_name))
# print(tabulate(vendor_foods(vendor_name), headers='keys', tablefmt='pretty'))
