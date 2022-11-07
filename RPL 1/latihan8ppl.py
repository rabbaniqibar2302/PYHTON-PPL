# Contoh overloading
# Mendefinisikan atau memfungsikan operator sesuai kemauan kita (+)

# membuat class angka
class angka:
    def __init__(self, angka):
        self.angka = angka

    def __add__(self, objek):
        return angka(
            self.angka + objek.angka
        )


# membuat objek
x1 = angka(10)
x2 = angka(20)
x3 = x1 + x2 
print(x3.angka)
