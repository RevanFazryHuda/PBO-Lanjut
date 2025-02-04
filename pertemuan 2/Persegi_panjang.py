panjang = float(input("Masukkan panjang: "))
lebar = float(input("Masukkan lebar: "))

def hitung_luas_persegi_panjang(panjang, lebar):
    try:
        if panjang <= 0 or lebar <= 0:
            raise ValueError("Panjang dan lebar harus lebih dari 0")
        luas = panjang * lebar
        return luas
    except ValueError :
        print('Nilai yang dimasukkan salah')
        
print("Luas persegi panjang:", hitung_luas_persegi_panjang(panjang, lebar))