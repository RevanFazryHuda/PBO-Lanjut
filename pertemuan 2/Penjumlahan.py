A = int(input('Masukkan Sebuah Angka = '))
B = input('Masukkan Sebuah Angka = ')
try:
    C = A + B
except TypeError:
    print('Terjadi Error, pengoperasian tersebut tak bisa dieksekusi')