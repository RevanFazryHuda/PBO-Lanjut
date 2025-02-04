class PrismaSegitiga():
    def __init__(self, alas, tinggi_segitiga, tinggi_prisma):
        self.__alas = 0  # Private Method
        self.__tinggi_segitiga = 0  # Private Method
        self.__tinggi_prisma = 0  # Private Method
        self.__setAlas(alas)
        self.__setTinggiSegitiga(tinggi_segitiga)
        self.__setTinggiPrisma(tinggi_prisma)

    def cariAlas(self):
        return self.__alas

    def cariTinggiSegitiga(self):
        return self.__tinggi_segitiga

    def cariTinggiPrisma(self):
        return self.__tinggi_prisma

    def __setAlas(self, nilai):
        self.__alas = nilai

    def __setTinggiSegitiga(self, nilai):
        self.__tinggi_segitiga = nilai

    def __setTinggiPrisma(self, nilai):
        self.__tinggi_prisma = nilai

    def Volume(self):
        volume = (1/2) * self.__alas * self.__tinggi_segitiga * self.__tinggi_prisma
        return volume

    def LuasPermukaan(self):
        luas_permukaan = (2 * (0.5 * self.__alas * self.__tinggi_segitiga)) + \
                         (self.__alas * self.__tinggi_prisma) + \
                         (3 * (0.5 * self.__alas * self.__tinggi_segitiga))
        return luas_permukaan

try:
    alas = float(input("Masukkan Alas Segitiga Prisma\t:"))
    if alas <= 0:
        raise ValueError('Alas segitiga tidak boleh kurang dari atau sama dengan 0')

    tinggi_segitiga = float(input("Masukkan Tinggi Segitiga Prisma\t:"))
    if tinggi_segitiga <= 0:
        raise ValueError('Tinggi segitiga tidak boleh kurang dari atau sama dengan 0')

    tinggi_prisma = float(input("Masukkan Tinggi Prisma\t\t:"))
    if tinggi_prisma <= 0:
        raise ValueError('Tinggi prisma tidak boleh kurang dari atau sama dengan 0')

except ValueError as e:
    print(e)

else:
    PS = PrismaSegitiga(alas, tinggi_segitiga, tinggi_prisma)
    print('Alas Segitiga\t:', PS.cariAlas())
    print('Tinggi Segitiga\t:', PS.cariTinggiSegitiga())
    print('Tinggi Prisma\t:', PS.cariTinggiPrisma())
    print('Volume\t\t:', PS.Volume())
    print('Luas Permukaan\t:', PS.LuasPermukaan())
