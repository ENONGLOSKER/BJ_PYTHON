#perulangan list
data1 = [1,2,4,6,4,7,9,5,2,1]
p_data = len(data1)

#for baru

for data in data1:
    print(f"DATA = {data}")


#for lama
print("\n for")
for i in range (p_data):
    print(f"DATA = {data1[i]}")

#while 
print("\n while")
no = 0
while no < p_data:
    print(f"DATA = {data1[no]}")
    no +=1


#list comrehension
print("\n list comrehension")
[print(f"DATA = {i}") for i in data1]

angka = [1,3,5,4,2,6]
pangkat =[a**2 for a in angka]
print(pangkat)


#enumerate
print("\n enumerate")
for nomor,isi in enumerate(data1):
    print(f"INDEX = {nomor} ISI = {isi}")