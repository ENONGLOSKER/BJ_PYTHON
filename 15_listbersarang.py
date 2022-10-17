from ast import ImportFrom


print (8*"=","LIST BERASARANG",8*"=" ,"\n")
data1 = [1,2,3]
data2 = [6,5,4]
data = [data1,data2]

print(data,"\n")

klp1 = ['al',204855113,'ti']
klp2 = ['el',204855114,'si']
klp3 = ['zq',204855115,'tk']

kelompok = [klp1,klp2,klp3]
info = kelompok.copy()

info[0] [0] = 'za' 

print(hex(id(kelompok)))
print(hex (id(info)))

print(kelompok)
print(info,"\n")

# for info in kelompok:
#     print(f"NAMA : {info [0]}")
#     print(f"NIM  : {info [1]}")
#     print(f"PRODI: {info [2]}\n")

#mengambil data
data = kelompok [0] #data 1
print("DATA KE 1 : ",data)
data = kelompok [0] [1]  #data 1 dg index 2
print("DATA DENGAN INDEX :",data)

print(25*"=")
from copy import deepcopy #var = deepcopy(list)

kelompok = [klp1,klp2,klp3]
info_deep = deepcopy(kelompok)

print(hex(id(kelompok)))
print(hex (id(info_deep)))

print(hex(id(kelompok[0])))
print(hex (id(info_deep[0])))

kelompok[0] [0] = 'zs'

print(kelompok)
print(info)
print(info_deep,"\n")



