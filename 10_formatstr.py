kata = "hello gaes"
angka = 132321

print("------------------ cara 1")
print("elq :", kata)
print("code : " + str(angka))
print("------------------ cara 2")
print(f"elq : {kata}")
print(f"code : {angka}")

#format uang
print(f"ribu = {angka:,}")
angka = 132321000
print(f"juta = {angka:,} \n")

#angka
angka = 132
print(angka)
biner = f"dalam biner = {bin(angka)}"
oktal = f"dalam oktal = {oct(angka)}"
hexsa = f"dalam hexsa = {hex(angka)}"

print(biner)
print(oktal)
print(hexsa,"\n")

#rata
print(5*"="," MY DATA ",5*"=")
data = f"""
nama = "elqusairi"
alamat = "lokon"
code = "132"
"""
print(data)
