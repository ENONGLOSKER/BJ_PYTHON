# #super clas
# class pahlawan:
#     def __init__(self,nama, kesehatan, kekuatan):
#         self.nama = nama
#         self.kesehatan = kesehatan
#         self.kekutan = kekuatan
# #sub clas
# class hero1(pahlawan):#akan mewarisi sifat dari super klas
#     pass
# class hero2(pahlawan):
#     pass

# #memngakses super klas
# pemain = pahlawan("elqusairi",190,200)
# print("super class (kesehatan)  : ",pemain.kesehatan)

# #memngakses sub klas
# pemain1 = hero1("zaq",800,500)
# print("sub class1 (kesehatan)   : ",pemain1.nama)
# pemain2 = hero2("qaz",900,700)
# print("sub class2 (kesehatan)   : ",pemain2.nama)

# bagian 2

class pahlawan:
    def __init__(self,nama, kesehatan, kekuatan):
        self.nama = nama
        self.kesehatan = kesehatan
        self.kekuatan = kekuatan
    def showinfo(self):
        print("nama : {} , kesehatan : {} , kekuatan : {}".format(self.nama,self.kesehatan,self.kekuatan))

#sub class
class hero1(pahlawan):#akan mewarisi sifat dari super klas
    def __init__(self, nama):#mengambil 1 argumen sisanya langsung di set
        pahlawan.__init__(self,nama, 123, 1443)#superclass.__init__(argumen1,argumen1,nilai1,nilai2)
       

    #atau bisa dengan menggunakan super()
class hero2(pahlawan):
   def __init__(self, nama):#mengambil 1 argumen sisanya langsung di set
       super().__init__(nama, 123, 321)
    #atau dengan cara memanggil fungsi di dalam fungsi
       super().showinfo()

#     #atau bisa dengan menggunakan super()
# class hero3(pahlawan):
#    def __init__(self,nama):#mengambil 1 argumen sisanya langsung di set
#        super().showinfo()
 

#mengakases hero1 dan 2
pemain1 = hero1("ELQUSAIRI")
print(pemain1.nama,pemain1.kesehatan,pemain1.kekuatan)

pemain1 = hero2("ALQUSAIRI")
print(pemain1.nama,pemain1.kesehatan,pemain1.kekuatan)









