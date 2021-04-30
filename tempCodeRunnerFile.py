def cariRarity():
    # Mencari gadget yang memiliki rarity sesuai yang diinputkan
    
    # input -> gadget : array of array of string and integer
    
    # I.S. matriks data gadget terdefinisi
    # F.S. tercetak ke layar data gadget yang memiliki rarity sesuai yang diinputkan
    
    # KAMUS LOKAL
    # rarity : string
    # i : integer
    # ditemukan : boolean
    
    # Function / Procedure
    
    # ALGORITMA
    rarity = input("Masukkan rarity: ")
    print()
    print("Hasil pencarian: ")
    print()
    
    ditemukan = False
    for i in range(len(gadget)):
        if gadget[i][4] == rarity:
            print("Nama             :", gadget[i][1])
            print("Deskripsi        :", gadget[i][2])
            print("Jumlah           :", gadget[i][3])
            print("Rarity           :", gadget[i][4])
            print("Tahun ditemukan  :", gadget[i][5])
            print()
            ditemukan = True
    if not ditemukan:
        print("Tidak ada gadget yang memiliki rarity", rarity)