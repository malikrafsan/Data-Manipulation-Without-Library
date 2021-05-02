import os; import sys; import math; import time; import argparse; import datetime

# ============================ F1 ========================================
def register():
    # Menambahkan data user baru ke dalam database
    # I.S. matriks data user terdefinisi
    # F.S. matriks data user ditambahkan data user baru
    
    # KAMUS LOKAL
    # nama, username, password, alamat, idUser : string
    # notUnik : boolean
    # i, count : integer
    # register : array of data_user
    
    # Variable global
    global user 
    
    # Function / Procedure
    # hashing(password : string) -> integer
    # Meng-hash password user menggunakan metode Polynomial Rolling Hash
    # I.S. password yang belum di hash terdefinisi
    # F.S. password ter-hash
    
    # ALGORITMA
    nama = input("Masukkan nama: ")
    username = input("Masukkan username: ")
    
    # Validasi username unik
    notUnik = True
    while notUnik:
        notUnik = False
        for i in range(len(user)):
            if user[i][1] == username:
                notUnik = True
                print()
                print("Username telah digunakan oleh user lain")
                print("Silakan input username yang berbeda")
                print()
                username = input("Masukkan username: ")
    # notUnik == False
    
    password = input("Masukkan password: ")
    alamat = input("Masukkan alamat: ")
    
    # Pembuatan idUSer
    count = 0
    for i in range(len(user)):
        if user[i][0][0] == 'U':
            count += 1
    id_user = "U" + str(count + 1)
    
    # Menambahkan data user baru ke dalam matriks data user
    register = [[id_user,username,nama,alamat,hashing(password),"User"]]
    user += register
    
    print("User", username, "telah berhasil register ke dalam Kantong Ajaib.")

# ============================ F2 ========================================
def login():
    # Melakukan prosedur login ke program dengan mengecek apakah data yang diinputkan
    # sudah terdaftar di database
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
    # rolling == False
        
# ============================ F3 ========================================
def cariRarity():
    # Mencari gadget yang memiliki rarity sesuai yang diinputkan
    # I.S. matriks data gadget terdefinisi
    # F.S. tercetak ke layar data gadget yang memiliki rarity sesuai yang diinputkan
    
    # KAMUS LOKAL
    # rarity : string
    # i : integer
    # ditemukan : boolean
    
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
        
# ============================ F4 ========================================
def caritahun():
  # Mencari gadget berdasarkan tahun ditemukan dan kategorinya
  # I.S. : matriks data gadget terdefinisi
  # F.S. : tercetak ke layar data gadget sesuai input tahun ditemukan dan kategorinya
  
  # KAMUS LOKAL
  # tahun, i : integer
  # kategori : string
  # found : boolean

  # ALGORITMA
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
              print()

      # Memvalidasi input tahun, dan mencegah terjadinya ValueError
      except ValueError:
        print("Tahun yang diinputkan harus berupa bilangan bulat")
        print()
      else:
        break

# ============================ F5 ========================================
def tambahItem():
    # Menambahkan data item baru ke database
    # I.S. : matriks data gadget dan consumable telah terdefinisi
    # F.S. : data item baru dimasukkan ke dalam database

    # KAMUS LOKAL
    # lanjut, isNumber : boolean
    # nama, deskripsi : string
    # jumlah, tahun : integer
    # rarity : character
    # arrTambahItem : any of data_gadget or data_consumable

    # Function / Procedure
    # IDItemAda(data : any of data_user or data_gadget or data_consumable or data_gadget_return_history or data_gadget_borrow_histroy or 
    #           data_consumable_history or data_inventory_user, ID : string) -> boolean
    # Mengecek apakah ID ada pada data
    # I.S. data dan ID terdefinisi
    # F.S. Mengembalikan True jika ID item ada di data dan False jika sebaliknya

    # ALGORITMA
    # Validasi ID
    lanjut = False
    while not lanjut:
        ID = input("Masukkan ID: ")
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
            # asumsi ID diawali huruf besar (kapitalisasi benar)
            print("Gagal menambahkan item karena ID tidak valid.")

    nama = input("Masukkan Nama: ")
    deskripsi = input("Masukkan Deskripsi: ")
    
    # Validasi jumlah
    isNumber = False
    while not isNumber:
        try:
            jumlah = int(input("Masukkan Jumlah: "))
            if jumlah <= 0:
                print("Jumlah harus bernilai positif")
            else:
                isNumber = True
        except:
            ValueError
            print("Jumlah harus berupa bilangan integer, silakan masukkan kembali")
            print()
    
    # Validasi rarity
    isRarity = False
    while not isRarity:
        rarity = input("Masukkan Rarity: ")
        if rarity in "CBAS":
            isRarity = True
        else:
            print("Rarity harus berupa karakter C, B, A, atau S")
            print()
    
    arrTambahItem = [ID,nama,deskripsi,jumlah,rarity]
    if ID[0] == 'G':
        
        # Validasi tahun
        isTahun = False
        while not isTahun:
            try:
                tahun = int(input("Masukkan tahun ditemukan: "))
                break
            except:
                ValueError
                print("Tahun harus berupa bilangan integer, silakan masukkan kembali")
                print()
            # isTahun == True

        arrTambahItem.append(tahun)
        gadget.append(arrTambahItem)
    else:
        consumable.append(arrTambahItem)
    
    print("Item telah berhasil ditambahkan ke database.")

# ============================ F6 ========================================
def hapusItem():
    # Menghapus gadget dari database  
    # I.S. matriks data gadget terdefinisi
    # F.S. data yang diinputkan dihapus dari data gadget

    # KAMUS LOKAL
    # ID, jawaban : string
    # urutan : integer
    # rolling : boolean

    # Function / Procedure
    # validasiYN(jawaban : string) -> boolean
    # Memvalidasi input dari user, harus 'Y' atau 'N'
    # I.S. string terdefinisi
    # F.S. mengembalikan True jika string adalah 'Y' atau 'N' dan False jika sebaliknya

    # IDItemAda(data : any of data_user or data_gadget or data_consumable or data_gadget_return_history or data_gadget_borrow_histroy or 
    #                   data_consumable_history or data_inventory_user, ID : string) -> boolean
    # Mengecek apakah ID ada pada data
    # I.S. data dan ID terdefinisi
    # F.S. Mengembalikan True jika ID item ada di data dan False jika sebaliknya

    # ALGORITMA
    # Validasi ID
    rolling = True
    while rolling:
        print()
        ID = input("Masukkan ID item: ")
        if ID[0] == 'G':
            if IDItemAda(gadget,ID):
                urutan = cariID(gadget,ID)
                jawaban = input("Apakah anda yakin ingin menghapus " + gadget[urutan][1] + " (Y/N)? ")
                
                # Validasi jawaban
                while not validasiYN(jawaban):
                    jawaban = input("Apakah anda yakin ingin menghapus " + gadget[urutan][1] + " (Y/N)? ")
                    
                if jawaban == 'Y':
                    gadget.pop(urutan)
                    print()
                    print("Item telah berhasil dihapus dari database.")
                else:
                    print("Item tidak jadi dihapus dari database")
                rolling = False
            else:
                print("Tidak ada item dengan ID tersebut.")
        elif ID[0] == 'C':
            if IDItemAda(consumable,ID):
                urutan = cariID(consumable,ID)
                jawaban = input("Apakah anda yakin ingin menghapus " + consumable[urutan][1] + " (Y/N)? ")

                # Validasi jawaban
                while not validasiYN(jawaban):
                    jawaban = input("Apakah anda yakin ingin menghapus " + gadget[urutan][1] + " (Y/N)? ")

                if jawaban == 'Y':
                    consumable.pop(urutan)
                    print()
                    print("Item telah berhasil dihapus dari database.")
                else:
                    print("Item tidak jadi dihapus dari database")
                rolling = False
            else:
                print("Tidak ada item dengan ID tersebut.")
        else:
            print("ID yang anda masukkan invalid, ID harus diawali dengan huruf C atau G")
    # rolling == False

