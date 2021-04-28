def kembalikan():
    '''Fungsinya belum pake yang pengembalian sebagian, jadi fungsi bonus yg FB02 belum terealisasi, nanti dicoba dulu, kalau bisa nanti diupdate, kalau engga berarti pake F09 tanpa bonus'''
    # Menampilkan ke user gadget yang pernah ia pinjam, asumsi user pasti pernah meminjam barang
    personal_borrow_not_returned = []
    for a in range(len(gadget_borrow_history)):
        if gadget_borrow_history[a][1] == idUser and gadget_borrow_history[a][5] == False:
            personal_borrow_not_returned.append(gadget_borrow_history[a][2])
            
    unique_personal_borrow_not_returned = set(personal_borrow_not_returned)
    updated_unique_personal_borrow_not_returned = list(unique_personal_borrow_not_returned)
    
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
            
    # Meminta user memasukan tanggal        
    format = "%d/%m/%Y"
    
    while(True):
        tanggal = input("Tanggal pengembalian: ").strip()
        
        try:
            datetime.datetime.strptime(tanggal, format)
            break
        except ValueError:
            print("Tanggal yang anda masukan salah. Silahkan masukan kembali tanggal dengan format DD/MM/YYYY")
            
    # Mengupdate jumlah gadget:
    id_returned_gadget = updated_unique_personal_borrow_not_returned[option - 1]
    
    for z in range(len(gadget_borrow_history)-1, 0, -1):
        if gadget_borrow_history[z][2] == id_returned_gadget and gadget_borrow_history[z][1] == idUser:
            gadget_borrow_history[z][5] = True
            indeksnya = z
            break
            
    for n in range(len(gadget)):
        if gadget[n][0] == id_returned_gadget:
            gadget[n][3] = gadget[n][3] + gadget_borrow_history[z][4]
            markernya = n
            break
         
    # Menampilkan jika berhasil       
    print(f"Item {gadget[markernya][1]} (x{gadget_borrow_history[z][4]}) telah dikembalikan")
    
    # Menambahkan gadget_return_history
    id_pengembalian = 'GRH' + str(len(gadget_return_history))
    gadget_return_history.append([id_pengembalian, gadget_borrow_history[z][0], tanggal])
