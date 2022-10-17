def operasi (*arg): #tidak harus arg tpi boleh yang lain
    hasil = 0
    for angka in arg:
        hasil += angka

    return hasil

output = operasi (1,2,2,2,2,2) #*arg : dapat mengisi dg argumen yang banyak
print(f"jumlah : {output}")

#kwargs
def fungsi(**kwargs):
    print(kwargs['nim']) #memanggil dic
    #atau
    nama = kwargs ["nama"]
    nim = kwargs ["nim"]
    hello = kwargs ["hello"]
    print(nama,nim, hello)

fungsi(nama = 'elqusairi',nim = 132321, hello = 'tess') #argumen berupa dictionary