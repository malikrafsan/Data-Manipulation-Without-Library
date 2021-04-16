def mintaConsumable():
    ID = input("Masukkan ID item: ")
    jumlah = input("Jumlah: ")
    tanggal = input("Tanggal permintaan: ") #belum divalidasi
    arrMintaConsumable = [ID,jumlah,tanggal]
    consumable.append(arrMintaConsumable)
    print("")
    print(f"Item {ID} (x{jumlah}) telah berhasil diambil!")