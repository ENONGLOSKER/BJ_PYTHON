print('satu kutip')
print("dua kutip")
print('''
tiga kutip:
dengan
fotmat yang sama
''')
print("'dalam satu kutip'")
print(""" 
hello
gaes
...?
 """)

 #KUTIP
print("hari jum'at")
print('hari jum\'at')

#TAMBAHAN
print("C:\\USER\\ELQ")
print("helo gaes \n gimana kabarnya?")
print("lorem \tipsum hfsydfysf bsdhfgys")
print("lorem \bipsum hfsydfysf bsdhfgys\n")
print("------------------------------------------")
e = "el"
l = "qusairi"
#mengabungkan / concat
nama = e + l
print(nama)

#mengambil jumlah karakter
print(len(nama))

#mencari karakter
zaq = "qus"
status = zaq in nama
print("apakah ada karakter "+zaq+" = ",str(status))

#looping 
print(10*"hello😁 ")
print("hello😁 "*10)

#mengambil karakter
print(nama)
print("nilai index ke1 =",nama[2])
print("nilai index ke1 =",nama[0:2])
print("nilai index loncat 2 =",nama[0:9:2])
print("nilai index loncat 2 =",min(nama))
print("nilai index loncat 2 =",max(nama))

#ukuran tex
print(nama)
nama = nama.upper()
print(nama)
nama = nama.lower()
print(nama)

#menukar 
nama = ["zaenul","al","qusairi"]
nama = " ".join(nama)
print(nama)

nama = "zaenul---al---qusairi"
print(nama.split("---"))

#posisi text
#rata kiri
nama = "PROGRAM".ljust(20,)
print("|",nama,"|")
#rata kiri
nama = "PROGRAM".rjust(20,)
print("|",nama,"|")
#rata tengah
nama = " PROGRAM ".center(20,"=")
print("|",nama,"|")

#LEBIH LENGKAP CARI KATA KUNCI : #METHOD STRING