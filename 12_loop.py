# for---------------------------------------

# for angka in range (1,11):
#     print(angka)

# data = [1,2,3,4,5]

# print(type(data))
# for angka in range (len(data)):
#     print(angka)

my_list = "elqusairi"

#iterate untuk mengulan data selain int
for item in my_list: #tanpa RANGE
    print(item)  # 👉️ 'a', 'b', 'c'
#iterate over list with index
for idx, item in enumerate(my_list):
    print(idx, item)  # 👉️ 0 a, 1 b, 2 c


# while----------------------------------------

no = 0

while no < 5:
    no +=1
    print(f"perulangan yang ke{no}")

print("berhenti, karena sudah melebihi")