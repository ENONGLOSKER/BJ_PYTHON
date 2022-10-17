#input() = mengambil masukan/inputan dari luar
data_a = input("masukan data teks :")
print("data =",data_a,type(data_a))

#jika mengambil angka, harus dicasting ke int atau  float
data_1 = int(input("masukan data angka :"))
print("data =",data_1,type(data_1))

#jika mengambil biner, harus dicasting ke boolean kemudian int
data_01 = bool(int(input("masukan data biner :")))
print("data =",data_01,type(data_01))