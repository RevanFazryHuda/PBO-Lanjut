print('\nKonversi Suhu Celcius')
print('='*20,'\n')

class Celcius:
    def __init__(self,suhu):
        self.suhu = suhu
        
    def celcius(self):
        celcius = self.suhu
        return celcius
                
    def cari_fahrenheit(self):
        fahrenheit = (9/5 * self.suhu) + 32
        return fahrenheit

    def cari_reamur(self):
        reamur = (4/5 * self.suhu)
        return reamur

    def cari_kelvin(self):
        kelvin = (self.suhu) + 273.15
        return kelvin

suhu = float(input('Masukkan suhu dalam celcius: '))
C = Celcius(suhu)
value = C.celcius()

F = C.cari_fahrenheit()
R = C.cari_reamur()
K = C.cari_kelvin()

print(f'Suhu dalam Celcuis = {suhu}° Celcius')
print(f'suhu dalam Farenheit = {F}° Farenheit')
print(f'suhu dalam Reamur = {R}° Reamus')
print(f'suhu dalam Kelvin = {K}° Kelvin')