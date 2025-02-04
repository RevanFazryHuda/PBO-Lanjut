import math

class Kerucut():
    def __init__(self, jari_jari, tinggi):
        self.__jari_jari = 0  # Private Method
        self.__tinggi = 0  # Private Method
        self.__setJariJari(jari_jari)
        self.__setTinggi(tinggi)

    def cariJariJari(self):
        return self.__jari_jari

    def cariTinggi(self):
        return self.__tinggi

    def __setJariJari(self, nilai):
        self.__jari_jari = nilai

    def __setTinggi(self, nilai):
        self.__tinggi = nilai

    def Volume(self):
        volume = (1/3) * math.pi * (self.__jari_jari ** 2) * self.__tinggi
        return volume

    def LuasPermukaan(self):
        garis_pelukis = math.sqrt((self.__jari_jari ** 2) + (self.__tinggi ** 2))
        luas_permukaan = math.pi * self.__jari_jari * (self.__jari_jari + garis_pelukis)
        return luas_permukaan

try:
    jari_jari = float(input("Masukkan Jari-jari Kerucut\t:"))
    if(jari_jari <= 0):
        raise ValueError('nilai tidak boleh kurang dari atau sama dengan 0')

    tinggi = float(input("Masukkan Tinggi Kerucut\t:"))
    if(tinggi <= 0):
        raise ValueError('nilai tidak boleh kurang dari atau sama dengan 0')

except ValueError as e:
    print(e)

else:
    K = Kerucut(jari_jari, tinggi)
    print('Jari-jari\t:', K.cariJariJari())
    print('Tinggi\t\t:', K.cariTinggi())
    print('Volume\t\t:', K.Volume())
    print('Luas Permukaan\t:', K.LuasPermukaan())
