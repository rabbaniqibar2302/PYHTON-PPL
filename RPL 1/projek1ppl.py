# SELAMAT DATANG DI JPHOTEL
print("--Selamat Datang DI JPHOTEL--")
print("--NO----TIPE--------HARGA--")
print("--01----Suite---1.000.000--")
print("--02----Royal-----500.000--")
print("--03----BPJS------250.000--")

# Sampe Resepsionis (input data)
cust = input("Masukan nama lengkap : ")
tipe = int(input("Tipe Kamar : "))
lama_inap = int(input("Masukan lama inap : "))

# struk JPHOTEL
print("Pelanggan atas nama : ", cust)
# tipe kamar
if tipe == 1:
    print("Tipe kamar yang dipilih Suite")
elif tipe == 2:
    print("Tipe kamar yang dipilih Royal")
elif tipe == 3:
    print("Tipe kamar yang dipilih BPJS")
print("Lama menginap : ", lama_inap)
