def main():
    while True:
        try:
            berat_badan = float(input("Masukkan berat badan (kg): "))
            tinggi_badan = float(input("Masukkan tinggi badan (cm): "))
            usia = int(input("Masukkan usia: "))
            jenis_kelamin = input("Masukkan jenis kelamin (pria/wanita): ")
            tingkat_aktivitas = float(input("Masukkan tingkat aktivitas (1.2 untuk Tidak Aktif, 1.375 untuk sedikit, 1.55 untuk Cukup Aktif,1.725 untuk Aktif, 1.9 untuk Sangat Aktif): "))
            break
        except ValueError:
            print("Nilai harus berupa koma (cth. 1.912)")

    bmr = hitung_bmr(berat_badan, tinggi_badan, usia, jenis_kelamin, tingkat_aktivitas)
    rda_lemak = hitung_rda_lemak(bmr)

    print()
    print(f"BMR: {bmr:.2f} kalori per hari.")
    print(f"RDA Lemak: {rda_lemak:.2f} gram per hari.")

def hitung_bmr(w, h, a, g, al): 
    """
    w = weight
    h = height
    a = age
    g = gender
    al = activity level
    """
    if g.lower() == 'pria':
        bmr = ((10.0 * w) + (6.25 * h) + (5.0 * a) + 5.0) * al
    elif g.lower() == 'wanita':
        bmr = ((10.0 * w) + (6.25 * h) + (5.0 * a) - 161.0) * al
    else:
        return "Jenis kelamin tidak valid"
    return bmr

def hitung_rda_lemak(bmr):
    rda_lemak = (bmr * 0.25) / 9  
    return rda_lemak

if __name__ == '__main__':
    main()
