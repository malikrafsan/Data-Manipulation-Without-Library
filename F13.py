def riwayatConsumable():
    count = 0
    riwayatConsumablePrint(count)

def riwayatConsumablePrint(count):
    consumableSort = sorted(consumable_history[count+1:], key = lamda date: datetime.datetime.strptime(date[3], '%d/%m/%Y'),reverse=True))
    berikutnya = True
    for i in range(5):
        try:
            namaUser = user[cariID(user,consumableSort[i][1])][2]
            namaConsumable = consumable[cariID(consumable,consumableSort[i][2])][1]
            print()
            print(i)
            print("ID Pengambilan       : " + consumableSort[i][1])
            print("Nama Pengambil       : " + namaUser)
            print("Nama Consumable      : " + namaConsumable)
            print("Tanggal Pengembalian : " + consumableSort[i][3])
            print("Jumlah               : " + str(consumableSort[i][4]))
        except:
            IndexError
            print()
            print("Data sudah habis")
            berikutnya = False
            break
    if berikutnya and len(consumableSort) != 5:
        print()
        next = input("Apakah mau ditampilkan data lebih lanjut? (Y/N) ")
        if next == 'Y':
            count += 5
            riwayatConsumablePrint(count)