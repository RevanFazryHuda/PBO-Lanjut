class Person:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    def info(self):
        return f"Nama: {self.nama}, Umur: {self.umur}"


class Manager(Person):
    def __init__(self, nama, umur, departemen):
        super().__init__(nama, umur)
        self.departemen = departemen

    def info(self):
        return f"Manager - {super().info()}, Departemen: {self.departemen}"


class Programmer(Person):
    def __init__(self, nama, umur, bahasa):
        super().__init__(nama, umur)
        self.bahasa = bahasa

    def info(self):
        return f"Programmer - {super().info()}, Bahasa Pemrograman: {self.bahasa}"


class Teknisi(Person):
    def __init__(self, nama, umur, spesialisasi):
        super().__init__(nama, umur)
        self.spesialisasi = spesialisasi

    def info(self):
        return f"Teknisi - {super().info()}, Spesialisasi: {self.spesialisasi}"


class Staff(Person):
    def __init__(self, nama, umur, tugas):
        super().__init__(nama, umur)
        self.tugas = tugas

    def info(self):
        return f"Staff - {super().info()}, Tugas: {self.tugas}"


# Contoh penggunaan:
manager1 = Manager("Anies", 40, "Pemasaran")
programmer1 = Programmer("Prabowo", 30, "Python")
teknisi1 = Teknisi("Jokowi", 35, "Jaringan")
staff1 = Staff("Ganjar", 25, "Administrasi")

print(manager1.info())
print(programmer1.info())
print(teknisi1.info())
print(staff1.info())
