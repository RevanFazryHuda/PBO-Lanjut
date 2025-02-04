class Balok():
    def __init__(self, panjang, lebar, tinggi):
        self.__panjang = 0  # Private Method
        self.__lebar = 0  # Private Method
        self.__tinggi = 0  # Private Method
        self.__setPanjang(panjang)
        self.__setLebar(lebar)
        self.__setTinggi(tinggi)

    def cariPanjang(self):
        return self.__panjang

    def cariLebar(self):
        return self.__lebar

    def cariTinggi(self):
        return self.__tinggi

    def __setPanjang(self, nilai):
        self.__panjang = nilai

    def __setLebar(self, nilai):
        self.__lebar = nilai

    def __setTinggi(self, nilai):
        self.__tinggi = nilai

    def Volume(self):
        volume = self.__panjang * self.__lebar * self.__tinggi
        return volume

    def LuasPermukaan(self):
        luas_permukaan = 2 * (self.__panjang * self.__lebar +
                              self.__panjang * self.__tinggi +
                              self.__lebar * self.__tinggi)
        return luas_permukaan

try:
    panjang = int(input("Masukkan Panjang Balok\t:"))
    if(panjang <= 0):
        raise ValueError('nilai tidak boleh kurang dari 1')
    lebar = int(input("Masukkan Lebar Balok\t:"))
    if(lebar <= 0):
        raise ValueError('nilai tidak boleh kurang dari 1')
    tinggi = int(input("Masukkan Tinggi Balok\t:"))
    if(tinggi <= 0):
        raise ValueError('nilai tidak boleh kurang dari 1')

except ValueError as e:
    print(e)

else:
    B = Balok(panjang, lebar, tinggi)
    print('Panjang\t:', B.cariPanjang())
    print('Lebar\t:', B.cariLebar())
    print('Tinggi\t:', B.cariTinggi())
    print('Volume\t:', B.Volume())
    print('Luas Permukaan:', B.LuasPermukaan())
