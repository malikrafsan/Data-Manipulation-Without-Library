def caritahun():
  while True:
      try:
        tahun = int(input("Masukkan tahun: "))
        kategori = input("Masukkan kategori: ")
        found = False

        print()
        print("Hasil pencarian: ")
        print()
        
        if kategori == "=":
          for i in range(1,len(gadget)):
            if gadget[i][5] == tahun:
              print(f"Nama: {gadget[i][1]}")
              print(f"Deskripsi: {gadget[i][2]}")
              print(f"Jumlah: {gadget[i][3]}")
              print(f"Rarity: {gadget[i][4]}")
              print(f"Tahun Ditemukan: {gadget[i][5]}")
              print()
              found = True
        elif kategori == "<":
          for i in range(1, len(gadget)):
            if gadget[i][5] < tahun:
              print(f"Nama: {gadget[i][1]}")
              print(f"Deskripsi: {gadget[i][2]}")
              print(f"Jumlah: {gadget[i][3]}")
              print(f"Rarity: {gadget[i][4]}")
              print(f"Tahun Ditemukan: {gadget[i][5]}")
              print()
              found = True
        elif kategori == ">":
          for i in range(1, len(gadget)):
            if gadget[i][5] > tahun:
              print(f"Nama: {gadget[i][1]}")
              print(f"Deskripsi: {gadget[i][2]}")
              print(f"Jumlah: {gadget[i][3]}")
              print(f"Rarity: {gadget[i][4]}")
              print(f"Tahun Ditemukan: {gadget[i][5]}")
              print()
              found = True
        elif kategori == "<=":
          for i in range(1, len(gadget)):
            if gadget[i][5] <= tahun:
              print(f"Nama: {gadget[i][1]}")
              print(f"Deskripsi: {gadget[i][2]}")
              print(f"Jumlah: {gadget[i][3]}")
              print(f"Rarity: {gadget[i][4]}")
              print(f"Tahun Ditemukan: {gadget[i][5]}")
              print()
              found = True
        elif kategori == ">=":
          for i in range(1, len(gadget)):
            if gadget[i][5] >= tahun:
              print(f"Nama: {gadget[i][1]}")
              print(f"Deskripsi: {gadget[i][2]}")
              print(f"Jumlah: {gadget[i][3]}")
              print(f"Rarity: {gadget[i][4]}")
              print(f"Tahun Ditemukan: {gadget[i][5]}")
              print()
              found = True
        if found == False:
              print("Tidak ada gadget yang ditemukan")
      except ValueError:
        print()
      else:
        break