# ============================ F7 ========================================
def ubahjumlah():
    # Mengubah jumlah gadget dan consumable yang ada pada database
    # I.S. matriks data gadget dan consumable terdefinisi
    # F.S. jumlah item pada database berubah
    
    # KAMUS LOKAL
    # id_item : string
    # before, change, indeks_found: integer
    # isInteger, found : boolean
    
    # ALGORITMA
    id_item = input("Masukan ID: ")
    
    # Validasi jumlah
    isInteger = False
    while not isInteger:
        try:
            change = int(input("Masukkan Jumlah: "))
            isInteger = True
        except:
            ValueError
            print("Silahkan masukan kembali angka dengan benar")
            print()
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

# ============================ F8 ========================================
def pinjam():
    # Meminjam gadget sesuai id_item yang dimasukan dan akan mengurangi jumlah pada gadget dan menambahkan entri pada gadget_borrow_history
    # I.S. matriks data gadget dan gadget_borrow_history terdefinisi
    # F.S. jumlah gadget pada data gadget berkurang dan terdapat entri baru pada gadget_borrow_history
    
    # KAMUS LOKAL
    # id_item, id_peminjaman, data_string : string
    # condition, found, syarat_terpenuhi_1, terms : boolean
    # indeks, current_amount, amount, a : integer
    # personal_borrow : array of string
    
    # ALGORITMA    
    # Validasi ID_Item
    condition = True
    while condition:
        try:
            id_item = input("Masukan ID item: ")
            found = False
        
            for i in range(1, len(gadget)):
                if gadget[i][0] == id_item:
                    found = True
                    condition = False
                    indeks = i
            if found == False:
                print("Tidak ada item dengan ID tersebut. Silahkan masukan kembali ID item yang sesuai")
                print()
        except ValueError:
            print()
    
    # Membuat array dari setiap gadget yang user pernah pinjam
    personal_borrow = []
    for a in range(len(gadget_borrow_history)):
        if gadget_borrow_history[a][1] == idUser:
            personal_borrow.append(gadget_borrow_history[a])
    
    # Mengecek apakah user pernah meminjam dan belum mengembalikan gadget yang sama atau user belum pernah meminjam sama sekali dari gadget dengan id_item
    # Syarat 1: User sudah mengembalikan gadget dengan id_item yang dimasukan secara utuh (tidak sebagian)
    syarat_terpenuhi_1 = False
    for i in range(len(personal_borrow)-1, 0, -1):
        if personal_borrow[i][2] == id_item:
            if personal_borrow[i][5] == True:
                syarat_terpenuhi_1 = True
                break
    # Syarat 2: User belum pernah sama sekali meminjam gadget dengan id_item inputan
    check = None
    for i in range(len(personal_borrow)):
        if personal_borrow[i][2] == id_item:
            check = 'Checked'
    
    # Jika user sudah pernah mengembalikan secara lengkap gadget dengan id = id_item (atau) gadget dengan id = id item belum pernah ia pinjam sama sekali
    if syarat_terpenuhi_1 == True or check == None:
        # Validasi Tanggal
        kondisi = True
        while(kondisi):
            format = "%d/%m/%Y"
            date_string = input("Tanggal peminjaman: ")
            
            cond = False
            if len(date_string) == 10:
                cond = True
            if cond == False:
                while(True):
                    print("Masukan tanggal dengan benar, yakni 2 digit tanggal, 2 digit bulan, dan 4 digit tahun dan format DD/MM/YYYY")
                    date_string = input("Tanggal peminjaman: ")
                    if len(date_string) == 10:
                        cond = True
                        break        
            try:
                datetime.datetime.strptime(date_string, format)
                break
            except ValueError:
                print("Tanggal yang anda masukan salah. Silahkan masukan kembali tanggal dengan format DD/MM/YYYY")

        # Validasi jumlah
        current_amount = gadget[indeks][3]
        terms = True
    
        while(terms):
            try:
                amount = int(input("Jumlah peminjaman: "))
        
                if (amount <= current_amount) and (amount > 0):
                    gadget[indeks][3] = current_amount - amount
                    print(f"Item {gadget[indeks][1]} (x{amount}) berhasil dipinjam!")
                    print()
                    terms = False
                else:
                    print(f"Jumlah yang anda ingin pinjam melebihi yang ada dalam stok penyimpanan atau anda memasukan angka di bawah 1. Silahkan masukan kembali jumlah yang ingin dipinjam dengan maksimal meminjam {current_amount}")
            except ValueError:
                print("Silahkan masukan kembali jumlah dengan angka yang benar")
    
        # Memasukan ke data gadget_borrow_history
        id_peminjaman = 'GBH' + str(len(gadget_borrow_history))
    
        gadget_borrow_history.append([id_peminjaman, idUser, id_item, date_string, amount, False])
    # Kondisi jika user pernah meminjam gadget dengan id = id_item, namun belum mengembalikannya
    else:
        print("Maaf, anda pernah meminjam gadget yang sama dan belum mengembalikannya, anda harus mengembalikan secara keseluruhan gadget yang baru saja anda ingin pinjam")
        print()

