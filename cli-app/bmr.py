def hitung_bmr(jenis_kelamin, berat_badan, tinggi_badan, usia, tingkat_aktivitas):
    if jenis_kelamin == 'L':
        bmr = ((10 * berat_badan) + (6.25 * tinggi_badan) - (5 * usia) - 161) * tingkat_aktivitas
    elif jenis_kelamin == 'P':
        bmr = ((10 * berat_badan) + (6.25 * tinggi_badan) - (5 * usia) + 5) * tingkat_aktivitas
    else:
        return None
    return bmr

jenis_kelamin = input("Jenis kelamin (L/P): ")
berat_badan = float(input("Berat badan (kg): "))
tinggi_badan = float(input("Tinggi badan (cm): "))
usia = int(input("Usia (tahun): "))
tingkat_aktivitas = (input("Tingkat aktivitas (1-5): "))

if tingkat_aktivitas == 1:
    tingkat_aktivitas = 1.2
elif tingkat_aktivitas == 2:
    tingkat_aktivitas = 1.375
elif tingkat_aktivitas == 3:
    tingkat_aktivitas = 1.55
elif tingkat_aktivitas == 4:
    tingkat_aktivitas = 1.725
elif tingkat_aktivitas == 5:
    tingkat_aktivitas = 1.9
else:
    print("Tingkat aktivitas tidak valid.")
    exit()

bmr = hitung_bmr(jenis_kelamin, berat_badan, tinggi_badan, usia, tingkat_aktivitas)

if bmr is None:
    print("Jenis kelamin tidak valid.")
else:
    print(f"BMR Kamu adalah {bmr:.2f} kalori per hari.")

