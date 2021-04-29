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
    
    user = load_data("user.csv")
    gadget = tryInt(load_data("gadget.csv"))
    consumable = tryInt(load_data("consumable.csv"))
    consumable_history = tryInt(load_data("consumable_history.csv"))
    gadget_borrow_history = tryInt(load_data("gadget_borrow_history.csv"))
    gadget_return_history = tryInt(load_data("gadget_return_history.csv"))

user =[]; gadget = []; consumable = []; consumable_history = []; gadget_borrow_history = []; gadget_return_history = []

import os
import sys
"""
oldDir = sys.path[0]

print("AAAAAAAAA")

for (root,dirs,files) in os.walk(oldDir, topdown=True):
    #print(root)
    #print(dirs)
    print(files)

print("AAAAAAAA")
for files in os.walk(oldDir,topdown=True):
    print(files)
"""
"""
parent = os.getcwd()
directory = input("Masukkan directory: ")

path = os.path.join(parent, directory)
try:
    os.mkdir(path)
    print("Directory '% s' created" % directory) 
except:
    FileExistsError
    print("Folder sudah ada")
    os.chdir('./tes')
    directory = input("Buat: ")
    path = os.path.join(parent, directory)
    os.mkdir(path)
    print() 
    path = os.getcwd()
    dir_list = os.listdir(path) 

    print("Files and directories in '", path, "' :") 
  
# print the list 
    print(dir_list)
"""
"""
print(os.getcwd())
os.chdir('./tes')
print(os.getcwd())
"""
# ============================ F15 ========================================
def save_data(file,data):
    f = open(file, "w") 
    f.write(data)
    f.close()

def save():
    parent = os.getcwd()
    directory = input("Masukkan directory: ")

    path = os.path.join(parent, directory)
    try:
        os.mkdir(path)
    except:
        FileExistsError
    os.chdir('./' + directory)

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

user = [['id', 'username', 'nama', 'alamat', 'password', 'role'], ['A1', 'malikakbar', 'Malik Akbar', 'Solo', 'mabar', 'Admin'], 
        ['U1', 'willy123', 'Willy Wonka', 'Semarang', 'akuwilly', 'User'], ['A2', 'nobita', 'Nobi Nobita', 'Tokyo', 'akunobi', 'Admin'], 
        ['U2', 'giant', 'Sutetsu', 'Tokyo juga', 'akugendud', 'User'], ['U3', 'rerekeren', 'Rere Roro', 'Jakarta', 'akurere', 'User'], 
        ['U4', 'tsubasa', 'Captain Tsubasa', 'Kyoto', 'akutsubasa', 'User']]
gadget = [['id', 'nama', 'deskripsi', 'jumlah', 'rarity', 'tahun_ditemukan'], ['G1', 'ini gadget', 'no desc', 5, 'C', 2002], 
          ['G2', 'Anywhere Door', 'Pintu kemana saja', 1, 'S', 2121], ['G3', 'Translation Jelly', 'Jelly buat translate', 10, 'A', 2100], 
          ['G4', 'Takecopter', 'Buat terbang ngab', 5, 'B', 2001], ['G5', '4D Pocket', 'Kantong tapi 4D hehe', 2, 'S', 2210], 
          ['G6', 'Time Cloth', 'Buat baju', 6, 'C', 2122], ['G7', 'Big Light', 'Buat gedein barang', 3, 'B', 2222], 
          ['G8', 'Small Light', 'Buat ngecilin barang', 10, 'A', 2000]]
consumable = [['id', 'nama', 'deskripsi', 'jumlah', 'rarity'], ['C1', 'permen', 'permen doang', 1000, 'C'], ['C2', 'dorayaki', 'enak banget sumpah', 20, 'A'], 
              ['C3', 'Ramen', 'mie ayam jejepangan hehe', 50, 'B'], ['C4', 'Udon', 'mirip ramen tapi rada beda', 40, 'B'], 
              ['C5', 'Sukiyaki', 'daging + sayur, enak', 34, 'C'], ['C6', 'Japanese Soba', 'Mie tapi soba', 4, 'S'], 
              ['C7', 'Sushi', 'yaaaa sushi, apalagi kalo bukan sushi', 6, 'S']]
consumable_history = [['id', 'id_pengambil', 'id_consumable', 'tanggal_peminjaman', 'jumlah'], ['CH1', 'U3', 'C1', '14/04/2021', 1000], 
                      ['CH2', 'U2', 'C3', '15/04/2021', 50], ['CH3', 'U2', 'C6', '15/04/2021', 4]]
