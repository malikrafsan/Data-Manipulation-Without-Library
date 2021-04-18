def ubahjumlah():
    id_item = input("Masukan ID: ")
    change = int(input("Masukkan Jumlah: "))
    found = False
    indeks_found = None
    
    if id_item[0] == 'G':
        for i in range(1, len(gadget)):
            if gadget[i][0] == id_item:
                found = True
                indeks_found = i
            if found == True:
                break
    
        if indeks_found == None:
            print("Tidak ada item dengan ID tersebut!")
        else: # indeks_found ada
            before = gadget[indeks_found][3]
        
            if before + change < 0:
                print(f"{change} {gadget[indeks_found][1]} gagal dibuang karena stok kurang. Stok sekarang: {before} (< {change})")
            elif before + change >= 0:
                gadget[indeks_found][3] = gadget[indeks_found][3] + change
                if change >= 0:
                    print(f"{change} {gadget[indeks_found][1]} berhasil ditambahkan. Stok sekarang: {gadget[indeks_found][3]}")
                elif change < 0:
                    print(f"{abs(change)} {gadget[indeks_found][1]} berhasil dibuang. Stok sekarang: {gadget[indeks_found][3]}")

    elif id_item[0] == 'C':
        for i in range(1, len(consumable)):
            if consumable[i][0] == id_item:
                found = True
                indeks_found = i
            if found == True:
                break
    
        if indeks_found == None:
            print("Tidak ada item dengan ID tersebut!")
        else: # indeks_found ada
            before = consumable[indeks_found][3]
        
            if before + change < 0:
                print(f"{change} {consumable[indeks_found][1]} gagal dibuang karena stok kurang. Stok sekarang: {before} (< {change})")
            elif before + change >= 0:
                consumable[indeks_found][3] = consumable[indeks_found][3] + change
                if change >= 0:
                    print(f"{change} {consumable[indeks_found][1]} berhasil ditambahkan. Stok sekarang: {consumable[indeks_found][3]}")
                elif change < 0:
                    print(f"{abs(change)} {consumable[indeks_found][1]} berhasil dibuang. Stok sekarang: {consumable[indeks_found][3]}")
    
    else:
        print("Tidak ada item dengan ID tersebut!")