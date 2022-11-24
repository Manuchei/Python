f=open('datos.txt', 'r')
texto = f.read()
print(texto)

f=open('datos.txt', 'r')
lines = f.readlines()
f.close()
print(lines[0], end='')
print(lines[1], end='')