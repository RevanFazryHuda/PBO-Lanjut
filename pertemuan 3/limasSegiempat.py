class LimasSegiEmpat():
    def __init__(self, panjang_alas, lebar_alas, tinggi):
        self.__panjang_alas = 0  # Private Method
        self.__lebar_alas = 0  # Private Method
        self.__tinggi = 0  # Private Method
        self.__setPanjangAlas(panjang_alas)
        self.__setLebarAlas(lebar_alas)
        self.__setTinggi(tinggi)

    def cariPanjangAlas(self):
        return self.__panjang_alas

    def cariLebarAlas(self):
        return self.__lebar_alas

    def cariTinggi(self):
        return self.__tinggi

    def __setPanjangAlas(self, nilai):
        self.__panjang_alas = nilai

    def __setLebarAlas(self, nilai):
        self.__lebar_alas = nilai

    def __setTinggi(self, nilai):
        self.__tinggi = nilai

    def Volume(self):
        volume = (1/3) * self.__panjang_alas * self.__lebar_alas * self.__tinggi
        return volume

    def LuasPermukaan(self):
        luas_permukaan = (0.5 * self.__panjang_alas * self.__lebar_alas) + \
                         (2 * self.__panjang_alas * self.__tinggi) + \
                         (2 * self.__lebar_alas * self.__tinggi)
        return luas_permukaan

try:
    panjang_alas = float(input("Masukkan Panjang Alas Limas Segiempat\t:"))
    if panjang_alas <= 0:
        raise ValueError('Panjang alas tidak boleh kurang dari atau sama dengan 0')

    lebar_alas = float(input("Masukkan Lebar Alas Limas Segiempat\t:"))
    if lebar_alas <= 0:
        raise ValueError('Lebar alas tidak boleh kurang dari atau sama dengan 0')

    tinggi = float(input("Masukkan Tinggi Limas Segiempat\t\t:"))
    if tinggi <= 0:
        raise ValueError('Tinggi tidak boleh kurang dari atau sama dengan 0')

except ValueError as e:
    print(e)

else:
    LS = LimasSegiEmpat(panjang_alas, lebar_alas, tinggi)
    print('Panjang Alas\t:', LS.cariPanjangAlas())
    print('Lebar Alas\t:', LS.cariLebarAlas())
    print('Tinggi\t\t:', LS.cariTinggi())
    print('Volume\t\t:', LS.Volume())
    print('Luas Permukaan\t:', LS.LuasPermukaan())
