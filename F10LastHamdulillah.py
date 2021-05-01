# ============================ F10 ========================================
def mintaConsumable():
    # Meminta consumable yang tersedia pada database
    
    # input/output ->   consumable : array of array of string and integer
    #                   inventory_user : array of array of string and integer
    #                   consumable_history : array of array of string and integer
    
    # I.S. matriks data consumable, inventory_user, dan consumable_history terdefinisi
    # F.S. consumable terpinjam dan data consumable, inventory_user, consumable_history telah diubah
    
    # KAMUS LOKAL
    # ID, date_string, id_history : string
    # kondisinya, ketemu, syrt : boolean
    # indeks, amount_asked : integer

    # ALGORITMA    
    # Validasi ID ada
    kondisinya = True
    while kondisinya:
        try:
            ID = input("Masukkan ID item: ")
            ketemu = False

            for j in range(1, len(consumable)):
                if consumable[j][0] == ID:
                    ketemu = True
                    kondisinya = False
                    indeks = j
                    break
            if ketemu == False:
                print("ID item tidak tersedia, mohon inputkan ID yang benar")
        except ValueError:
            print()
    
    # Validasi jumlah
    syrt = True
    while syrt:
        try:
            amount_asked = int(input("Jumlah: "))
            if amount_asked > 0 and amount_asked <= consumable[indeks][3]:
                syrt = False
            if syrt == True:
                print(f"Silahkan masukan jumlah dengan benar, minimal 1 dan maksimal {consumable[indeks][3]}")
        except ValueError:
            print("Masukan jumlah dengan benar dengan bilangan bulat")

    # Validasi tanggal
    format = "%d/%m/%Y"
    
    while(True):
        date_string = input("Tanggal permintaan: ").strip()
        
        try:
            datetime.datetime.strptime(date_string, format)
            break
        except ValueError:
            print("Tanggal yang anda masukan salah. Silahkan masukan kembali tanggal dengan format DD/MM/YYYY")
            print()
    
    # Mengubah data terbaru
    id_history = 'CH' + str(len(consumable_history))
    consumable_history.append([id_history, idUser, ID, date_string, amount_asked])

    consumable [indeks][3] = consumable[indeks][3] - amount_asked

    pernah = False
    for al in range(len(inventory_user)):
        if ID == inventory_user[al][1] and idUser == inventory_user[al][0]:
            pernah = True
            final_indeks = al
            break

    if pernah:
        inventory_user[final_indeks][2] = inventory_user[final_indeks][2] + amount_asked
    else: # belum pernah
        inventory_user.append([id_user, ID, amount_asked])
    
    # Menampilkan ke user bahwa item berhasil diminta
    print()
    print(f"Item {consumable[indeks][1]} (x{amount_asked}) telah berhasil diambil!")