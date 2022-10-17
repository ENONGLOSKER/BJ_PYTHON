#komparasi = perbandingan yang bernilai boolean
from ast import IsNot
from operator import is_not


a = int(input("masukan nilai 1 :"))
b = int(input("masukan nilai 2 :"))

# operasi
hasil = a < b
print("< : ",hasil)

hasil = a > b
print("> : ",hasil)

hasil = a <= b
print("<= : ",hasil)

hasil = a >= b
print(">= : ",hasil)

hasil = a == b
print("== : ",hasil)

hasil = a != b
print("!= : ",hasil)

print()

#perator identity = membadingkan alamat memori / objek
z = int(input("msukan nilai 1 :"))
q = int(input("msukan nilai 2 :"))

print()
print(z,"alamatnya = ",hex(id(z)))
print(q,"alamatnya = ",hex(id(q)))
print()

alamat1 = z is q
alamat2 = z is not q
print("nilai is =", alamat1)
print("nilai is not =", alamat2)