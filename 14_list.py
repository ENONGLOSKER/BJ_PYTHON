
#membuat list
nama = ["el","al","zaenul","qusairi"]

#mengambil isi list
print(nama[1])

data = nama[2]
print(data)

#urutan index, dari awal-akhir: 0 dst atau akhir-awal: -1 dst
print(nama[-1])

#panjang data
print(len(nama))
print("data berjumlah :", len(nama),"buah")

#manipulasi list--------------------------
#menambah dengan urutan yg berbeda
nama.insert(3,"zaenul alqusairi")
print(nama)
#atau menambah di urutan terakhir
nama.append("elqusairi")
print(nama)

#gabung
data = ['a','b','c']
info = nama + data
print(info)
#atau
nama.extend(data)
print(nama)

#mengubah/update
nama [-1] = "data terakhir"
print(nama)

#hapus data
nama.remove("data terakhir")
print(nama)
# nama.remove("EL") #EROR, karena penulisan tidak sesuai antara EL dengan el
# print(nama)
# atau menghapus data terakhir atau tertentu
nama.pop()
print(nama)
# atau menghapus melalui index
nama.pop(-1)
print(nama)

del nama [0]
print(nama)

#list lanjut-----------------------------
#mnghitung jumlah
data = [1,2,2,5,7,9,1,5,0,3,6,8,0,3,1,6,7]
jumlah = data.count(2) #mnghitung jumlah data 1
print(data)
print(jumlah)

#menetukan posisi
posisi = nama.index('zaenul')
print(posisi)

#mengurutkan
data = ['a','f','v','g','h','c']
nilai = [1,2,2,5,7,9,1,5,0,3,6,8,0,3,1,6,7]

print(data)
#dari awal-akhir
data.sort()
print(data)
#dari akkhir-awal
data.reverse()
print(data)
print("urutan awa-akhir dan akhir-awal")
#dari awal-akhir
print(nilai)

nilai.sort()
print(nilai)
#dari akkhir-awal
nilai.reverse()
print(nilai)

#copy dan duplicat list
nama = ['el','al','qusairi','elqusairi']
print(nama)

#menyamakan
nm = nama
#mengubah salah satu data, maka pd kedua list akan berubah
nm[0]='ws'
print(hex(id(nm)),': alamat list nm')
print(hex(id(nama)),': alamat list nama')

print(nama)
print(nm)
#untuk menduplikat data dengan tanpa mempengaruhi data pada list sebelumnya

baru = nama.copy()
print(hex(id(baru)),': alamat list baru\n')
#merubah data
baru[0] = 'zaenul'
nm [0] ='qusairi'

print(nama)
print(nm)
print(baru)