# ============================ F9 + FB02 ========================================
def kembalikan():
    # Mengembalikan gadget yang pernah dipinjam baik sebagian maupun keseluruhan  
    # I.S. matriks data gadget, gadget_borrow_history, dan gadget_return_history terdefinisi
    # F.S. jumlah gadget pada data gadget berkurang dan terdapat entri baru pada gadget_borrow_history
    
    # KAMUS LOKAL
    # id_returned_gadget, id_pengembalian, tanggal : string
    # syaratnya : boolean
    # option, indeksnya, markernya, max_returned, total_amount_returned, total_amount_returned_updated, amount_returned, z, n, an : integer
    # personal_borrow_not_return, updated_unique_personal_borrow_not_returned : array of string
    # unique_personal_borrow_not_returned : set of string
    
    # ALGORITMA 
    # Menampilkan ke user gadget yang pernah ia pinjam
    personal_borrow_not_returned = []
    for a in range(len(gadget_borrow_history)):
        if gadget_borrow_history[a][1] == idUser and gadget_borrow_history[a][5] == False:
            personal_borrow_not_returned.append(gadget_borrow_history[a][2])
    
    unique_personal_borrow_not_returned = set(personal_borrow_not_returned)
    updated_unique_personal_borrow_not_returned = list(unique_personal_borrow_not_returned)

    # Kondisi jika user pernah meminjam barang sebelumnya
    if len(updated_unique_personal_borrow_not_returned) > 0:
        # Menampilkan setiap gadget yang pernah dipinjam oleh user
        for i in range(len(updated_unique_personal_borrow_not_returned)):
            for j in range(len(gadget)):
                if updated_unique_personal_borrow_not_returned[i] == gadget[j][0]:
                    print(f"{i + 1}. {gadget[j][1]}")
                
        # Meminta user memilih opsi item sesuai nomor
        banyak = len(updated_unique_personal_borrow_not_returned)
        syaratnya = True
        while(syaratnya):
            try:
                option = int(input("Masukan nomor peminjaman: "))
                if option > 0 and option <= banyak:
                    syaratnya = False
            except ValueError:
                print("Silahkan masukan kembali nomor dengan benar")
            
        # Meminta user memasukan tanggal dan memvalidasinya
        kondisi = True
        while(kondisi):
            format = "%d/%m/%Y"
            date_string = input("Tanggal pengembalian: ")
            
            cond = False
            if len(date_string) == 10:
                cond = True

            if cond == False:
                while(True):
                    print("Masukan tanggal dengan benar, yakni 2 digit tanggal, 2 digit bulan, dan 4 digit tahun dan format DD/MM/YYYY")
                    date_string = input("Tanggal pengembalian: ")
                    if len(date_string) == 10:
                        cond = True
                        break        
            try:
                datetime.datetime.strptime(date_string, format)
                break
            except ValueError:
                print("Tanggal yang anda masukan salah. Silahkan masukan kembali tanggal dengan format DD/MM/YYYY")

        # Membuat string dari gadget yang user ingin kembalikan
        id_returned_gadget = updated_unique_personal_borrow_not_returned[option - 1]
    
        # Menelusuri entri gadget yang ingin user kembalikan pada data gadget_borrow_history
        for z in range(len(gadget_borrow_history)-1, 0, -1):
            if gadget_borrow_history[z][2] == id_returned_gadget and gadget_borrow_history[z][1] == idUser:
                indeksnya = z
                break
    
        # Menelusuri data gadget untuk mendapatkan sebagian informasi dari gadget yang ingin dikembalikan
        for n in range(len(gadget)):
            if gadget[n][0] == id_returned_gadget:
                markernya = n
                break
    
        # Menghitung jumlah semua yang pernah dikembalikan sebelumnya ditambahkan (jika ada)
        total_amount_returned = 0
        for an in range(len(gadget_return_history)):
            if gadget_return_history[an][1] == gadget_borrow_history[indeksnya][0] and gadget_return_history[an][4] == 'applicable':
                total_amount_returned = total_amount_returned + gadget_return_history[an][3]
                
        # Prompting user memasukan jumlah barang yang ingin ia kembalikan (baik sebagian atau keseluruhan)
        max_returned = gadget_borrow_history[indeksnya][4] - total_amount_returned
        while(True):
            try:
                amount_returned = int(input(f"Berapa jumlah {gadget[markernya][1]} yang ingin anda kembalikan (maksimal {max_returned}): "))
                if amount_returned > 0 and amount_returned <= max_returned:
                    break
                else:
                    print("Jumlah tidak sesuai")
                    print()
            except ValueError:
                print(f"Silahkan masukan kembali jumlah {gadget[markernya][1]} yang ingin dikembalikan dengan bilangan bulat")
                
        # Menambahkan entri gadget_return_history
        id_pengembalian = 'GRH' + str(len(gadget_return_history))
        gadget_return_history.append([id_pengembalian, gadget_borrow_history[indeksnya][0], date_string, amount_returned, 'applicable'])                
        
        # Total keseluruhan yang pernah dikembalikan sebelumnya ditambah dengan yang baru saja hendak dikembalikan
        total_amount_returned_updated = total_amount_returned + amount_returned
        
        # Menambah jumlah pada data gadget sesuai jumlah yang dikembalikan
        gadget[markernya][3] = gadget[markernya][3] + amount_returned
        
        # Mengubah kolom isReturned pada gadget_borrow_history menjadi True jika jumlah yang dipinjam sudah dikembalikan utuh
        if gadget_borrow_history[indeksnya][4] - total_amount_returned_updated == 0:
            gadget_borrow_history[indeksnya][5] = True
            for m in range(len(gadget_return_history)):
                if gadget_return_history[m][1] == gadget_borrow_history[indeksnya][0]:
                    gadget_return_history[m][4] = 'not applicable'
        
        # Menampilkan nama gadget dan jumlah yang pernah ia pinjamm secara kesuluruhan     
        print(f"Item {gadget[markernya][1]} (x{amount_returned}) telah dikembalikan")
    
    # Kondisi jika user belum pernah meminjam barang
    else:
        print("Anda belum pernah meminjam gadget sama sekali")
        
# ============================ F10 ========================================
def mintaConsumable():
    # Meminta consumable yang tersedia pada database
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
    kondisi = True
    while(kondisi):
        format = "%d/%m/%Y"
        date_string = input("Tanggal permintaan: ")
        
        cond = False
        if len(date_string) == 10:
            cond = True

        if cond == False:
            while(True):
                print("Masukan tanggal dengan benar, yakni 2 digit tanggal, 2 digit bulan, dan 4 digit tahun dan format DD/MM/YYYY")
                date_string = input("Tanggal permintaan: ")
                if len(date_string) == 10:
                    cond = True
                    break        
        try:
            datetime.datetime.strptime(date_string, format)
            break
        except ValueError:
            print("Tanggal yang anda masukan salah. Silahkan masukan kembali tanggal dengan format DD/MM/YYYY")

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
        inventory_user.append([idUser, ID, amount_asked])

    # Menampilkan ke user bahwa item berhasil diminta
    print()
    print(f"Item {consumable[indeks][1]} (x{amount_asked}) telah berhasil diambil!")
    
