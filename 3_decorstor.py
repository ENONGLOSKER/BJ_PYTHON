class pahlawan:
    __jumlah = 0
    def __init__(self,nama):
        self.__nama = nama
        pahlawan.__jumlah += 1 #menempel pada class

        #mengakases
    def getjumlah1(): #tanpa argumnet, karena bukan objek
        return pahlawan.__jumlah

    @staticmethod #decorator : agar bisa di akses oleh objek atau class, tanpa ada argument
    def getjumlah2(): # static method
        return pahlawan.__jumlah

    @classmethod #decorator : agar bisa di akses oleh objek atau class dengan adanya argument
    def getjumlah3(pepadu): # static method
        return pepadu.__jumlah

hero1 = pahlawan("elqusairi")
print(pahlawan.getjumlah1())
# print(hero1.getjumlah1()) tidak bisa di akases karena berupa objek

hero2 = pahlawan("alqusairi")
print(hero2.getjumlah2())
        
hero3 = pahlawan("elqz132")
print(hero3.getjumlah3())
print(pahlawan.getjumlah3())

        