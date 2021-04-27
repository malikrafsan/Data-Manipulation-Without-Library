import os; import sys; import math; import time; import argparse; import datetime

# ============================ F1 ========================================
def register():
    # Belum selesai, belum dikasih validasi username unik
    global user
    
    nama = input("Masukkan nama: ")
    username = input("Masukkan username: ")
    notUnik = True
    while notUnik:
        notUnik = False
        for i in range(len(user)):
            if user[i][1] == username:
                notUnik = True
                print()
                print("Ssername telah digunakan oleh user lain")
                print("Silakan input username yang berbeda")
                print()
                username = input("Masukkan username: ")
    password = input("Masukkan password: ")
    alamat = input("Masukkan alamat: ")
    
    count = 0
    for i in range(len(user)):
        if user[i][0][0] == 'U':
            count += 1
    
    id_user = "U" + str(count + 1)
    
    register = [[id_user,username,nama,alamat,hashing(password),"User"]]

    user += register
    print("User", username, "telah berhasil register ke dalam Kantong Ajaib.")

# ============================ F2 ========================================
def login():
    global hasLogin
    global isAdmin
    global idUser
    
    while True:
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")
        print()
        for i in range(len(user)):
            if (username == user[i][1]) and (str(hashing(password)) == str(user[i][4])): #belum dihash
                hasLogin = True
                idUser = user[i][0]
                print("Selamat datang " + Bold(user[i][2]) + " ^_^")
                if user[i][5] == "Admin":
                    isAdmin = True
                break
        if not hasLogin:
            print("Username atau password Anda tidak cocok")
            print("Silakan masukkan kembali username dan password")
            print()
        else:
            break
        
# ============================ F3 ========================================
def cariRarity():
    rarity = input("Masukkan rarity: ")
    
    print()
    print("Hasil pencarian: ")
    print()
    
    for i in range(len(gadget)):
        if gadget[i][4] == rarity:
            print("Nama             :", gadget[i][1])
            print("Deskripsi        :", gadget[i][2])
            print("Jumlah           :", gadget[i][3])
            print("Rarity           :", gadget[i][4])
            print("Tahun ditemukan  :", gadget[i][5])
            print()

# ============================ F4 ========================================
def caritahun():
  while True:
      try:
        tahun = int(input("Masukkan tahun: "))
        kategori = input("Masukkan kategori: ")
        found = False

        print()
        print("Hasil pencarian: ")
        print()
        
        if kategori == "=":
          for i in range(1,len(gadget)):
            if gadget[i][5] == tahun:
              print(f"Nama: {gadget[i][1]}")
              print(f"Deskripsi: {gadget[i][2]}")
              print(f"Jumlah: {gadget[i][3]}")
              print(f"Rarity: {gadget[i][4]}")
              print(f"Tahun Ditemukan: {gadget[i][5]}")
              print()
              found = True
        elif kategori == "<":
          for i in range(1, len(gadget)):
            if gadget[i][5] < tahun:
              print(f"Nama: {gadget[i][1]}")
              print(f"Deskripsi: {gadget[i][2]}")
              print(f"Jumlah: {gadget[i][3]}")
              print(f"Rarity: {gadget[i][4]}")
              print(f"Tahun Ditemukan: {gadget[i][5]}")
              print()
              found = True
        elif kategori == ">":
          for i in range(1, len(gadget)):
            if gadget[i][5] > tahun:
              print(f"Nama: {gadget[i][1]}")
              print(f"Deskripsi: {gadget[i][2]}")
              print(f"Jumlah: {gadget[i][3]}")
              print(f"Rarity: {gadget[i][4]}")
              print(f"Tahun Ditemukan: {gadget[i][5]}")
              print()
              found = True
        elif kategori == "<=":
          for i in range(1, len(gadget)):
            if gadget[i][5] <= tahun:
              print(f"Nama: {gadget[i][1]}")
              print(f"Deskripsi: {gadget[i][2]}")
              print(f"Jumlah: {gadget[i][3]}")
              print(f"Rarity: {gadget[i][4]}")
              print(f"Tahun Ditemukan: {gadget[i][5]}")
              print()
              found = True
        elif kategori == ">=":
          for i in range(1, len(gadget)):
            if gadget[i][5] >= tahun:
              print(f"Nama: {gadget[i][1]}")
              print(f"Deskripsi: {gadget[i][2]}")
              print(f"Jumlah: {gadget[i][3]}")
              print(f"Rarity: {gadget[i][4]}")
              print(f"Tahun Ditemukan: {gadget[i][5]}")
              print()
              found = True
        if found == False:
              print("Tidak ada gadget yang ditemukan")
      except ValueError:
        print()
      else:
        break

