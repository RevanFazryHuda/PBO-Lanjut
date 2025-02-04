import math

radius = float(input("Masukkan jari-jari tabung: "))
tinggi = float(input("Masukkan tinggi tabung: "))
def hitung_luas_lingkaran(radius,tinggi):
    try:
        if radius <= 0 or tinggi <= 0:
            raise ValueError("Jari-jari lingkaran harus lebih dari 0")
        luas = math.pi * radius ** 2 * tinggi
        return luas
    except ValueError:
        print('Nilai yang dimasukkan salah')

print("Luas lingkaran:", hitung_luas_lingkaran(radius,tinggi))
