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
"""
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
"""
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--foo")
parser.add_argument("-b", "--bar")
args = parser.parse_args()
if args.foo is None:
    print("gaada foo")

if args.foo and args.bar is None:
    parser.error("--foo requires --bar. You did not specify bar.")

print ("foo =", args.foo)
print ("bar =", args.bar)