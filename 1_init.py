#CLASS OBJEK METHOD
class hello: #class
    jmlh = 1
    #init :mejik kyword
    def __init__(self,nama,nim):
        #instance
        self.nama=nama
        self.nim =nim
        hello.jmlh += 1
    #str
    def __str__(self):
        return f"{self.nama}({self.nim})"
    #methode tanpa argumen
    def sapa1(self):
        print("hai..",self.nama)
    #method dengan argumen
    def sapa2(self,n):
        self.nim += n
    #method dengan return
    def sapa3(self):
        return self.nim

# nm1 = hello('3lqu6a1r1',343243) 
# print(nm1.nama)
# print(nm1.jmlh)
# nm2 = hello('3lqu6a1r1',343243) 
# print(nm2.nama)
# print(nm2.jmlh)
# nm3 = hello('3lqu6a1r1',343243) 
# print(nm2.jmlh)

nm = hello("elqusairi",123231)

nm.sapa1() #mathod tanpa argumen
nm.sapa2(11)
print(nm.nim)#methode dg argumen
print(nm.sapa3())#methode dengan return

#PRIVAT VARIABEL

class pahlawan:
    def __init__(self,nama,kesehatan):
        self.nama = nama
        self.kesehatan = kesehatan

        #varibel instence PRIVAT
        self.__private = "akses ditolak"
        #varibel instence PROTECTED
        self._protected = "izin tdk diterima"

hero = pahlawan ("elqusairi",92)
print(hero.__dict__)
print(pahlawan.__dict__)
