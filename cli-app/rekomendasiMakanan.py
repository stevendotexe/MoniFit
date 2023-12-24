import pandas as pd
import random as rd

# read file csv
def rekomendasiMakanan():
  daftarMakanan = pd.read_csv("cli-app/vendordata/daftar_makanan.csv")

  makananRekomendasi = pd.DataFrame() # buat variable kosong yg menampung 3 makanan rekomen
  lst = [] # list kosong yg nanti akan dimasukkan ke dataframe
  nmr = [] # list nomor untuk mencegah duplikasi makanan rekomendasi

  for i in range(3):
    rand = rd.randint(daftarMakanan["No"].min(), daftarMakanan["No"].max())
    while rand in nmr:
      rand = rd.randint(daftarMakanan["No"].min(), daftarMakanan["No"].max()) # cegah duplikasi makanan
    nmr.append(rand)

    lst.append(daftarMakanan[daftarMakanan["No"] == rand]) # masukkan makanan ke lst
  makananRekomendasi = pd.concat(lst) # masukkan lst ke dalam makananRekomendasi

  print(makananRekomendasi)
  
