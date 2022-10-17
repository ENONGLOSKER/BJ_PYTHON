def data (nilai):
    anggota = nilai.copy()
    for d_anggota in anggota:
        print(f"hello {d_anggota}") 

list_anggota = ["el","al","qu"]
data(list_anggota)

#nilai defoult
def hello (hi = "selamat datang"):
    print(f"hello {hi}")
    return hi

hello( )
hello("el")

#latiahn
def penjumlahan(n1,n2):
    jumlah = n1 + n2
    return jumlah
def pengurangan(n1,n2):
    kurang = n1 - n2
    return kurang
def perkalian(n1,n2):
    kali = n1 * n2
    return kali
def pembagian(n1,n2):
    bagi = n1 / n2
    return bagi