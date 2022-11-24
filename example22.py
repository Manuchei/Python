#Pasar argumentos indetermindos
def add(*args):
    count = 0
    for n in args:
        count+=n
    return count 
print(add(5, 8, 7))

def calculate(**args):
    p=args['precio']
    k=args['kilos']
    return p*k
print(calculate(nombre='Frase', precio=4.6, kilos=20))