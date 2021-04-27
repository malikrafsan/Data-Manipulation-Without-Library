def mintaConsumable():
    ID = input("Masukkan ID item: ")
    jumlah = int(input("Jumlah: "))
    # validasi jumlah
    while (jumlah<=0):
        print("Masukan tidak valid!")
        jumlah = int(input("Jumlah: "))
    valid_date = False
    # validasi tanggal
    while not valid_date:
        tanggal = input("Tanggal permintaan: ")
        try:
            datetime.datetime.strptime(tanggal, '%d/%m/%Y')
            valid_date = True
        except ValueError:
            valid_date = False
            print("Masukan tidak valid!")
    global isAvailable
    isAvailable = False
    consumabledata1 = load_data("consumable.csv")
    consumabledata = consumabledata1[1]
    #print(consumabledata)
    for consumable in consumabledata :
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
                save_data("comsumable_history")