gadget_borrow_history = [['id', 'id_peminjam', 'id_gadget', 'tanggal_peminjaman', 'jumlah'], ['GBH1', 'U1', 'G6', '14/04/2021', 6], 
                         ['GBH2', 'U2', 'G8', '15/04/2021', 10], ['GBH3', 'U2', 'G1', '15/04/2021', 5],
                         ['GBH2', 'U3', 'G8', '15/04/2021', 10], ['GBH3', 'U4', 'G1', '15/04/2021', 5]]
gadget_return_history = [['id', 'id_peminjam', 'id_gadget', 'tanggal_pengembalian', 'jumlah_peminjaman'], 
                         ['GRH1', 'U1', 'G6', '15/04/2021', 6], ['GRH2', 'U2', 'G1', '16/04/2021', 5]]

#save()
#from datetime import datetime
import datetime
#gadget_borrow_history[1:].sort(key = lambda date: datetime.strptime(date[3], '%d/%m/%Y'))
#borrowSort = sorted(gadget_borrow_history[1:], key = lambda date: datetime.datetime.strptime(date[3], '%d/%m/%Y'))
#print(borrowSort)
"""
# Mencari data Item berdasarkan ID
def cariID(data,ID):
    urutan = 0
    for i in range(len(data)):
        if data[i][0] == ID:
            urutan = i
            break
    return urutan
"""
# Mencari data Item berdasarkan ID
def cariID(data,ID):
    for i in range(len(data)):
        if data[i][0] == ID:
            return i
        
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
    print()
        
#riwayatPinjam()

import F10

#F10.mintaConsumable()
"""
import datetime
date_string = '2017-10-21'
date_format = '%Y-%m-%d'
try:
    date_obj = datetime.datetime.strptime(date_string, date_format)
    print(date_obj)
except ValueError:
    print("Incorrect data format, should be YYYY-MM-DD")
"""
"""import argparse
parser = argparse.ArgumentParser(description="Menerima input nama folder")
parser.add_argument("folder", type=str, help="echo the string you use here")

parent = os.getcwd()
directory = parser.parse_args().folder

path = os.path.join(parent, directory)
print(path)
#os.chdir()"""

def cariID(data,ID):
    for i in range(len(data)):
        if data[i][0] == ID:
            return i
"""def login():
    # Melakukan prosedur login ke program dengan mengecek apakah data yang diinputkan
    # sudah terdaftar di database
    
    # input ->  user : array of array of string and integer, 
    #           hasLogin, isAdmin : boolean 
    #           idUser : string
    # output -> hasLogin, isAdmin : boolean
    
    # I.S.  matriks data user, variable hasLogin, isAdmin, dan idUser terdefinisi
    # F.S.  mengubah variable hasLogin jika username dan password sesuai dengan data
    #       dan isAdmin jika rolenya adalah admin
    
    # KAMUS LOKAL
    # username, password : string
    # i : integer
    # rolling : boolean
    
    # Variable global
    global hasLogin
    global isAdmin
    global idUser
    
    # Function / Procedure
    # hashing(password : string) -> integer
    # Meng-hash password user menggunakan metode Polynomial Rolling Hash
    # I.S. password yang belum di hash terdefinisi
    # F.S. password ter-hash
    
    # Bold(text : string) -> string
    # Mengubah text menjadi terlihat bold jika di-print
    # I.S. text terdefinisi
    # F.S. text diberi 'kode' yang jika di-print text menjadi terlihat bold
    
    # ALGORITMA
    rolling = True
    while rolling:
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")
        print()
        for i in range(len(user)):
            # Mengecek apakah data yang diinputkan telah terdaftar di database
            if (username == user[i][1]) and (str(hashing(password)) == str(user[i][4])):
                hasLogin = True
                idUser = user[i][0]
                print("Selamat datang " + Bold(user[i][2]) + " ^_^")
                
                # Mengecek apakah rolenya Admin
                if user[i][5] == "Admin":
                    isAdmin = True
                break
        if not hasLogin:
            print("Username atau password Anda tidak cocok")
            print("Silakan masukkan kembali username dan password")
            print()
        else:
            rolling = False
    # rolling == False"""

def hashing(str):
    P = 101
    m = 1e9 + 1
    powerOfP = 1
    hashed = 0
    for i in range(len(str)):
        hashed = ((hashed + (ord(str[i]) - ord('!') + 1) * powerOfP) % m) 
        powerOfP = (powerOfP * P) % m
    return int(hashed)

print(hashing("akunobi"))