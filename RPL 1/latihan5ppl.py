#Buat 3 objek Orang , Pelajar , Pekerja
#Orang = Kelas Induk 
#Pelajar , Pekerja = Kelas Turunan

class Orang:
    def __init__(self, nama, asal):
        self.nama = nama
        self.asal = asal
    
    def perkenalan(self):
        print("Halo nama saya ",self.nama,"dari",self.asal)

class Pelajar(Orang):
    def __init__(self, nama, asal, sekolah):
        Orang.__init__(self, nama, asal)
        self.sekolah = sekolah

class Pekerja(Orang):
    def __init__(self, nama, asal, kantor):
        super().__init__(nama, asal)
        self.kantor = kantor
    
andi = Orang('Andi','Jakarta\n')
andi.perkenalan()

tito = Pelajar('Tito','Subang','SMKJP1')
tito.perkenalan()
print(f'Saya Sekolah di{tito.sekolah}\n')

cahyo = Pekerja('Cahyo','Bandung','SMKJP1')
cahyo.perkenalan()
print(f'Saya Kerja di{cahyo.kantor}')

