# F11 GAGAL

def cetakRiwayat(index,namaUser,namaGadget):
    print()
    print("ID Peminjam          : " + gadget_borrow_history[index][1])
    print("Nama Pengambil       : " + namaUser)
    print("Nama Gadget          : " + namaGadget)
    print("Tanggal Peminjamanan : " + gadget_borrow_history[index][3])
    print("Jumlah               : " + str(gadget_borrow_history[index][4]))

def riwayatPinjam(idUser):
    namaUser = user[cariID(user,idUser)][2]
    for i in range(len(gadget_borrow_history)):
        if gadget_borrow_history[i][1] == idUser:
            namaGadget = gadget[cariID(gadget,gadget_borrow_history[i][2])][1]
            cetakRiwayat(i,namaUser,namaGadget)

def mintaCon():
    ID = input("Masukkan ID item: ")
    while not IDItemAda(consumable, ID):
        print()
        print("ID item tidak tersedia, silakan inputkan kembali")
        ID = input("Masukkan ID item: ")
    jumlah = input("Jumlah: ")
    #while not jumlahValid(consumable,ID,jumlah):
        
def jumlahValid(data,ID,jumlahAmbil):
    if jumlahAmbil > 0:
        for i in range(len(data)):
            if data[i][0] == ID:
                if data[i][3] < jumlahAmbil:
                    return False
                else:
                    return True
    else:
        return False

# ============================ FB03 ========================================
def seed(seed):
    global random
    random = round(time.time())

def rand():
    a = 47071034
    c = 22206856
    m = 87635214759
    global random
    random = (a*random + c) % m
    return random

def chance(lstRarity,rarity):
    if rarity == 'C':
        lstRarity[0] += 90
        lstRarity[1] += 10
    elif rarity == 'B':
        lstRarity[0] += 10
        lstRarity[1] += 80
        lstRarity[2] += 10
    elif rarity == 'A':
        lstRarity[1] += 10
        lstRarity[2] += 80
        lstRarity[3] += 10
    else:
        lstRarity[2] += 10
        lstRarity[3] += 90
    sum = 0
    for i in range(4):
        sum += lstRarity[i]
    for i in range(4):
        lstRarity[i] = lstRarity[i] * 100 / sum

    return lstRarity

def printChance(chance,rarity):
    if chance != 0:
        return Bold(rarity) + " (" + Bold("{:.2f}".format(chance)) + "%) "
    else:
        return ""

def hasilGacha(lstChance):
    random = rand() % 100 # 0 - 99
    random += 1
    for i in range(4):
        random -= lstChance[i]
        if random <= 0:
            if i == 0:
                return 'C'
            elif  i == 1:
                return 'B'
            elif i == 2:
                return 'A'
            else:
                return 'S'