# ============================ F5 ========================================
def tambahItem():
    # Khusus admin, nanti diberi validasi di main program
    
    lanjut = False
    while not lanjut:
        print()
        ID = input("Masukkan ID: ")
        if (ID[0] == 'G'):
            if IDItemAda(gadget,ID):
                print()
                print("Gagal menambahkan item karena ID sudah ada.")
            else:
                lanjut = True
        elif (ID[0] == 'C'):
            if IDItemAda(consumable,ID):
                print()
                print("Gagal menambahkan item karena ID sudah ada.")
            else:
                lanjut = True
        else:
            print("Gagal menambahkan item karena ID tidak valid.") # asumsi ID diawali huruf besar (kapitalisasi benar)
    
    if lanjut:
        nama = input("Masukkan Nama: ")
        deskripsi = input("Masukkan Deskripsi: ")
        isNumber = False
        while not isNumber:
            jumlah = input("Masukkan Jumlah: ")
            try:
                jumlah = int(jumlah)
                isNumber = True
            except:
                ValueError
                print("Jumlah harus berupa bilangan integer, silakan masukkan kembali")
                print()
        isRarity = False
        while not isRarity:
            rarity = input("Masukkan Rarity: ")
            if rarity in "CBAS":
                break
            else:
                print("Rarity harus berupa karakter C, B, A, atau S")
                print()
        
        arrTambahItem = [ID,nama,deskripsi,jumlah,rarity]
        if ID[0] == 'G':
            isTahun = False
            while not isTahun:
                tahun = input("Masukkan tahun ditemukan: ")
                try:
                    tahun = int(tahun)
                    break
                except:
                    ValueError
                    print("Tahun harus berupa bilangan integer, silakan masukkan kembali")
                    print()
            arrTambahItem.append(tahun)
            gadget.append(arrTambahItem)
        else:
            consumable.append(arrTambahItem)
        print("Item telah berhasil ditambahkan ke database.")

# ============================ F6 ========================================
def hapusItem():
    ID = input("Masukkan ID item: ")
    if ID[0] == 'G':
        if IDItemAda(gadget,ID):
            urutan = cariID(gadget,ID)
            jawaban = input("Apakah anda yakin ingin menghapus " + gadget[urutan][1] + " (Y/N)? ")
            if jawaban == 'Y':
                gadget.pop(urutan)
                print()
                print("Item telah berhasil dihapus dari database.")
        else:
            print()
            print("Tidak ada item dengan ID tersebut.")
    elif ID[0] == 'C':
        if IDItemAda(consumable,ID):
            urutan = cariID(consumable,ID)
            jawaban = input("Apakah anda yakin ingin menghapus " + consumable[urutan][1] + " (Y/N)? ")
            if jawaban == 'Y':
                consumable.pop(urutan)
                print()
                print("Item telah berhasil dihapus dari database.")
        else:
            print()
            print("Tidak ada item dengan ID tersebut.")
    else:
        print()
        print("Tidak ada item dengan ID tersebut.")

# ============================ F7 ========================================
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

# ============================ F10 ========================================

"""def mintaConsumable():
    ID = input("Masukkan ID item: ")
    jumlah = input("Jumlah: ")
    tanggal = input("Tanggal permintaan: ") #belum divalidasi
    arrMintaConsumable = [ID,jumlah,tanggal]
    consumable.append(arrMintaConsumable)
    print("")
    print(f"Item {ID} (x{jumlah}) telah berhasil diambil!")"""



# ============================ F11 ========================================
def riwayatPinjam():
    count = 0
    riwayatPinjamPrint(count)

