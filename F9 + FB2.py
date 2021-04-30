def kembalikan():
    # Mengembalikan gadget yang pernah dipinjam
    
    # input/output -> gadget : array of array of string and integer
    # input/output -> gadget_borrow_history : array of array of string, integer, and boolean
    # input/output -> gadget_return_history: array of array of string
    
    # I.S. matriks data gadget, gadget_borrow_history, dan gadget_return_history terdefinisi
    # F.S. jumlah gadget pada data gadget berkurang dan terdapat entri baru pada gadget_borrow_history
    
    # KAMUS LOKAL
    # id_returned_gadget, id_pengembalian : string
    # syaratnya : boolean
    # option, indeksnya, markernya, max_returned, total_amount_returned, total_amount_returned_updated, amount_returned : integer
    
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
        format = "%d/%m/%Y"
    
        while(True):
            tanggal = input("Tanggal pengembalian: ").strip()
        
            try:
                datetime.datetime.strptime(tanggal, format)
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
            except ValueError:
                print(f"Silahkan masukan kembali jumlah {gadget[markernya][1]} yang ingin dikembalikan dengan bilangan bulat")
                
        # Menambahkan entri gadget_return_history
        id_pengembalian = 'GRH' + str(len(gadget_return_history))
        gadget_return_history.append([id_pengembalian, gadget_borrow_history[indeksnya][0], tanggal, amount_returned, 'applicable'])                
        
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