# ============================ F11 ========================================
def riwayatPinjam():
    # Menampilkan daftar peminjaman gadget yang telah dilakukan para user ke layar
    # I.S. matriks data user, gadget, gadget_borrow_history terdefinisi
    # F.S. tercetak ke layar riwayat peminjaman user
    
    # KAMUS LOKAL
    # rolling, bisaLanjut : boolean
    # count : integer
    # borrowSort : data_gadget_borrow_history
    # namaUser, namaGadget, lanjut : string
    
    # Function / Procedure
    # validasiYN(jawaban : string) -> boolean
    # Memvalidasi input dari user, harus 'Y' atau 'N'
    # I.S. string terdefinisi
    # F.S. mengembalikan True jika string adalah 'Y' atau 'N' dan False jika sebaliknya
    
    # ALGORITMA
    rolling = True
    count = 0
    while rolling:
        # Mensortir data berdasarkan tanggal, secara descending
        borrowSort = sorted(gadget_borrow_history[count+1:], key = lambda date: datetime.datetime.strptime(date[3], '%d/%m/%Y'),reverse=True)
        bisaLanjut = True
        for i in range(5):
            try:
                namaUser = user[cariID(user,borrowSort[i][1])][2]
                namaGadget = gadget[cariID(gadget,borrowSort[i][2])][1]
                print()
                print("ID Peminjam          : " + borrowSort[i][1])
                print("Nama Pengambil       : " + namaUser)
                print("Nama Gadget          : " + namaGadget)
                print("Tanggal Peminjamanan : " + borrowSort[i][3])
                print("Jumlah               : " + str(borrowSort[i][4]))
            except:
                # Ketika data habis maka akan terjadi IndexError
                IndexError
                print()
                print("Data sudah habis")
                bisaLanjut = False
                break

        if bisaLanjut and len(borrowSort) != 5:
            print()
            lanjut = input("Apakah mau ditampilkan data lebih lanjut? (Y/N) ")
            # Validasi input
            while not validasiYN(lanjut):
                lanjut = input("Apakah mau ditampilkan data lebih lanjut? (Y/N) ")
            if lanjut == 'Y':
                count += 5
            else:
                rolling = False
        else:
            rolling = False
            
# ============================ F12 ========================================
def riwayatKembali():
    # Menampilkan daftar pengembalian gadget yang telah dilakukan para user ke layar
    # I.S. matriks data user, gadget, gadget_borrow_history terdefinisi
    # F.S. tercetak ke layar riwayat peminjaman user
    
    # KAMUS LOKAL
    # rolling, lanjutkan : boolean
    # count : integer
    # returnSort : data_gadget_return_histroy
    # namaUser, namaGadget, id_user, id_gadget, nextInp : string
    
    # Function / Procedure
    # validasiYN(jawaban : string) -> boolean
    # Memvalidasi input dari user, harus 'Y' atau 'N'
    # I.S. string terdefinisi
    # F.S. mengembalikan True jika string adalah 'Y' atau 'N' dan False jika sebaliknya

    # ALGORITMA
    rolling = True
    count = 0
    while rolling:
        # Mensortir data berdasarkan tanggal, secara descending
        returnSort = sorted(gadget_return_history[count+1:], key = lambda date: datetime.datetime.strptime(date[2], '%d/%m/%Y'),reverse=True)
        lanjutkan = True
        for i in range(5):
            try:
                #cari id gadget dan id user
                for line in range(len(gadget_borrow_history)):
                    if returnSort[i][1] == gadget_borrow_history[line][0]:
                        id_gadget = gadget_borrow_history[line][2]
                        id_user = gadget_borrow_history[line][1]

                namaUser = user[cariID(user,id_user)][2]
                namaGadget = gadget[cariID(gadget,id_gadget)][1]

                print()
                print("ID Pengembalian      : " + returnSort[i][0])
                print("Nama Pengambil       : " + namaUser)
                print("Nama Gadget          : " + namaGadget)
                print("Tanggal Pengembalian : " + returnSort[i][2])
                print("Jumlah               : " + str(returnSort[i][3]))
            except:
                # Ketika data habis maka akan terjadi IndexError
                IndexError
                print()
                print("Data sudah habis")
                lanjutkan = False
                break
        if lanjutkan and len(returnSort) != 5:
            print()
            nextInp = input("Apakah mau ditampilkan data lebih lanjut? (Y/N) ")
            # Validasi input
            while not validasiYN(nextInp):
                nextInp = input("Apakah mau ditampilkan data lebih lanjut? (Y/N) ")
            if nextInp == 'Y':
                count += 5
            else:
                rolling = False
        else:
            rolling = False

# ============================ F13 ========================================
def riwayatConsumable():
    # Menampilkan daftar pengambilan consumable yang telah dilakukan para user ke layar
    # I.S. matriks data user, gadget, gadget_borrow_history terdefinisi
    # F.S. tercetak ke layar riwayat peminjaman user
    
    # KAMUS LOKAL
    # rolling, berikutnya : boolean
    # count : integer
    # consumableSort : data_consumable_history
    # namaUser, namaConsumable : string
    
    # Function / Procedure
    # validasiYN(jawaban : string) -> boolean
    # Memvalidasi input dari user, harus 'Y' atau 'N'
    # I.S. string terdefinisi
    # F.S. mengembalikan True jika string adalah 'Y' atau 'N' dan False jika sebaliknya
    
    # ALGORITMA
    rolling = True
    count = 0
    while rolling:
        # Mensortir data berdasarkan tanggal, secara descending
        consumableSort = sorted(consumable_history[count+1:], key = lambda date: datetime.datetime.strptime(date[3], '%d/%m/%Y'),reverse=True)
        berikutnya = True
        for i in range(5):
            try:
                namaUser = user[cariID(user,consumableSort[i][1])][2]
                namaConsumable = consumable[cariID(consumable,consumableSort[i][2])][1]
                print()
                print("ID Pengambilan       : " + consumableSort[i][1])
                print("Nama Pengambil       : " + namaUser)
                print("Nama Consumable      : " + namaConsumable)
                print("Tanggal Pengambilan  : " + consumableSort[i][3])
                print("Jumlah               : " + str(consumableSort[i][4]))
            except:
                # Ketika data habis maka akan terjadi IndexError
                print(i)
                IndexError
                print()
                print("Data sudah habis")
                berikutnya = False
                break
        if berikutnya and len(consumableSort) != 5:
            print()
            nextInp = input("Apakah mau ditampilkan data lebih lanjut? (Y/N) ")
            # Validasi input
            while not validasiYN(nextInp):
                lanjut = input("Apakah mau ditampilkan data lebih lanjut? (Y/N) ")
            if nextInp == 'Y':
                count += 5
            else:
                rolling = False
        else:
            rolling = False

# ============================ F14 ========================================
def load_data(file):
    # Membaca file csv dan mengembalikan matriks data sesuai data csv
    # I.S. file terdefinisi
    # F.S. dikembalikan matriks data sesuai file
    
    # KAMUS LOKAL
    # f : SEQFILE OF
    #       (*) raw_lines : array of string
    #       (1) mark : None 
    # lst : array of string
    # data : string
    # lstAll : array of array of string
    
    # ALGORITMA
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
                # jika bertemu dengan ';' maka data akan ditambahkan ke lst
                lst.append(data)
                data = ""
            elif (i == len(line) - 1):
                # menambahkan data bagian paling belakang pada satu baris ke dalam lst
                lst.append(data + line[i])
            else:
                data += line[i]
        lstAll.append(lst)
    return lstAll

def tryChange(data):
    # Mengubah tipe data yang ada pada data menjadi boolean atau integer jika dimungkinkan
    # I.S. data terdefinisi
    # F.S. dikembalikan data dimana elemen yang dapat diubah, diubah menjadi boolean atau integer telah diubah
    
    # KAMUS LOKAL
    # i, j : integer
    
    # ALGORITMA
    for i in range(len(data)):
        for j in range(len(data[i])):
            try:
                # Dicoba diubah menjadi integer
                data[i][j] = int(data[i][j])
            except:
                ValueError
            # Dicoba diubah menjadi boolean
            if data[i][j] == "True":
                data[i][j] = True
            elif data[i][j] == "False":
                data[i][j] = False
    return data

