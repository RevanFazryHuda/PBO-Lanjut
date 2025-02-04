sisi = float(input("Masukkan panjang sisi kubus: "))

def hitung_volume_kubus(sisi):
    try:
        if sisi <= 0:
            raise ValueError("Sisi kubus harus lebih dari 0")
        volume = sisi ** 3
        return volume
    except ValueError:
        print('Nilai yang dimasukkan salah')

print("Volume kubus:", hitung_volume_kubus(sisi))
