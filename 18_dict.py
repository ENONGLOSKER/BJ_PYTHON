
from distutils.log import info


data = {
    'el':'elqusairi',
    'al':'alqusairi',
    'zq':'zaenul alqusairi'
}

#mengambil
print(data.get('el'))

#update
#jika data ada, menganti nilai
data.update({'el':'el_qusairi'})
print(data)

#jika data tdk ada, menambah
data.update({'elq':'elqusairi'})
print(data)

#delet
del data['el']
print(data)

#perulangan dic

#mengambil key
keys = data.keys()
print(keys)

for key in data.keys():
    print(key)

#mengambil values
nilai = data.values()
print(nilai)

for value in data.values():
    print(value)

#mengambil item
item = data.items()
print(item)

for nomor, nilai in data.items():
    print("key = ",nomor, "values = ",nilai,"\n")

#copy
info = data.copy()
print(f"info ={info}")
print(f"data ={data}\n")

#menghapus item

#menghapus berdasarkan key
daftar = info.pop("zq")

print(f"daftar ={daftar}")#data terhapus
print(f"data ={info}\n")#sisa data

#menghapus berdasarkan item yang terakhir
akhir = info.popitem()

print(f"akhir ={akhir}")#data terhapus
print(f"info ={info}") #sisa data


