print("CONTINUE-----------")
n= 0

while n < 5 :
    n+=1
    print("hai..")

    if n == 3 :
        print("apa kabar")
        continue
    print("hello..") #continue akan meloncat ini, kemudian akan mencetak print 1 hai..
print("selamat!\n")

n= 0

print("BREAK-----------")
while n < 5 :
    n+=1
    print("hai..")

    if n == 3 :
        print("apa kabar")
        break
    print("hello..") #continue akan meloncat ini, kemudian akan mencetak print 1 hai..
print("selamat!\n")

print("PASS-----------")
n=0
while n < 5:
    n+= 1
    print(f"nilai ke {n}")
    if n % 2 == 0 :
        pass #tidak dijalankan
print("selesai")