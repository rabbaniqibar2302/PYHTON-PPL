# Perpus kosong untuk menyimpan buku
buku = []

#fungsi show buku ( perlihatkan buku )
def show_buku():
    if len(buku) <= 0:
        print ("Buku Kosong mas!")
    else:
        for indeks in range(len(buku)):
            print ("[{}]] {}".format (indeks,buku [indeks]))

#fungsi insert buku
def insert_buku():
    buku_baru = input("Judul Buku : ")
    buku.append(buku_baru)

# Menu untuk tampilan perpus
def show_menu():
    print("-Selamat datang di Perpus-")
    print("1. Show buku")
    print("2. Insert buku")
    print("3. Edit buku")
    print("4. Delete buku")
    print("5. Keluar")

    menu = int(input("Pilih Menu : > "))

    if menu == 1:
        show_buku()
    elif menu == 2:
        insert_buku()
    elif menu == 3:
        edit_buku()
    elif menu == 4:
        delete_buku()
    elif menu == 5:
        exit()
    else:
        print ("Upss Salaahh")

# tampilkan Menu
if __name__ == "__main__":
    while True:
        show_menu()
