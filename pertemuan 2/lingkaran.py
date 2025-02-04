import math

radius = float(input("Masukkan jari-jari lingkaran: "))
def hitung_luas_lingkaran(radius):
    try:
        if radius <= 0:
            raise ValueError("Jari-jari lingkaran harus lebih dari 0")
        luas = math.pi * radius ** 2
        return luas
    except ValueError:
        print('Nilai yang dimasukkan salah')

print("Luas lingkaran:", hitung_luas_lingkaran(radius))