def load(folder):
    # Membaca file-file csv pada folder yang diinputkan
    # I.S. pada folder terdapat file-file csv yang dibutuhkan
    # F.S. didapatkan matriks data sesuai dengan file-file csv yang ada

    # KAMUS LOKAL
    # user : array of data_user
    # gadget : array of data_gadget 
    # consumable : array of data_consumable
    # consumable_history : array of data_consumable_history 
    # gadget_borrow_history : array of data_gadget_borrow_history
    # gadget_return_history : array of data_gadget_return_history
    # inventory_user : array of data_inventory_user

    # Variable global
    global user
    global gadget
    global consumable
    global consumable_history
    global gadget_borrow_history
    global gadget_return_history
    global inventory_user

    # Function / Procedure
    # load_data(file : csv) -> array of array of string
    # Membaca file csv dan mengembalikan matriks data sesuai data csv
    # I.S. file terdefinisi
    # F.S. dikembalikan matriks data sesuai file

    # tryChange(data : array of array of string) -> any of data_user or data_gadget or data_consumable or data_gadget_return_history or 
    #                                               data_gadget_borrow_histroy or data_consumable_history or data_inventory_user
    # Mengubah tipe data yang ada pada data menjadi boolean atau integer jika dimungkinkan
    # I.S. data terdefinisi
    # F.S. dikembalikan data dimana elemen yang dapat diubah, diubah menjadi boolean atau integer telah diubah

    # ALGORITMA
    os.chdir('./' + str(folder))

    user = tryChange(load_data("user.csv"))
    gadget = tryChange(load_data("gadget.csv"))
    consumable = tryChange(load_data("consumable.csv"))
    consumable_history = tryChange(load_data("consumable_history.csv"))
    gadget_borrow_history = tryChange(load_data("gadget_borrow_history.csv"))
    gadget_return_history = tryChange(load_data("gadget_return_history.csv"))
    inventory_user = tryChange(load_data("inventory_user.csv"))
    os.chdir('../')

def loading():
    # Membaca argumen dari python menggunakan argparse
    # I.S. sembarang
    # F.S. Dikembalikan driectory folder csv jika ada, dan None jika tidak ada
    
    # KAMUS LOKAL
    # parser : ArgumentParser
    # directory, parent, path, files : string
    # lstFile : array of string

    # Function / Procedure
    # fileExist(files : csv) -> boolean
    # Mengecek apakah file ada atau tidak
    # I.S. sembarang
    # F.S. Dikembalikan True jika file ada, dan False jika tidak ada
    
    # ALGORITMA
    # Penjelasan program
    parser = argparse.ArgumentParser(description="""
Program Tugas Besar IF1210 Kelompok 11 Kelas 10 Dasar Pemrograman
\033[93m format input : python main.py -f <nama-folder-csv> \033[0m
""", epilog='Enjoy the program! :D')
    
    # Menghandle jika input salah
    parser.add_argument("-f","--folder", type=str, help="Inputkan nama folder csv (harus diinputkan)")  
    if parser.parse_args().folder is None:
        parser.error("""
\033[91m Nama folder csv tidak diinputkan! \033[0m
\033[93m format input : python main.py -f <nama-folder-csv> \033[0m""")
        return None
    
    # Berpindah directory ke folder csv
    directory = parser.parse_args().folder
    parent = os.getcwd()
    path = os.path.join(parent, directory)
    
    # Validasi folder ada
    if not os.path.exists(path):
        print("Nama folder yang diinputkan tidak ada")
    else:
        os.chdir('./' + directory)
        lstFile = ["user.csv","gadget.csv","gadget_borrow_history.csv","gadget_return_history.csv","consumable.csv","consumable_history.csv", "inventory_user.csv"]
        for files in lstFile:
            # Validasi file ada
            if not fileExist(files):
                print(files + " tidak tersedia di folder yang diinputkan")
                return None
        # Berpindah directory ke parent
        os.chdir('../')
        return directory
        
def fileExist(files):
    # Mengecek apakah file ada atau tidak
    # I.S. sembarang
    # F.S. Dikembalikan True jika file ada, dan False jika tidak ada
    
    # KAMUS LOKAL
    
    # ALGORITMA
    if os.path.exists(files):
        return True
    else:
        return False

# ============================ F15 ========================================
def save_data(file,data):
    # Menulis data ke dalam file csv
    # I.S. data terdefinisi
    # F.S. jika sebelumnya file sudah ada, maka di file diperbarui, dan jika belum ada, maka tertulis file baru
    
    # KAMUS LOKAL
    # data : string
    # f : SEQFILES OF
    #       (*) array of string
    #       (1) mark : None
    
    # Function / Procedure
    # convert_datas_to_string (data : array of array of string) -> string
    # Mengubah data menjadi string sesuai format agar dapat di-write ke dalam file csv
    # I.S. data terdefinisi
    # F.S. Dikembalikan string sesuai format
    
    # ALGORITMA
    data = convert_datas_to_string(data)
    
    f = open(file, "w") 
    f.write(data)
    f.close()

def convert_datas_to_string(data):
    # Mengubah data menjadi string sesuai format agar dapat di-write ke dalam file csv
    # I.S. data terdefinisi
    # F.S. Dikembalikan string sesuai format
    
    # KAMUS LOKAL
    # string_data : string
    # arr_data : any of data_user or data_gadget or data_consumable or data_gadget_return_history or data_gadget_borrow_histroy 
    #               or data_consumable_history or data_inventory_user
    # arr_data_all_string : array of string
    
    # ALGORITMA
    string_data = ""
    for arr_data in data:
        arr_data_all_string = [str(var) for var in arr_data]
        string_data += ";".join(arr_data_all_string)
        string_data += "\n"
    return string_data

def save():
    # Menyimpan data ke dalam file di folder yang diinputkan
    # I.S. user, gadget, consumable, gadget_borrow_history, gadget_return_history, consumable_history, inventory_user terdefinisi
    # F.S. file user, gadget, consumable, gadget_borrow_history, gadget_return_history, consumable_history, inventory_user tersimpan

    # KAMUS LOKAL
    # parent, directory, path : string

    # Function / Procedure
    # save_data (file : csv, data : any of data_user or data_gadget or data_consumable or data_gadget_return_history or 
    #                               data_gadget_borrow_histroy or data_consumable_history or data_inventory_user)
    # Menulis data ke dalam file csv
    # I.S. data terdefinisi
    # F.S. jika sebelumnya file sudah ada, maka di file diperbarui, dan jika belum ada, maka tertulis file baru

    # ALGORITMA
    parent = os.getcwd()

    # Validasi directory
    checkedDir = False
    while not checkedDir:
        directory = input("Masukkan nama folder penyimpanan : ")
        checkedDir = True
        for i in range(len(directory)):
            if directory[i] in ('\/:*?"<>|'):
                checkedDir = False
                print('nama folder anda mengandung \/:*?"<>|')
                print()

    path = os.path.join(parent, directory)

    try:
        # Membuat folder baru jika folder belum ada
        os.mkdir(path)
    except:
        FileExistsError

    # Berpindah directory ke dalam folder csv
    os.chdir('./' + directory)
    print()
    print("Saving...")
    time.sleep(2)

    # Menyimpan file-file csv
    save_data("user.csv",user)
    save_data("gadget.csv",gadget)
    save_data("consumable.csv",consumable)
    save_data("gadget_borrow_history.csv",gadget_borrow_history)
    save_data("gadget_return_history.csv",gadget_return_history)
    save_data("consumable_history.csv",consumable_history)
    save_data("inventory_user.csv",inventory_user)

    print("Data telah disimpan pada folder " + Bold(directory))
    # Berpindah directory ke folder parent
    os.chdir('../')

