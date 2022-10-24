# Kelas induk = Kendaraan , Kelas turunan = Mobil
# Kendaraan mempunyai sifat berjalan(), Mobil mempunyai sifat berjalan() tapi lebih spesifik
from os import sep


class kendaraan:
    def berjalan(self):
        print('Berjalan')

class mobil(kendaraan):
    def berjalan(self, kecepatan, satuan = 'km/j'):
        print(f'Berjalan lebih ngebut {kecepatan} {satuan}')

#instansiasi (memanggil fungsi dan kelas)
sepeda = kendaraan()
sedan = mobil()

sepeda.berjalan()
sedan.berjalan(200)