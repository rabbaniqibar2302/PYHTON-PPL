# buat rumus yang sama
# Mesin dan spion ada di dua kendaraan yang sama
class bagian1():
    def part1(mesin):
        mesin = print("mesin")

    def part2(spion):
        spion = print("spion")

# berikut bagian yang hanya didapat oleh masing masing kendaraan


class bagian2():
    def part_motor(roda):
        roda = print("roda dua")

    def part_mobil(roda):
        roda = print("roda empat")


obj = bagian1()
print("Bagian kendaraan mobil adalah"), obj.part1()
