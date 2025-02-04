alas = float(input("Masukkan alas segitiga: "))
tinggi = float(input("Masukkan tinggi segitiga: "))
def hitung_luas_segitiga(alas, tinggi):
    try:
        if alas <= 0 or tinggi <= 0:
            raise ValueError("Alas dan tinggi segitiga harus lebih dari 0")
        luas = 0.5 * alas * tinggi
        return luas
    except ValueError:
        print('Nilai yang dimasukkan salah')

print("Luas segitiga:", hitung_luas_segitiga(alas, tinggi))
