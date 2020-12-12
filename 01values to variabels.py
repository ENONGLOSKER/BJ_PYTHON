#variabel dan nilai atau values
usia   = 20 
tinggi = 100 
berat  = 12,1
nama   = "elqusairi "

print("usia ",20 )
print("tinggi",100 )
print("berat ", 12,1)
print("nama   = elqusairi ") 

#string atau karakter
str='zaenul alqusairi'
print (str)
print (str[0])
print (str[2:5])
print (str[2:])
print (str*2)
print (str+"ok")

#list (bisa di ubah)
mylist=["zaq",786,2.223,"qaz",70.2]
mytinylist=[123,'qaz']

print(mylist)
print(mylist [0])
print(mylist [1:3])
print(mylist [2:])
print( mytinylist*2)
print(mylist+mytinylist)
del mylist[2]
print (mylist)
mylist.append(100)
print(mylist)

#dictionaries(kamus)

mydictionaries={}
mydictionaries['satu']= 'ini'
mydictionaries[2]='ini dari key satu'
mytinydict={'kaprodi:l.puji,nik':11111,'sekprodi:fahrurazi,nik':22222}

print(mydictionaries['satu'])
print(mydictionaries[2])
print(mytinydict)
print(mytinydict.keys())
print(mytinydict.values())

#def
def fungsi(x):
    return((x*x)+(20*x)-7)
y=int(input("masukan fungsi: "))
print(fungsi(y))
    
