# ada 3 kategori enkapsulasi yaitu : Public, Protected, Private

#contoh class public 
class segitiga:
    def __init__(self , alas, tinggi):
        self.alas = alas
        self.tinggi = tinggi
        self.luas = 0.5 * alas * tinggi

#buat instansiasinya
# segitiga_besar = segitiga(100,80)
# print(f'alas : {segitiga_besar.alas}')
# print(f'tinggi : {segitiga_besar.tinggi}')
# print(f'luas : {segitiga_besar.luas}')

# contoh class protected 
class mobil:
    def __init__(self, merk):
        self._merk = merk

class mobilefwan(mobil):
    def __init__(self, merk, total_gear):
        super().__init__(merk)
        self._total_gear = total_gear

    # Akses _merk dari subclass (kelas turunan)
    def pamer(self):
        print(f'Mobil{self._merk} dengan total gear {self._total_gear}')

redbull = mobilefwan(' Redbull Racing',8)
redbull.pamer()

# sedan = mobil('Toyota')

# #tampilkan merk dari luar kelas
# print (f'Merk Mobil : {sedan._merk}')