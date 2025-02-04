class Kubus():
    def __init__(self, sisi):
        self.__sisi = 0  # Private Method
        self.__setSisi(sisi)

    def cariSisi(self):
        return self.__sisi

    def __setSisi(self, nilai):
        self.__sisi = nilai

    def Volume(self):
        volume = self.__sisi ** 3
        return volume

    def LuasPermukaan(self):
        luas_permukaan = 6 * (self.__sisi ** 2)
        return luas_permukaan

try:
    sisi = int(input("Masukkan Panjang Sisi Kubus\t:"))
    if(sisi <= 0):
        raise ValueError('nilai tidak boleh kurang dari 1')

except ValueError as e:
    print(e)

else:
    K = Kubus(sisi)
    print('Sisi\t:', K.cariSisi())
    print('Volume\t:', K.Volume())
    print('Luas Permukaan:', K.LuasPermukaan())
