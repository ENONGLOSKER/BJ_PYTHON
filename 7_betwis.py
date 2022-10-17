print("===== BETWIS =====")

a = int(input("masukan data : "))
b = int(input("masukan data : "))

c = a | b
print("----------------------------------- or (|)")
print("decimal :",a,"atau biner : ",format(a,"08b"))
print("decimal :",b,"atau biner : ",format(b,"08b"))
print("----------------------------------- or (|)")
print("decimal :",c,"atau biner : ",format(c,"08b"))
print("===================================")
c = a & b
print("----------------------------------- and (&)")
print("decimal :",a,"atau biner : ",format(a,"08b"))
print("decimal :",b,"atau biner : ",format(b,"08b"))
print("----------------------------------- and (&)")
print("decimal :",c,"atau biner : ",format(c,"08b"))
print("===================================")
c = a ^ b
print("----------------------------------- xor (^)")
print("decimal :",a,"atau biner : ",format(a,"08b"))
print("decimal :",b,"atau biner : ",format(b,"08b"))
print("----------------------------------- xor (^)")
print("decimal :",c,"atau biner : ",format(c,"08b"))
print("===================================")
z = a<<1
q = b>>1
al= z ^ q
print("----------------------------------- shift (<< >>)")
print("decimal :",z,"atau biner : ",format(z,"08b"))
print("decimal :",q,"atau biner : ",format(q,"08b"))
print("----------------------------------- xor (^)")
print("decimal :",al,"atau biner : ",format(al,"08b"))