# ============================ F16 ========================================
def help():
    # Menampilkan keyword-keyword yang tersedia ke layar
    
    # I.S. sembarang
    # F.S. tercetak list keyword ke layar
    
    # KAMUS LOKAL

    # ALGORITMA
    print("""
============================================================ HELP ============================================================
Berikut merupakan keyword yang dapat digunakan beserta fungsi dan aksesnya
Ketikkan keyword di bawah ini untuk melakukan fungsi yang diinginkan

> \033[1mregister\033[0m       => melakukan registrasi user baru                                                  \033[91m(Akses: Admin)\033[0m
> \033[1mlogin\033[0m          => melakukan login ke dalam program                                                \033[91m(Akses: Admin/User)\033[0m
> \033[1mcarirarity\033[0m     => mencari gadget berdasarkan rarity yang diinputkan                               \033[91m(Akses: Admin/User)\033[0m
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
> \033[1mgacha\033[0m          => menggacha consumable yang ada di inventory untuk mendapatkan consumable baru    \033[91m(Akses: User)\033[0m
> \033[1mhelp\033[0m           => memberikan panduan penggunaan sistem                                            \033[91m(Tidak perlu login)\033[0m
> \033[1mexit\033[0m           => keluar dari program                                                             \033[91m(Tidak perlu login)\033[0m
          """)

# ============================ F17 ========================================
def exit():
    # Menutup dan keluar dari program
    # I.S. program sedang berjalan
    # F.S. program ditutup dan selesai

    # KAMUS LOKAL
    # isSave : string

    # global variable
    global program

    # Function / Procedure
    # validasiYN(jawaban : string) -> boolean
    # Memvalidasi input dari user, harus 'Y' atau 'N'
    # I.S. string terdefinisi
    # F.S. mengembalikan True jika string adalah 'Y' atau 'N' dan False jika sebaliknya

    # save()
    # Menyimpan data ke dalam file di folder yang diinputkan
    # I.S. user, gadget, consumable, gadget_borrow_history, gadget_return_history, consumable_history, inventory_user terdefinisi
    # F.S. file user, gadget, consumable, gadget_borrow_history, gadget_return_history, consumable_history, inventory_user tersimpan

    # ALGORITMA
    if hasLogin:
        isSave = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (Y/N) ")
        while not validasiYN(isSave):
            isSave = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (Y/N) ")
        if isSave == "Y":
            save()
    print()
    print("Terima kasih telah menggunakan kantong ajaib ^_^")
    # Menghentikan program
    program = False

# ============================ FB01 ========================================
def hashing(str):
    # Melakukan hashing pada password dengan metode RollingHash yang bersifat satu arah
    # input -> str : string
    # output -> integer
    
    # I.S. string password terdefinisi
    # F.S. string password telah dilakukan hashing
    
    # KAMUS LOKAL
    # P, m, powerOfP, hashed, i : integer
    
    # ALGORITMA
    P = 101
    m = 1e9 + 1
    powerOfP = 1
    hashed = 0
    for i in range(len(str)):
        hashed = ((hashed + (ord(str[i]) - ord('!') + 1) * powerOfP) % m) 
        powerOfP = (powerOfP * P) % m
    return int(hashed)

# ============================ FB03 ========================================
def seed():
    # Mendapatkan seed berdasarkan time.time() (jumlah detik sejak 1 januari 1970) untuk prosedure rand()
    # I.S. random terdefinisi
    # F.S. random diubah nilainya sesuai time.time()
    
    # KAMUS LOKAL
    # random : integer
    
    # Variable global
    global random
    
    # ALGORITMA
    random = round(time.time())

def rand():
    # Menghasilkan angka acak yang akan digunakan untuk gacha
    # I.S. random terdefinisi
    # F.S. dikembalikan random yang nilainya diubah menjadi angka acak baru
    
    # KAMUS LOKAL
    # a, c, m : integer
    
    # Variable global
    global random
    
    # ALGORITMA
    a = 47071034
    c = 22206856
    m = 87635214759
    random = (a*random + c) % m
    return random

def chance(lstRarity,rarity):
    # Menghasilkan array peluang untuk mendapatkan rarity tertentu berdasarkan rarity consumable yang digunakan untuk gacha
    # input ->  lstRarity : array of float
    #           rarity : character
    # output -> array of float
    
    # I.S. lstRarity dan rarity terdefinisi
    # F.S. dikembalikan lstRarity yang nilainya telah diubah
    
    # KAMUS LOKAL
    # sumN : float
    
    # ALGORITMA
    if rarity == 'C':
        lstRarity[0] += 90.0
        lstRarity[1] += 10.0
    elif rarity == 'B':
        lstRarity[0] += 10.0
        lstRarity[1] += 80.0
        lstRarity[2] += 10.0
    elif rarity == 'A':
        lstRarity[1] += 10.0
        lstRarity[2] += 80.0
        lstRarity[3] += 10.0
    else:
        lstRarity[2] += 10.0
        lstRarity[3] += 90.0
    
    # Menjadikan total peluang tetap 100 persen
    sumN = 0
    for i in range(4):
        sumN += lstRarity[i]
    for i in range(4):
        lstRarity[i] = lstRarity[i] * 100 / sumN
    return lstRarity