def gacha():
    global lstChance
    global consumable_history
    global consumable
    
    print()
    print("========INVENTORY========")
    count = 0
    IDInventory = []
    for i in range(len(consumable_history)):
        if consumable_history[i][1] == idUser:
            count += 1
            urutan = cariID(consumable,consumable_history[i][2])
            print(str(count) + ". " + consumable[urutan][1] + "(Rarity " + consumable[urutan][4] + ") (" + str(consumable_history[i][4]) + ")")
            IDInventory.append(consumable_history[i][2])
    if count == 0:
        print("Anda tidak mempunyai consumable di inventory Anda")
        print("=========================")
        print()
        return
    print("=========================")
    print()
    digunakan = int(input("Pilih consumable yang mau digunakan: "))
    if digunakan > count:
        print("Input anda tidak valid")
        return
    jumlah = int(input("Jumlah yang digunakan: "))
    urutan = cariID(consumable,IDInventory[digunakan - 1])
    if consumable[urutan][3] < jumlah:
        print("Jumlah consumable Anda tidak mencukupi")
    else:
        print(Bold(consumable[urutan][1]) + " (" + Bold("x" + str(jumlah)) + ") ditambahkan!")
        lstChance = chance(lstChance,consumable[urutan][4])
        consumable[urutan][3] += jumlah
        # Tanya kakaknya kalo digunakan gacha apakah hilang consumablenya
        consumable_history[cariData(consumable_history,IDInventory[digunakan-1],2)][4] -= jumlah
        print("Chance mendapatkan Rarity ", end='')
        if lstChance[0] != 0:
            print(Bold('C') + " (" + Bold("{:.2f}".format(lstChance[0])) + "%) ", end='')
        if lstChance[1] != 0:
            print(Bold('B') + " (" + Bold("{:.2f}".format(lstChance[1])) + "%) ", end='')
        if lstChance[2] != 0:
            print(Bold('A') + " (" + Bold("{:.2f}".format(lstChance[2])) + "%) ", end='')
        if lstChance[3] != 0:
            print(Bold('S') + " (" + Bold("{:.2f}".format(lstChance[3])) + "%)", end='')
        print()
        print()
        perintah = input("Tambahkan item lagi? (Y/N): ")
        
        if perintah == 'Y':
            gacha()
        else:
            print()
            print("Rolling...")
            time.sleep(3)
            print()
            rarity = hasilGacha(lstChance)        
            finished = False
            while not finished:
                for i in range(len(consumable)):
                    if consumable[i][4] == rarity:
                        print("Selamat Anda mendapatkan " + Bold(consumable[i][1]) + " (Rarity " + rarity + ") sebanyak x" + Bold(str(consumable[i][3])) + "!")
                        tambah_con_history = ["CH" + str(len(consumable_history)),idUser,consumable[i][0],datetime.date.today().strftime("%d/%m/%Y")]
                        consumable_history += tambah_con_history
                        lstChance = [0,0,0,0]
                        finished = True
                        return
                rarity = hasilGacha(lstChance)

# ============================ F16 ========================================
def help():
    print("""
============================================================ HELP ============================================================
Berikut merupakan keyword yang dapat digunakan beserta fungsi dan aksesnya
Ketikkan keyword di bawah ini untuk melakukan fungsi yang diinginkan

> \033[1mregister\033[0m       => melakukan registrasi user baru                                                  \033[91m(Akses: Admin)\033[0m
> \033[1mlogin\033[0m          => melakukan login ke dalam program                                                \033[91m(Akses: Admin/User)\033[0m
> \033[1mcaricarity\033[0m     => mencari gadget berdasarkan rarity yang diinputkan                               \033[91m(Akses: Admin/User)\033[0m
> \033[1mcaritahun\033[0m      => mencari gadget berdasarkan tahun ditemukan                                      \033[91m(Akses: Admin/User)\033[0m
> \033[1mtambahitem\033[0m     => menambahkan item (gadget/consumable) ke dalam database                          \033[91m(Akses: Admin)\033[0m
> \033[1mhapusitem\033[0m      => menghapus item (gadget/consumable) dari database                                \033[91m(Akses: Admin)\033[0m
> \033[1mubahjumlah\033[0m     => mengubah jumlah gadget/consumable pada database                                 \033[91m(Akses: Admin)\033[0m
> \033[1mpinjam\033[0m         => meminjam gadget dari database dan memasukkan ke dalam inventory                 \033[91m(Akses: User)\033[0m
> \033[1mkembalikan\033[0m     => mengembalikan gadget yang dipinjam                                              \033[91m(Akses: User)\033[0m
> \033[1mminta\033[0m          => meminta consumable dari database dan memasukkan ke dalam inventory              \033[91m(Akses: User)\033[0m
> \033[1mriwayatpinjam\033[0m  => melihat record peminjaman gadget yang tersortir berdasar tanggal                \033[91m(Akses: Admin)\033[0m
> \033[1mriwayatkembali\033[0m => melihat record pengembalian gadget yang tersortir berdasar tanggal              \033[91m(Akses: Admin)\033[0m
> \033[1mriwayatambil\033[0m   => melihat record pengambilan consumable yang tersortir berdasar tanggal           \033[91m(Akses: Admin)\033[0m
> \033[1msave\033[0m           => menyimpan data setelah dilakukan perubahan                                      \033[91m(Akses: Admin/User)\033[0m
> \033[1mhelp\033[0m           => memberikan panduan penggunaan sistem                                            \033[91m(Akses: Admin/User)\033[0m
> \033[1mgacha\033[0m          => menggacha consumable yang ada di inventory untuk mendapatkan consumable baru    \033[91m(Akses: User)\033[0m
> \033[1mexit\033[0m           => keluar dari program                                                             \033[91m(Akses: Admin/User)\033[0m
          """)

