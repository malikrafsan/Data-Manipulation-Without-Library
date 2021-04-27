"""from datetime import datetime

def dateValid(date):
    try:
        datetime.datetime.strptime(date, '%d/%m/%Y')
        return True
    except:
        ValueError
        return False
"""
import datetime
date_string = '2017-12-31'

def tglValid(date):
    date_format = '%d/%m/%Y'
    try:
        datetime.datetime.strptime(date, date_format)
        return True
    except ValueError:
        return False

#tgl = input("Masukkan tanggal: ")
#print(tglValid(tgl))

lst = "register,login,caricarity,caritahun,tambahitem,hapusitem,ubahjumlah,pinjam,kembalikan,minta,riwayatpinjam,riwayatkembali,riwayatambil,save,help,exit"
mir = []
kata = ""
for i in range(len(lst)):
    if lst[i] == ',':
        mir.append(kata)
        kata = ""
    else:
        kata += lst[i]

print(mir)