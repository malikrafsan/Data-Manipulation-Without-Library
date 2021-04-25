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
