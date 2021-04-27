def mintaConsumable():
    next = False
    while not next:
        ID = input("Masukkan ID item: ")
            if (ID[0] == 'G'):
                if IDItemAda(gadget,ID):
                    next = True
                else:
                    print("ID tidak valid!")
            elif (ID[0] = 'C'):
                if IDItemAda(consumable,ID):
                    next = True
                else:
                    print("ID tidak valid!")
            else:
                print("ID tidak valid!")
    # validasi ID
    jumlah = int(input("Jumlah: "))
    while (jumlah<=0):
        print("Masukan tidak valid!")
        jumlah = int(input("Jumlah: "))
    # validasi jumlah
    valid_date = False
    while not valid_date:
        tanggal = input("Tanggal permintaan: ")
        try:
            datetime.datetime.strptime(tanggal, '%d/%m/%Y')
            valid_date = True
        except ValueError:
            valid_date = False
            print("Masukan tidak valid!")
    # validasi tanggal
    isAvailable = False
    consumable = consumabledata[1]
    #print(consumabledata)
    for consumable in consumabledata:
        if consumable[0] == iditem :
            isAvailable = True
            iditem = consumable[1]
    if isAvailable == False:
        print("Tidak ada Consumable ditemukan")
    else :
        for consumable in consumabledata :
            if int(consumable[3]) < Jumlah or (int(consumable[3]) - Jumlah) <= 0 :
                print("Masukkan tidak valid!")
            else:
                print("")
                print(f"Item {ID} (x{jumlah}) telah berhasil diambil!")