def hasilGacha(lstChance):
    # Mengembalikan rarity berdasarkan array peluang
    # input -> lstChance : array of float
    # output -> character
    
    # I.S. lstChance terdefinisi
    # F.S. dikembalikan rarity yang didapatkan secara acak berdasarkan array peluang
    
    # KAMUS LOKAL
    # random, i : integer

    # Function / Procedure
    # seed()
    # Mendapatkan seed berdasarkan time.time() (jumlah detik sejak 1 januari 1970) untuk prosedure rand()
    # I.S. random terdefinisi
    # F.S. random diubah nilainya sesuai time.time()
    
    # rand()
    # Menghasilkan angka acak yang akan digunakan untuk gacha
    # I.S. random terdefinisi
    # F.S. dikembalikan random yang nilainya diubah menjadi angka acak baru

    # ALGORITMA
    seed()
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
    # Mendapatkan consumable baru yang rarity-nya mungkin lebih tinggi / lebih rendah
    # I.S. list lstChance, dan data inventory_user, consumable_history, consumable terdefinisi
    # F.S. User mendapatkan consumable baru
    
    # KAMUS LOKAL
    # count, urutan, digunakan, urutanInventory, jumlah : integer
    # IDInventory : array of string
    # digunakanBenar, jumlahBenar,finished : boolean
    # perintah, rarity : character
    # tambah_con_history : data_consumable_history 
    # tambah_inventory : data_inventory_user
    # perintah : string
    
    # Variable global
    global lstChance
    global inventory_user
    global consumable_history
    global consumable
    
    # Function / Procedure
    # cariData(data)
    # Mencari "dicari" di dalam data berdasarkan index kolomnya
    # I.S. data, dicari, dan index terdefinisi
    # F.S. dikembalikan index baris dimana "dicari" berada pada data

    # cariID(data : any of data_user or data_gadget or data_consumable or data_gadget_return_history or data_gadget_borrow_histroy or 
    #                   data_consumable_history or data_inventory_user, ID : string) -> integer
    # Mencari index dimana ID adaa pada data
    # I.S. data dan ID terdefinisi
    # F.S. dikembalikan index dimana ID berada pada data

    # Bold(text : string) -> string
    # Mengubah text menjadi terlihat bold jika di-print
    # I.S. text terdefinisi
    # F.S. text diberi 'kode' yang jika di-print text menjadi terlihat bold

    # chance(lstRarity : array of float, rarity : character) -> array of float
    # Menghasilkan array peluang untuk mendapatkan rarity tertentu berdasarkan rarity consumable yang digunakan untuk gacha
    # I.S. lstRarity dan rarity terdefinisi
    # F.S. dikembalikan lstRarity yang nilainya telah diubah

    # validasiYN(jawaban : string) -> boolean
    # Memvalidasi input dari user, harus 'Y' atau 'N'
    # I.S. string terdefinisi
    # F.S. mengembalikan True jika string adalah 'Y' atau 'N' dan False jika sebaliknya

    # hasilGacha(lstChance : array of float) -> character
    # Mengembalikan rarity berdasarkan array peluang
    # I.S. lstChance terdefinisi
    # F.S. dikembalikan rarity yang didapatkan secara acak berdasarkan array peluang

    # ALGORITMA
    print()
    print("========INVENTORY========")
    count = 0
    IDInventory = []
    for i in range(len(inventory_user)):
        if inventory_user[i][0] == idUser:
            count += 1
            urutan = cariID(consumable,inventory_user[i][1])
            print(str(count) + ". " + consumable[urutan][1] + "(Rarity " + consumable[urutan][4] + ") (" + str(inventory_user[i][2]) + ")")
            IDInventory.append(inventory_user[i][1])
    if count == 0:
        print("Anda tidak mempunyai consumable di inventory Anda")
        print("=========================")
        print()
        return
    print("=========================")
    print()
    
    # Validasi consumable yang digunakan
    digunakanBenar = False
    while not digunakanBenar:
        try:
            digunakan = int(input("Pilih consumable yang mau digunakan: "))
            if digunakan > count:
                print("Input anda tidak valid")
                print()
            else:
                digunakanBenar = True
        except:
            ValueError
            print("Pilihan harus berupa bilangan bulat")
            print()
    urutanInventory = cariData(inventory_user,IDInventory[digunakan-1],1)

    # Validasi jumlah consumable yang digunakan
    jumlahBenar = False
    while not jumlahBenar:
        try:
            jumlah = int(input("Jumlah yang digunakan: "))
            if jumlah > inventory_user[urutanInventory][2]:
                print("Jumlah yang diinputkan terlalu banyak")
                print()
            else:
                jumlahBenar = True
        except:
            ValueError
            print("Pilihan harus berupa bilangan bulat")
            print()

    # Mengubah data consumable, dan inventory_user
    urutan = cariID(consumable,IDInventory[digunakan - 1])
    consumable[urutan][3] += jumlah
    inventory_user[urutanInventory][2] -= jumlah
    if inventory_user[urutanInventory][2] == 0:
        inventory_user.pop(urutanInventory)
    print(Bold(consumable[urutan][1]) + " (" + Bold("x" + str(jumlah)) + ") ditambahkan!")
    
    # Menampilkan peluang per rarity ke layar
    lstChance = chance(lstChance,consumable[urutan][4])
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
    
    perintah = input("Tambahkan item lagi? (Y/N): ")
    # Validasi perintah
    while not validasiYN(perintah):
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
                    tambah_con_history = ["CH" + str(len(consumable_history)),idUser,consumable[i][0],datetime.date.today().strftime("%d/%m/%Y"),consumable[i][3]]
                    consumable_history.append(tambah_con_history)
                    tambah_inventory = [idUser,consumable[i][0],consumable[i][3]]
                    inventory_user.append(tambah_inventory)
                    consumable[i][3] = 0
                    lstChance = [0,0,0,0]
                    finished = True
                    return
            # Bila tidak ada data consumable yang memiliki rarity seperti yang didapatkan
            rarity = hasilGacha(lstChance)

# ============================ FUNGSI TAMBAHAN ========================================
def Bold(string):
    # Mengubah text menjadi terlihat bold jika di-print
    # input -> string : string
    # output -> string
    
    # I.S. text terdefinisi
    # F.S. text diberi 'kode' yang jika di-print text menjadi terlihat bold
    
    # KAMUS LOKAL
    # hasil : string
    
    # ALGORITMA
    hasil = "\033[1m" + string + "\033[0m"
    return hasil

def cariID(data,ID):
    # Mencari index dimana ID adaa pada data
    # input ->  data : any of data_user or data_gadget or data_consumable or data_gadget_return_history or data_gadget_borrow_histroy or 
    #                   data_consumable_history or data_inventory_user
    #           ID : string
    # output -> integer

    # I.S. data dan ID terdefinisi
    # F.S. dikembalikan index dimana ID berada pada data 
    
    # KAMUS LOKAL
    # i : integer
    
    # ALGORITMA
    for i in range(len(data)):
        if data[i][0] == ID:
            return i

def IDItemAda(data,ID):
    # Mengecek apakah ID ada pada data
    # input ->  data : any of data_user or data_gadget or data_consumable or data_gadget_return_history or data_gadget_borrow_histroy or 
    #                   data_consumable_history or data_inventory_user
    #           ID : string
    # output -> boolean
    
    # I.S. data dan ID terdefinisi
    # F.S. Mengembalikan True jika ID item ada di data dan False jika sebaliknya
    
    # KAMUS LOKAL
    # Ada : boolean
    # i : integer
    
    # ALGORITMA
    Ada = False
    for i in range(len(data)):
        if data[i][0] == ID:
            return True
    return False

