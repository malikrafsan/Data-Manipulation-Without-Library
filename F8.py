def pinjam():
    '''Validasi ID_Item'''
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
        except ValueError:
            print()
    
    personal_borrow = []
    for a in range(len(gadget_borrow_history)):
        if gadget_borrow_history[a][1] == idUser:
            personal_borrow.append(gadget_borrow_history[a])
    
    '''Cek apakah user pernah meminjam dan belum mengembalikan gadget yang sama'''
    syarat_terpenuhi_1 = False
    for i in range(len(personal_borrow)-1, 0, -1):
        if personal_borrow[i][2] == id_item:
            if personal_borrow[i][5] == True:
                syarat_terpenuhi_1 = True
                break
    
    check = None
    for i in range(len(personal_borrow)):
        if personal_borrow[i][2] == id_item:
            check = 'Checked'
    
    if syarat_terpenuhi_1 == True or check == None:
        '''Validasi Tanggal'''
        format = "%d/%m/%Y"
    
        while(True):
            date_string = input("Tanggal peminjaman: ").strip()
        
            try:
                datetime.datetime.strptime(date_string, format)
                break
            except ValueError:
                print("Tanggal yang anda masukan salah. Silahkan masukan kembali tanggal dengan format DD/MM/YYYY")
            
        '''Validasi jumlah'''
        current_amount = gadget[indeks][3]
        terms = True
    
        while(terms):
            try:
                amount = int(input("Jumlah peminjaman: "))
        
                if (amount <= current_amount) and (amount > 0):
                    gadget[indeks][3] = current_amount - amount
                    print(f"Item {gadget[indeks][1]} (x{amount}) berhasil dipinjam!")
                    terms = False
                else:
                    print(f"Jumlah yang anda ingin pinjam melebihi yang ada dalam stok penyimpanan atau anda memasukan angka di bawah 1. Silahkan masukan kembali jumlah yang ingin dipinjam dengan maksimal meminjam {current_amount}")
            except ValueError:
                print("Silahkan masukan kembali jumlah dengan angka yang benar")
    
        '''Memasukan ke data gadget_borrow_history'''
        id_peminjaman = 'GBH' + str(len(gadget_borrow_history))
    
        gadget_borrow_history.append([id_peminjaman, idUser, id_item, date_string, amount, False])
    else:
        print("Maaf, anda pernah meminjam gadget yang sama dan belum mengembalikannya")