def riwayatPinjamPrint(count):
    borrowSort = sorted(gadget_borrow_history[count+1:], key = lambda date: datetime.datetime.strptime(date[3], '%d/%m/%Y'),reverse=True)
    bisaLanjut = True
    for i in range(5):
        try:
            namaUser = user[cariID(user,borrowSort[i][1])][2]
            namaGadget = gadget[cariID(gadget,borrowSort[i][2])][1]
            print()
            print(i)
            print("ID Peminjam          : " + borrowSort[i][1])
            print("Nama Pengambil       : " + namaUser)
            print("Nama Gadget          : " + namaGadget)
            print("Tanggal Peminjamanan : " + borrowSort[i][3])
            print("Jumlah               : " + str(borrowSort[i][4]))
        except:
            IndexError
            print()
            print("Data sudah habis")
            bisaLanjut = False
            break
    if bisaLanjut and len(borrowSort) != 5:
        print()
        lanjut = input("Apakah mau ditampilkan data lebih lanjut? (Y/N) ")
        if lanjut == 'Y':
            count += 5
            riwayatPinjamPrint(count)
# ============================ F14 ========================================
def load_data(file):
    f = open(file,"r")
    raw_lines = f.readlines()
    f.close()
    lines = [raw_line.replace("\n", "") for raw_line in raw_lines]
    lstAll = []
    for line in lines:
        lst = []
        data =""
        for i in range(len(line)):
            if line[i] == ';':
                lst.append(data)
                data = ""
            elif (i == len(line) - 1):
                lst.append(data + line[i])
            else:
                data += line[i]
        lstAll.append(lst)
    return lstAll

def tryInt(data):
    for i in range(len(data)):
        for j in range(len(data[i])):
            try:
                data[i][j] = int(data[i][j])
            except:
                ValueError
    return data

def load(): 
    global user
    global gadget
    global consumable
    global consumable_history
    global gadget_borrow_history
    global gadget_return_history
    
    os.chdir('./csvFolder')
    user = load_data("user.csv")
    gadget = tryInt(load_data("gadget.csv"))
    consumable = tryInt(load_data("consumable.csv"))
    consumable_history = tryInt(load_data("consumable_history.csv"))
    gadget_borrow_history = tryInt(load_data("gadget_borrow_history.csv"))
    gadget_return_history = tryInt(load_data("gadget_return_history.csv"))
    os.chdir('../')

# ============================ F15 ========================================
def save_data(file,data):
    data = convert_datas_to_string(data)
    
    f = open(file, "w") 
    f.write(data)
    f.close()

def save():
    parent = os.getcwd()
    directory = input("Masukkan nama folder penyimpanan : ")

    path = os.path.join(parent, directory)
    try:
        os.mkdir(path)
    except:
        FileExistsError
    os.chdir('./' + directory)
    print()
    print("Saving...")
    time.sleep(2)

    save_data("user.csv",user)
    save_data("gadget.csv",gadget)
    save_data("consumable.csv",consumable)
    save_data("gagdet_borrow_history.csv",gadget_borrow_history)
    save_data("gadget_return_history.csv",gadget_return_history)
    save_data("consumable_history.csv",consumable_history)    
    
    print("Data telah disimpan pada folder " + Bold(directory))
    os.chdir('../')
    
def convert_datas_to_string(file):
    string_data = ""
    for arr_data in file:
        arr_data_all_string = [str(var) for var in arr_data]
        string_data += ";".join(arr_data_all_string)
        string_data += "\n"
    return string_data

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

# ============================ FB01 ========================================
def hashing(str):
    # P and M
    P = 101
    m = 1e9 + 1
    powerOfP = 1
    hashed = 0
    # Loop to calculate the hash value
    # by iterating over the elements of string
    for i in range(len(str)):
        hashed = ((hashed + (ord(str[i]) - ord('!') + 1) * powerOfP) % m) 
        powerOfP = (powerOfP * P) % m
    return int(hashed)

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

# ============================ FUNGSI TAMBAHAN ========================================

# Mengembalikan string menjadi tulisan tebal
def Bold(string):
    hasil = "\033[1m" + string + "\033[0m"
    return hasil

# Mengubah data
def modify_data(data, idx, col, value):
    data[idx][col] = value
    return data

# Mencari data Item berdasarkan ID
def cariID(data,ID):
    for i in range(len(data)):
        if data[i][0] == ID:
            return i

# Mengecek ada tidaknya item
def IDItemAda(data,ID):
    Ada = False
    for i in range(len(data)):
        if data[i][0] == ID:
            return True
    return False

# Mencari data berdasarkan index (generalisasi cariID)
def cariData(data,dicari,index):
    for i in range(len(data)):
        if data[i][index] == dicari:
            return i

