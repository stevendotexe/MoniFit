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
    vendor_data = []
    # Nama Makanan, Harga, Protein, Karbohidrat, Lemak, Kalori
    with open(f'vendordata/{vendorname}.csv', 'r') as file:
        read = csv.DictReader(file)
        for row in read:
            vendor_data.append({'Nama Makanan': row['Nama Makanan'], 
                        'Harga': row['Harga'], 
                        'Protein': row['Protein'], 
                        'Karbohidrat': row['Karbohidrat'], 
                        'Lemak': row['Lemak'], 
                        'Kalori': row['Kalori']})
            
    return vendor_data