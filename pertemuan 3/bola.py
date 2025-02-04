import math

class Bola():
    def __init__(self, jari_jari):
        self.__jari_jari = 0  # Private Method
        self.__setJariJari(jari_jari)

    def cariJariJari(self):
        return self.__jari_jari

    def __setJariJari(self, nilai):
        self.__jari_jari = nilai

    def Volume(self):
        volume = (4/3) * math.pi * (self.__jari_jari ** 3)
        return volume

    def LuasPermukaan(self):
        luas_permukaan = 4 * math.pi * (self.__jari_jari ** 2)
        return luas_permukaan

try:
    jari_jari = float(input("Masukkan Jari-jari Bola\t:"))
    if(jari_jari <= 0):
        raise ValueError('nilai tidak boleh kurang dari atau sama dengan 0')

except ValueError as e:
    print(e)

else:
    B = Bola(jari_jari)
    print('Jari-jari\t:', B.cariJariJari())
    print('Volume\t\t:', B.Volume())
    print('Luas Permukaan\t:', B.LuasPermukaan())
