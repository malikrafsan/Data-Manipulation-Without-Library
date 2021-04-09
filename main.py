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
    global login_status
    global isAdmin
    
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")

    for i in range(len(user)):
        if (username == user[i][1]) and (password == user[i][3]):
            login_status = True
            if user[i][5] == "Admin":
                isAdmin = True
    
    if login_status == False:
        print("Username atau password Anda tidak cocok")
        
# ============================ F3 ========================================
def carirarity():
    data = gadget
    rarity = input("Masukkan rarity: ")
    
    print()
    print("Hasil pencarian: ")
    print()
    
    for i in range(len(data)):
        if data[i][4] == rarity:
            print("Nama             :", data[i][1])
            print("Deskripsi        :", data[i][2])
            print("Jumlah           :", data[i][3])
            print("Rarity           :", data[i][4])
            print("Tahun ditemukan  :", data[i][5])
            print()


# ============================ F5 ========================================
def IDItemAda(data, ID):
    itemAda = False
    for i in range(len(data)):
        if data[i][0] == ID:
            itemAda = True
            break
    
    return itemAda

def tambahitem():
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

def save(user,gadget):
    save_data("user.csv",user)
    save_data("gadget.csv",gadget)
    
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

# ============================== MAIN PROGRAM =======================================

user =[]; gadget = []; consumable = []; consumable_history = []; gadget_borrow_history = []; gadget_return_history = []

program = True
login_status = False
isAdmin = False

while (program):
    print("Loading...")
    time.sleep(2)
    load()
    print('Selamat datang di "Kantong Ajaib!"')
    perintah = input((">>> "))
    if perintah == "help":
        pass
        # printhelp()
    elif perintah == "login":
        login()
    else:
        if login_status == True:
            if perintah == "register":
                register()
            # elif ...
            # elif ...
        else:
            print("Anda harus login terlebih dahulu")