print('===== 02 TUPLE =====')

#membuat
el = ('z',1,2,3,'q')

#mengakses
print(el)
print('ini data list:',el[0])

#menambah
tp1 =list(el)
tp1.insert(3,'a')
el=tuple(tp1)
print(el)

#merubah
tp1 = list(el)
tp1[4]='l'
el = tuple(tp1)
print(el)

#menghapus
tp1 =list(el)
del tp1[1]
el = tuple(tp1)
print(el)


# TUPLE LANJUT----------------