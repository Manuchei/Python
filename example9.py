f=open('datos.txt', 'r')
f.seek(0)
f.seek(2)
info = f.read(4)
f.seek(4)
info=f.read(4)
info=f.read(4)
print(info)