# Mengembalikan string menjadi string berwarna jika di-print
def colorStr(string,color):
    if color == "purple":
        warna = '\033[95m'
    elif color == "cyan":
        warna = '\033[96m'
    elif color == "darkcyan":
        warna = '\033[36m'
    elif color == "blue":
        warna = '\033[94m'
    elif color == "green":
        warna = '\033[92m'
    elif color == "yellow":
        warna = '\033[93m'
    elif color == "red":
        warna = '\033[91m'
    elif color == "bold":
        warna = '\033[1m'
    else:
        return string
    return warna + string + '\033[0m'

# Memvalidasi input tanggal
def tglValid(date):
    date_format = '%d/%m/%Y'
    try:
        datetime.datetime.strptime(date, date_format)
        return True
    except ValueError:
        return False

# ============================== MAIN PROGRAM =======================================

user =[]; gadget = []; consumable = []; consumable_history = []; gadget_borrow_history = []; gadget_return_history = []
idUser = ""; random=0; lstChance = [0,0,0,0]

program = True
hasLogin = False
isAdmin = False

print("Loading...")
time.sleep(2)
load()
print()
print("""\
\033[93m __  __               __                          _______ __         __ __    \033[0m
\033[93m|  |/  |.---.-.-----.|  |_.-----.-----.-----.    |   _   |__|.---.-.|__|  |--.\033[0m
\033[93m|     < |  _  |     ||   _|  _  |     |  _  |    |       |  ||  _  ||  |  _  |\033[0m
\033[93m|__|\__||___._|__|__||____|_____|__|__|___  |    |___|___|  ||___._||__|_____|\033[0m
\033[93m                                      |_____|           |___|                 \033[0m

\033[36m⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣤⣴⣶⣶⣶⣶⣶⠶⣶⣤⣤⣀⠀⠀⠀⠀⠀⠀ \033[0m
\033[36m⠀⠀⠀⠀⠀⠀⠀⢀⣤⣾⣿⣿⣿⠁⠀⢀⠈⢿⢀⣀⠀⠹⣿⣿⣿⣦⣄⠀⠀⠀ \033[0m
\033[36m⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⠿⠀⠀⣟⡇⢘⣾⣽⠀⠀⡏⠉⠙⢛⣿⣷⡖⠀ \033[0m
\033[36m⠀⠀⠀⠀⠀⣾⣿⣿⡿⠿⠷⠶⠤⠙⠒⠀⠒⢻⣿⣿⡷⠋⠀⠴⠞⠋⠁⢙⣿⣄ \033[0m
\033[36m⠀⠀⠀⠀⢸⣿⣿⣯⣤⣤⣤⣤⣤⡄⠀⠀⠀⠀⠉⢹⡄⠀⠀⠀⠛⠛⠋⠉⠹⡇ \033[0m
\033[36m⠀⠀⠀⠀⢸⣿⣿⠀⠀⠀⣀⣠⣤⣤⣤⣤⣤⣤⣤⣼⣇⣀⣀⣀⣛⣛⣒⣲⢾⡷ \033[0m
\033[36m⢀⠤⠒⠒⢼⣿⣿⠶⠞⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠀⣼⠃ \033[0m
\033[36m⢮⠀⠀⠀⠀⣿⣿⣆⠀⠀⠻⣿⡿⠛⠉⠉⠁⠀⠉⠉⠛⠿⣿⣿⠟⠁⠀⣼⠃⠀ \033[0m
\033[36m⠈⠓⠶⣶⣾⣿⣿⣿⣧⡀⠀⠈⠒⢤⣀⣀⡀⠀⠀⣀⣀⡠⠚⠁⠀⢀⡼⠃⠀⠀ \033[0m
\033[36m⠀⠀⠀⠈⢿⣿⣿⣿⣿⣿⣷⣤⣤⣤⣤⣭⣭⣭⣭⣭⣥⣤⣤⣤⣴⣟⠁\033[0m
                    """)


print('Selamat datang di "Kantong Ajaib!"')