# ============================ F17 ========================================

# Kalo mau diganti boleee, aku mbuat cuma nyoba nyoba wkwkw
def exit():
    global program

    isSave = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")
    if isSave == 'y':
        save()
    elif isSave != 'n':
        print("input tidak valid")
        exit()
    print()
    print("Terima kasih telah menggunakan kantong ajaib ^_^")
    program = False

# ============================ F10 ========================================
def mintaConsumable():
    # Meminta consumable yang tersedia pada database
    
    # input/output ->   consumable : array of array of string and integer
    #                   inventory_user : array of array of string and integer
    #                   consumable_history : array of array of string and integer
    
    # I.S. matriks data consumable, inventory_user, dan consumable_history terdefinisi
    # F.S. consumable terpinjam dan data consumable, inventory_user, consumable_history telah diubah
    
    # KAMUS LOKAL
    # ID, tanggal : string
    # indexCon, jumlah, dataInventory : integer
    # jumlahCocok : boolean
    # tambahHistory, tambahInventory : array of string and integer
    
    # Function / Procedure
    # cariID(data : array of array of string and integer, ID : string) -> integer
    # Mencari index dimana ID adaa pada data
    # I.S. data dan ID terdefinisi
    # F.S. dikembalikan index dimana ID berada pada data
    
    # cariData(data)
    # Mencari "dicari" di dalam data berdasarkan index kolomnya
    # I.S. data, dicari, dan index terdefinisi
    # F.S. dikembalikan index baris dimana "dicari" berada pada data
    
    # Bold(string) -> string
    # Mengubah text menjadi terlihat bold jika di-print
    # I.S. text terdefinisi
    # F.S. text diberi 'kode' yang jika di-print text menjadi terlihat bold

    # ALGORITMA
    ID = input("Masukkan ID item: ")
    
    # Validasi ID ada
    while (cariID(consumable,ID) == None):
        print("ID item tidak tersedia, mohon inputkan ID yang benar")
        print()
        ID = input("Masukkan ID item: ")
        indexCon = cariID(consumable,ID)
    
    # Validasi jumlah
    jumlahCocok = False
    while not jumlahCocok:
        try:
            jumlah = int(input("Jumlah: "))
            if jumlah > consumable[indexCon][3]:
                print("Jumlah melebihi jumlah database")
                print()
            elif jumlah <= 0:
                print("Jumlah harus positif")
                print()
            else:
                jumlahCocok = True
        except ValueError:
            print("Jumlah harus berupa bilangan bulat, silakan input kembali")
            print()
    
    # Validasi tanggal
    tanggal = input("Tanggal permintaan: ")
    while not tglValid(tanggal):
        print("Tanggal yang diinputkan invalid, mohon inputkan kembali")
        print()
        tanggal = input("Tanggal permintaan: ")
    
    # Mengubah data pada consumable, consumable_history, dan inventory_user
    consumable[indexCon][3] -= jumlah
    tambahHistory = ["CH" + str(len(consumable_history)), idUser, ID, tanggal, jumlah]
    consumable_history.append(tambahHistory)
    dataInventory = cariData(inventory_user,ID,1)
    if dataInventory == None:
        tambahInventory = [idUser,ID,jumlah]
        inventory_user.append(tambahInventory)
    else:
        inventory_user[dataInventory][2] += jumlah
    
    # Mencetak ke layar bahwa consumable berhasil diambil
    print("Item " + Bold(consumable[indexCon][1] + " (x" + str(jumlah) + ")") + " telah berhasil diambil!")