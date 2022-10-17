#operator logika = digunakan untuk menentukan nilai boolean

satu = True
dua = False

# OR : jika salah satu benar maka bernilai BENAR
hasil1 = satu or dua
hasil2 = satu or satu
hasil3 = dua or dua
hasil4 = dua or satu
print(hasil1,hasil2, hasil3, hasil4)

# AND : jika salah satu salah maka bernilai SALAH
hasil1 = satu and dua
hasil2 = satu and satu
hasil3 = dua and dua
hasil4 = dua and satu
print(hasil1,hasil2, hasil3, hasil4)

# XOR : jika Berbeda/tidak sama maka bernilai BENAR
hasil1 = satu ^ dua
hasil2 = satu ^ satu
hasil3 = dua ^ dua
hasil4 = dua ^ satu
print(hasil1,hasil2, hasil3, hasil4)