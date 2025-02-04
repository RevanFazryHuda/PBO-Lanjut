class Person:
    def __init__(self, nama, jk):
        self.nama = nama
        self.jk = jk

    def info(self):
        return f"Nama: {self.nama}, Usia: {self.jk}"

class Dokter(Person):
    def __init__(self, nama, jk, spesialisasi):
        super().__init__(nama, jk)
        self.spesialisasi = spesialisasi

    def info(self):
        return f"{super().info()}, Spesialisasi: {self.spesialisasi}"

class Perawat(Person):
    def __init__(self, nama, jk, departemen):
        super().__init__(nama, jk)
        self.departemen = departemen

    def info(self):
        return f"{super().info()}, Departemen: {self.departemen}"

class Karyawan(Person):
    def __init__(self, nama, jk, jabatan):
        super().__init__(nama, jk)
        self.jabatan = jabatan

    def info(self):
        return f"{super().info()}, Jabatan: {self.jabatan}"

# Contoh penggunaan
dokter = Dokter("Dr. Garry", 'L', "Gigi")
perawat = Perawat("Nina", 'P', "ICU")
karyawan = Karyawan("Otong", 'L', "Human Resource")

print(dokter.info())
print(perawat.info())
print(karyawan.info())
