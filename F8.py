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
        amount = int(input("Jumlah peminjaman: "))
        
        if amount <= current_amount:
            gadget[indeks][3] = current_amount - amount
            print(f"Item {gadget[indeks][1]} (x{amount}) berhasil dipinjam!")
            terms = False
        else:
            print(f"Jumlah yang anda ingin pinjam melebihi yang ada dalam stok penyimpanan, anda maksimal meminjam {current_amount}")
    
    '''Memasukan ke data gadget_borrow_history'''
    id_peminjaman = 'GBH' + str(len(gadget_borrow_history))
    
    gadget_borrow_history.append([id_peminjaman, idUser, id_item, date_string, amount])
'''Di gadget_borrow_history nya ada kolom baru tulisannya is_returned (cek di GDocs spek tubes) tapi belum dibuat append bagian kolom is_returned nya'''