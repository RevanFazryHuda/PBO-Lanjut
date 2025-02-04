import math

class Tabung():
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
        volume = math.pi * (self.__jari_jari ** 2) * self.__tinggi
        return volume

    def LuasPermukaan(self):
        luas_permukaan = 2 * math.pi * self.__jari_jari * (self.__jari_jari + self.__tinggi)
        return luas_permukaan

try:
    jari_jari = float(input("Masukkan Jari-jari Tabung\t:"))
    if(jari_jari <= 0):
        raise ValueError('nilai tidak boleh kurang dari atau sama dengan 0')

    tinggi = float(input("Masukkan Tinggi Tabung\t\t:"))
    if(tinggi <= 0):
        raise ValueError('nilai tidak boleh kurang dari atau sama dengan 0')

except ValueError as e:
    print(e)

else:
    T = Tabung(jari_jari, tinggi)
    print('Jari-jari\t:', T.cariJariJari())
    print('Tinggi\t\t:', T.cariTinggi())
    print('Volume\t\t:', T.Volume())
    print('Luas Permukaan\t:', T.LuasPermukaan())
