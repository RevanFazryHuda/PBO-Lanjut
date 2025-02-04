import math

class LimasSegitiga():
    def __init__(self, alas, tinggi_segitiga, tinggi_limas):
        self.__alas = 0  # Private Method
        self.__tinggi_segitiga = 0  # Private Method
        self.__tinggi_limas = 0  # Private Method
        self.__setAlas(alas)
        self.__setTinggiSegitiga(tinggi_segitiga)
        self.__setTinggiLimas(tinggi_limas)

    def cariAlas(self):
        return self.__alas

    def cariTinggiSegitiga(self):
        return self.__tinggi_segitiga

    def cariTinggiLimas(self):
        return self.__tinggi_limas

    def __setAlas(self, nilai):
        self.__alas = nilai

    def __setTinggiSegitiga(self, nilai):
        self.__tinggi_segitiga = nilai

    def __setTinggiLimas(self, nilai):
        self.__tinggi_limas = nilai

    def Volume(self):
        volume = (1/6) * self.__alas * self.__tinggi_segitiga * self.__tinggi_limas
        return volume

    def LuasPermukaan(self):
        luas_permukaan = (0.5 * self.__alas * self.__tinggi_segitiga) + \
                         (self.__alas * self.__tinggi_limas)
        return luas_permukaan

try:
    alas = float(input("Masukkan Alas Limas Segitiga\t:"))
    if(alas <= 0):
        raise ValueError('nilai alas tidak boleh kurang dari atau sama dengan 0')

    tinggi_segitiga = float(input("Masukkan Tinggi Segitiga Limas\t:"))
    if(tinggi_segitiga <= 0):
        raise ValueError('nilai tinggi segitiga tidak boleh kurang dari atau sama dengan 0')

    tinggi_limas = float(input("Masukkan Tinggi Limas\t\t:"))
    if(tinggi_limas <= 0):
        raise ValueError('nilai tinggi limas tidak boleh kurang dari atau sama dengan 0')

except ValueError as e:
    print(e)

else:
    LS = LimasSegitiga(alas, tinggi_segitiga, tinggi_limas)
    print('Alas\t\t:', LS.cariAlas())
    print('Tinggi Segitiga\t:', LS.cariTinggiSegitiga())
    print('Tinggi Limas\t:', LS.cariTinggiLimas())
    print('Volume\t\t:', LS.Volume())
    print('Luas Permukaan\t:', LS.LuasPermukaan())
