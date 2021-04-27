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

tgl = input("Masukkan tanggal: ")
print(tglValid(tgl))
