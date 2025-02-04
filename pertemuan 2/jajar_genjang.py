alas = float(input("Masukkan panjang alas jajar genjang: "))
tinggi = float(input("Masukkan tinggi jajar genjang: "))
def hitung_luas_jajar_genjang(alas, tinggi):
    try:
        if alas <= 0 or tinggi <= 0:
            raise ValueError("Alas dan tinggi jajar genjang harus lebih dari 0")
        luas = alas * tinggi
        return luas
    except ValueError:
        print('Nilai yang dimasukkan salah')

print("Luas jajar genjang:", hitung_luas_jajar_genjang(alas, tinggi))
