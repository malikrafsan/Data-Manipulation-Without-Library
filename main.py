import os
import sys
import math
import time
import argparse

# ============================ F1 ========================================
def register():
    nama = input("Masukkan nama: ")
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")
    alamat = input("Masukkan alamat: ")
    
    id_user = "U" + str(len(user))
    
    register = [[id_user,username,nama,alamat,password,"User"]]

    user += register
    print(user)
    print("User", username, "telah berhasil register ke dalam Kantong Ajaib.")

# ============================ F2 ========================================
def login():
    global hasLogin
    global isAdmin
    global idUser
    
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")

    for i in range(len(user)):
        if (username == user[i][1]) and (password == user[i][3]): #belum dihash
            hasLogin = True
            idUser = user[i][0]
            if user[i][4] == "Admin":
                isAdmin = True   
    if not hasLogin:
        print("Username atau password Anda tidak cocok")
        
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

# ============================ F5 ========================================
def tambahItem():
    # Khusus admin, nanti diberi validasi di main program
    ID = input("Masukkan ID: ")
    
    lanjut = False
    if (ID[0] == 'G'):
        if IDItemAda(gadget,ID):
            print("Gagal menambahkan item karena ID sudah ada.")
        else:
            lanjut = True
    elif (ID[0] == 'C'):
        if IDItemAda(consumable,ID):
            print("Gagal menambahkan item karena ID sudah ada.")
        else:
            lanjut = True
    else:
        print("Gagal menambahkan item karena ID tidak valid.") # asumsi ID diawali huruf besar (kapitalisasi benar)
    
    if lanjut:
        nama = input("Masukkan Nama: ")
        deskripsi = input("Masukkan Deskripsi: ")
        jumlah = int(input("Masukkan Jumlah: "))
        rarity = input("Masukkan Rarity: ")
        
        daftar_rarity = "CBAS"
        if rarity in daftar_rarity:
            arrTambahItem = [ID,nama,deskripsi,jumlah,rarity]
            if ID[0] == 'G':
                tahun = int(input("Masukkan tahun ditemukan: "))
                arrTambahItem.append(tahun)
                gadget.append(arrTambahItem)
            else:
                consumable.append(arrTambahItem)
            print("Item telah berhasil ditambahkan ke database.")
        else:
            print("Input rarity tidak valid!")

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

# ============================ F11 ========================================
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
                try:
                    data = int(data)
                except:
                    ValueError
                lst.append(data)
                data = ""
            elif (i == len(line) - 1):
                lst.append(data + line[i])
            else:
                data += line[i]
        lstAll.append(lst)
    return lstAll

def load(): 
    global user
    global gadget
    global consumable
    global consumable_history
    global gadget_borrow_history
    global gadget_return_history
    
    user =[]; gadget = []; consumable = []; consumable_history = []; gadget_borrow_history = []; gadget_return_history = []
    
    user = load_data("user.csv")
    gadget = load_data("gadget.csv")
    consumable = load_data("consumable.csv")
    consumable_history = load_data("consumable_history.csv")
    gadget_borrow_history = load_data("gadget_borrow_history.csv")
    gadget_return_history = load_data("gadget_return_history.csv")

# ============================ F15 ========================================
def save_data(file,data):
    f = open(file, "w") 
    f.write(data)
    f.close()

def save():
    save_data("user.csv",user)
    save_data("gadget.csv",gadget)
    save_data("consumable.csv",consumable)
    save_data("gagdet_borrow_history.csv",gadget_borrow_history)
    save_data("gadget_return_history.csv",gadget_return_history)
    save_data("consumable_history.csv",consumable_history)    
    
def convert_datas_to_string(file):
    string_data = ""
    for arr_data in file:
        arr_data_all_string = [str(var) for var in arr_data]
        string_data += ";".join(arr_data_all_string)
        string_data += "\n"
    return string_data

# ============================ FUNGSI TAMBAHAN ========================================

# Mengubah data
def modify_data(data, idx, col, value):
    data[idx][col] = value
    return data

# Mencari data Item berdasarkan ID
def cariID(data,ID):
    urutan = 0
    for i in range(len(data)):
        if data[i][0] == ID:
            urutan = i
            break
    return urutan

# Mengecek ada tidaknya item
def IDItemAda(data,ID):
    if cariID(data,ID) == 0:
        return False
    else:
        return True

# ============================== MAIN PROGRAM =======================================

user =[]; gadget = []; consumable = []; consumable_history = []; gadget_borrow_history = []; gadget_return_history = []; idUser = ""

program = True
hasLogin = False
isAdmin = False

print("Loading...")
time.sleep(2)
load()
print('Selamat datang di "Kantong Ajaib!"')

while (program):
    perintah = input((">>> "))
    if perintah == "help":
        pass
        # printhelp()
    elif perintah == "login":
        if hasLogin:
            print("Anda sudah login, exit terlebih dahulu untuk menggunakan akun lain")
        else:
            login() #dapet idUser
    else:
        if hasLogin:
            if perintah == "register":
                if isAdmin:
                    register()
                else:
                    pass #print() peringatan
            elif perintah == "carirarity":
                cariRarity()
            elif perintah == "caritahun":
                pass #caritahun()
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
                    pass #ubahJumlah()
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
                    pass #minta()
                else:
                    pass #print() peringatan
            elif perintah == "riwayatpinjam":
                if isAdmin:
                    riwayatPinjam(idUser)
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
                pass #exit()
            else:
                print("Input anda tidak valid, ketik help untuk mendapatkan daftar input yang valid") #diganti nanti          
        else:
            print("Anda harus login terlebih dahulu")