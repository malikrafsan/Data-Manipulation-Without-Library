def modify_data(data, idx, col, value):
    data[idx][col] = value
    return data

def load_data(file):
    f = open(file,"r")
    raw_lines = f.readlines()
    f.close()
    lines = [raw_line.replace("\n", "") for raw_line in raw_lines]
    lstAll = []
    for line in lines:
        lst = []
        data =""
        for i in range(len(line)):
            if line[i] == ';':
                try:
                    data = int(data)
                except:
                    ValueError
                lst.append(data)
                data = ""
            elif (i == len(line) - 1):
                lst.append(data + line[i])
            else:
                data += line[i]
        lstAll.append(lst)
    return lstAll

# ===================================================

def load(): 
    user = load_data("user.csv")
    gadget = load_data("gadget.csv")
    
    return user,gadget

# =================================================
def save_data(file,data):
    f = open(file, "w") 
    f.write(data)
    f.close()

def save(user,gadget):
    save_data("user.csv",user)
    save_data("gadget.csv",gadget)

def convert_datas_to_string(file):
    string_data = ""
    for arr_data in file:
        arr_data_all_string = [str(var) for var in arr_data]
        string_data += ";".join(arr_data_all_string)
        string_data += "\n"
    return string_data

# ==========================================================
def register(user):
    nama = input("Masukkan nama: ")
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")
    alamat = input("Masukkan alamat: ")
    
    id_user = "U" + str(len(user))
    
    register = [[id_user,username,nama,alamat,password,"User"]]

    user += register
    print(user)
    print("User", username, "telah berhasil register ke dalam Kantong Ajaib.")

user, gadget = load()
print(user)
#user = modify_data(user,1,1,"tetot")
#register()
#user = convert_datas_to_string(user)
#save_data("testing.csv",user)


# load()
# modify_data(user,1,1,"tetot")
# print(user)
# save()