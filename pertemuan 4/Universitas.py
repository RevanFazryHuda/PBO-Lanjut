class Person:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    def info(self):
        return f"Nama: {self.nama}, Umur: {self.umur}"


class Dosen(Person):
    def __init__(self, nama, umur, bidang):
        super().__init__(nama, umur)
        self.bidang = bidang

    def info(self):
        return f"Dosen - {super().info()}, Bidang: {self.bidang}"


class Mahasiswa(Person):
    def __init__(self, nama, umur, jurusan):
        super().__init__(nama, umur)
        self.jurusan = jurusan

    def info(self):
        return f"Mahasiswa - {super().info()}, Jurusan: {self.jurusan}"


class Staff(Person):
    def __init__(self, nama, umur, departemen):
        super().__init__(nama, umur)
        self.departemen = departemen

    def info(self):
        return f"Staff - {super().info()}, Departemen: {self.departemen}"


class Satpam(Person):
    def __init__(self, nama, umur, lokasi):
        super().__init__(nama, umur)
        self.lokasi = lokasi

    def info(self):
        return f"Satpam - {super().info()}, Lokasi: {self.lokasi}"


class OB(Person):
    def __init__(self, nama, umur, tugas):
        super().__init__(nama, umur)
        self.tugas = tugas

    def info(self):
        return f"OB - {super().info()}, Tugas: {self.tugas}"


# Contoh penggunaan:
dosen1 = Dosen("Dr. Ahmad", 45, "Fisika")
mahasiswa1 = Mahasiswa("Budi", 20, "Teknik Informatika")
staff1 = Staff("Ani", 35, "Human Resource")
satpam1 = Satpam("Joko", 50, "Gedung Utama")
ob1 = OB("Susi", 25, "Membantu kebutuhan kantor")

print(dosen1.info())
print(mahasiswa1.info())
print(staff1.info())
print(satpam1.info())
print(ob1.info())