while (program):
    print(colorStr(">>> ","red"),end='')
    perintah = input()
    if perintah == "help":
        pass
        # printhelp()
    elif perintah == "login":
        if hasLogin:
            print(colorStr("Anda sudah login, exit terlebih dahulu untuk menggunakan akun lain","red"))
        else:
            login() #dapet idUser
    else:
        if hasLogin:
            if perintah == "register":
                if isAdmin:
                    register()
                else:
                    print("Maaf, hanya boleh diakses oleh admin ^_^")
                    pass #print() peringatan
            elif perintah == "carirarity":
                cariRarity()
            elif perintah == "caritahun":
                caritahun()
            elif perintah == "tambahitem":
                if isAdmin:
                    tambahItem()
                else:
                    pass #print() peringatan
            elif perintah == "hapusitem":
                if isAdmin:
                    hapusItem()
                else:
                    pass #print() peringatan
            elif perintah == "ubahjumlah":
                if isAdmin:
                    ubahjumlah()
                else:    
                    pass #print() peringatan
            elif perintah == "pinjam":
                if not isAdmin:
                    pass #pinjam()
                else:
                    pass #print() peringatan
            elif perintah == "kembalikan":
                if not isAdmin:
                    pass #kembalikan()
                else:
                    pass #print() peringatan
            elif perintah == "minta":
                if not isAdmin:
                    mintaConsumable()
                else:
                    pass #print() peringatan
            elif perintah == "riwayatpinjam":
                if isAdmin:
                    riwayatPinjam()
                else:
                    pass #print() peringatan
            elif perintah == "riwayatkembali":
                if isAdmin:    
                    pass #riwayatKembali
                else:
                    pass #print() peringatan
            elif perintah == "riwayatambil":
                if isAdmin:
                    pass #riwayatAmbil()
                else:
                    pass #print() peringatan
            elif perintah == "save":
                save()
            elif perintah == "exit":
                # Diganti ajaaa gapapaa, ini cuma testing
                exit()
                print("""\
                    
\033[36m⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣤⣴⣶⣶⣶⣶⣶⠶⣶⣤⣤⣀⠀⠀⠀⠀⠀⠀ \033[0m
\033[36m⠀⠀⠀⠀⠀⠀⠀⢀⣤⣾⣿⣿⣿⠁⠀⢀⠈⢿⢀⣀⠀⠹⣿⣿⣿⣦⣄⠀⠀⠀ \033[0m
\033[36m⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⠿⠀⠀⣟⡇⢘⣾⣽⠀⠀⡏⠉⠙⢛⣿⣷⡖⠀ \033[0m
\033[36m⠀⠀⠀⠀⠀⣾⣿⣿⡿⠿⠷⠶⠤⠙⠒⠀⠒⢻⣿⣿⡷⠋⠀⠴⠞⠋⠁⢙⣿⣄ \033[0m
\033[36m⠀⠀⠀⠀⢸⣿⣿⣯⣤⣤⣤⣤⣤⡄⠀⠀⠀⠀⠉⢹⡄⠀⠀⠀⠛⠛⠋⠉⠹⡇ \033[0m
\033[36m⠀⠀⠀⠀⢸⣿⣿⠀⠀⠀⣀⣠⣤⣤⣤⣤⣤⣤⣤⣼⣇⣀⣀⣀⣛⣛⣒⣲⢾⡷ \033[0m
\033[36m⢀⠤⠒⠒⢼⣿⣿⠶⠞⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠀⣼⠃ \033[0m
\033[36m⢮⠀⠀⠀⠀⣿⣿⣆⠀⠀⠻⣿⡿⠛⠉⠉⠁⠀⠉⠉⠛⠿⣿⣿⠟⠁⠀⣼⠃⠀ \033[0m
\033[36m⠈⠓⠶⣶⣾⣿⣿⣿⣧⡀⠀⠈⠒⢤⣀⣀⡀⠀⠀⣀⣀⡠⠚⠁⠀⢀⡼⠃⠀⠀ \033[0m
\033[36m⠀⠀⠀⠈⢿⣿⣿⣿⣿⣿⣷⣤⣤⣤⣤⣭⣭⣭⣭⣭⣥⣤⣤⣤⣴⣟⠁\033[0m
                                    """)
            elif perintah == "gacha":
                gacha()
            else:
                print(colorStr("Input anda tidak valid, ketik help untuk mendapatkan daftar input yang valid","red")) #diganti nanti 
                print()
                #print("Berikut merupakan input yang valid")
                #help()        
        else:
            print(colorStr("Anda harus login terlebih dahulu","red"))
            