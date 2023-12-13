def hitung_kalori(berat_badan, tinggi_badan, usia, jenis_kelamin, tingkat_aktivitas):
    tingkat_aktivitas_lower = tingkat_aktivitas.lower()
    faktor_aktivitas = 0  

    if tingkat_aktivitas_lower == "tidak aktif":
        faktor_aktivitas = 1.2
    elif tingkat_aktivitas_lower == "sedikit aktif":
        faktor_aktivitas = 1.375
    elif tingkat_aktivitas_lower == "cukup aktif":
        faktor_aktivitas = 1.55
    elif tingkat_aktivitas_lower == "aktif":
        faktor_aktivitas = 1.725
    elif tingkat_aktivitas_lower == "sangat aktif":
        faktor_aktivitas = 1.9
    else:
        print("Error: Tingkat aktivitas tidak valid. Pilih dari: 'Tidak Aktif', 'Sedikit Aktif', 'Cukup Aktif', 'Aktif', 'Sangat Aktif'.")
        return

    if jenis_kelamin.lower() == "pria":
        bmr = ((10.0 * berat_badan) + (6.25 * tinggi_badan) + (5.0 * usia) + 5.0) * faktor_aktivitas
    elif jenis_kelamin.lower() == "wanita":
        bmr = ((10.0 * berat_badan) + (6.25 * tinggi_badan) + (5.0 * usia) - 161.0) * faktor_aktivitas
    else:
        print("Error: Jenis kelamin harus 'pria' atau 'wanita'.")
        return

    

    kalori_harian = bmr * faktor_aktivitas
    print(f"\nKalori Harian (dengan tingkat aktivitas {tingkat_aktivitas}): {kalori_harian:.2f} kalori/hari")


berat_badan = float(input("Masukkan berat badan (kg): "))
tinggi_badan = float(input("Masukkan tinggi badan (cm): "))
usia = float(input("Masukkan usia: "))
jenis_kelamin = input("Masukkan jenis kelamin (pria/wanita): ")
tingkat_aktivitas = input("Masukkan tingkat aktivitas (Tidak Aktif/Sedikit Aktif/Cukup Aktif/Aktif/Sangat Aktif): ")

hitung_kalori(berat_badan, tinggi_badan, usia, jenis_kelamin, tingkat_aktivitas)