def cariData(data,dicari,index):
    # Mencari "dicari" di dalam data berdasarkan index kolomnya
    # input ->  data : any of data_user or data_gadget or data_consumable or data_gadget_return_history or data_gadget_borrow_histroy or 
    #                   data_consumable_history or data_inventory_user
    #           ID : string
    #           index : integer
    # output -> integer

    # I.S. data, dicari, dan index terdefinisi
    # F.S. dikembalikan index baris dimana "dicari" berada pada data
    
    # KAMUS LOKAL
    # i : integer
    
    # ALGORITMA
    for i in range(len(data)):
        if data[i][index] == dicari:
            return i

def colorRed(text):
    # Mengembalikan string menjadi string berwarna merah jika di-print
    # input -> text : string
    # output -> string
    
    # I.S. text terdefinisi
    # F.S. text diberi 'kode' yang jika di-print text menjadi terlihat merah
    
    # KAMUS LOKAL
    
    # ALGORITMA
    return '\033[91m' + text + '\033[0m'

def validasiYN(string):
    # Memvalidasi input dari user, harus 'Y' atau 'N'
    # input -> string : string
    # output -> boolean
    
    # I.S. string terdefinisi
    # F.S. mengembalikan True jika string adalah 'Y' atau 'N' dan False jika sebaliknya
    
    # KAMUS LOKAL
    
    # ALGORITMA
    if (string == 'Y') or (string == 'N'):
        return True
    else:
        print("Jawaban harus 'Y' atau 'N' ")
        print()
        return False

def tglValid(date):
    # Mengembalikan True juka date valid sesuai format DD/MM/YYYY, dan False jika sebaliknya
    # input -> date : string
    # output -> boolean
    
    # I.S. date terdefinisi
    # F.S. dikembalikan True jika format date benar, dan False jika salah
    
    # KAMUS LOKAL
    # date_format : string
    
    # ALGORITMA
    date_format = '%d/%m/%Y'
    if len(date) == 10:
        try:
            datetime.datetime.strptime(date, date_format)
            return True
        except ValueError:
            return False
    else:
        return False



# ============================== MAIN PROGRAM =======================================

# KAMUS GLOBAL
# type data_user : <id: string, username: string, nama: string, alamat: string, password: integer, role: string>
# type data_gadget : <id:string, nama: string; deskripsi: string; jumlah: integer; rarity: character; tahun_ditemukan: integer>
# type data_consumable : <id: string; nama: string; deskripsi: string; jumlah: integer; rarity: character>
# type data_gadget_borrow_history : <id: string; id_peminjam: string; id_gadget: string; tanggal_peminjaman: string; jumlah: integer; is_returned: boolean>
# type data_gadget_return_history : <id: string; id_peminjaman: string; tanggal_pengembalian: string; jumlah_pengembalian: integer; applicable_or_not: string>
# type data_consumable_history : <id: string; id_pengambil: string; id_consumable: string; tanggal_pengambilan: string; jumlah: integer>
# type data_inventory_user : <id_user: string; id_consumable: string; jumlah_yang_dipunyai: integer>

# user : array of data_user
# gadget : array of data_gadget 
# consumable : array of data_consumable
# consumable_history : array of data_consumable_history 
# gadget_borrow_history : array of data_gadget_borrow_history
# gadget_return_history : array of data_gadget_return_history
# inventory_user : array of data_inventory_user
# idUser, directory, perintah : string
# random : integer
# lstChance : array of float
# lstPerintah : array of string
# program, isAdmin, hasLogin : boolean

# INISIALISASI
user =[]; gadget = []; consumable = []; consumable_history = []; gadget_borrow_history = []; gadget_return_history = []; inventory_user = []
idUser = ""; random=0; lstChance = [0.0,0.0,0.0,0.0]
lstPerintah = ['register', 'login', 'carirarity', 'caritahun', 'tambahitem', 'hapusitem', 'ubahjumlah', 'pinjam', 
               'kembalikan', 'minta', 'riwayatpinjam', 'riwayatkembali', 'riwayatambil', 'save', 'help', 'gacha']
program = True
hasLogin = False
isAdmin = False

# Pemanggilan procedure loading()
directory = loading()

if not(directory == None):
    print("Loading...")
    time.sleep(2)
    load(directory)
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

    # Jalannya program utama
    while (program):
        print(colorRed(">>> "),end='')
        perintah = input()
        if perintah == "help":
            help()
        elif perintah == "login":
            if hasLogin:
                print(colorRed("Anda sudah login, exit terlebih dahulu untuk menggunakan akun lain"))
                print()
            else:
                login()
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
        elif perintah == "exit":
            # Asumsi exit tidak perlu login
            exit()
        else:
            if hasLogin:
                if perintah == "register":
                    if isAdmin:
                        register()
                    else:
                        print("Maaf, hanya boleh diakses oleh admin ^_^")
                        print()
                elif perintah == "carirarity":
                    cariRarity()
                elif perintah == "caritahun":
                    caritahun()
                elif perintah == "tambahitem":
                    if isAdmin:
                        tambahItem()
                    else:
                        print("Maaf, hanya boleh diakses oleh admin ^_^")
                        print()
                elif perintah == "hapusitem":
                    if isAdmin:
                        hapusItem()
                    else:
                        print("Maaf, hanya boleh diakses oleh admin ^_^")
                        print()
                elif perintah == "ubahjumlah":
                    if isAdmin:
                        ubahjumlah()
                    else:    
                        print("Maaf, hanya boleh diakses oleh admin ^_^")
                        print()
                elif perintah == "pinjam":
                    if not isAdmin:
                        pinjam()
                    else:
                        print("Maaf, hanya boleh diakses oleh user ^_^")
                        print()
                elif perintah == "kembalikan":
                    if not isAdmin:
                        kembalikan()
                    else:
                        print("Maaf, hanya boleh diakses oleh user ^_^")
                        print()
                elif perintah == "minta":
                    if not isAdmin:
                        mintaConsumable()
                    else:
                        print("Maaf, hanya boleh diakses oleh user ^_^")
                        print()
                elif perintah == "riwayatpinjam":
                    if isAdmin:
                        riwayatPinjam()
                    else:
                        print("Maaf, hanya boleh diakses oleh admin ^_^")
                        print()
                elif perintah == "riwayatkembali":
                    if isAdmin:    
                        riwayatKembali()
                    else:
                        print("Maaf, hanya boleh diakses oleh admin ^_^")
                        print()
                elif perintah == "riwayatambil":
                    if isAdmin:
                        riwayatConsumable()
                    else:
                        print("Maaf, hanya boleh diakses oleh admin ^_^")
                        print()
                elif perintah == "save":
                    save()
                elif perintah == "gacha":
                    if not isAdmin:
                        gacha()
                    else:
                        print("Maaf, hanya boleh diakses oleh user ^_^")
                        print()
                else:
                    # Masukan salah, tidak sesuai keyword yang valid, sudah login
                    print(colorRed("Input anda tidak valid"))
                    print("Berikut merupakan input yang valid")
                    help()        
            elif perintah in lstPerintah:
                # Masukan benar, tetapi belum login
                print(colorRed("Anda harus login terlebih dahulu"))
                print()
            else:
                # Masukan salah, tidak sesuai keyword yang valid, belum login
                print(colorRed("Input yang diberikan tidak tersedia"))
                print()
