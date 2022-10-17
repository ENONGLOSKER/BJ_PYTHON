class pahlawan:
    def __init__(self,nama,kekuatan,kesehatan):
        #encapsulation : membuat variabel privat
        self.__nama = nama
        self.__kekuatan = kekuatan
        self.__kesehatan = kesehatan

        #getter : mengambil variabel
    def getNama (self): #mengakases1
        return self.__nama
    def getKesehatan(self):
        return self.__kesehatan
    def serangan(self,serang):
        self.__kesehatan -= serang
    
        #setter : mengeset variabel
    def setKekuatan(self,kekuatanku):
        self.__kekuatan=kekuatanku


hero1 = pahlawan("elqusairi",190,290)
print(hero1.__dict__)
print(hero1.getNama())#mangkases2

hero1.serangan(10)
print(hero1.getKesehatan())





        