#soal ketiga "SALESMAN"

#input
hasil = int(input("Masukan hasil penjualan"))

if hasil >= 250000:
    uang_jasa = 15000
    komisi = hasil/20
elif hasil >= 500000:
    uang_jasa = 25000
    komisi = hasil/10
elif hasil >= 750000:
    uang_jasa = 35000
    komisi = hasil*(3/20)

