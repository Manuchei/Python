#-*. coding: utf-8 -*-
entero = int('3')
decimal = float('4.5')
texto = str(55)

#No hace sobrecarga, solo imprime la ultima vez,
#por lo tanto si en le print ponemos 2 numeros peta

def sum(a,b):
    return a+b

def sum(a,b,c):
    return a+b+c

print(sum(5,6,7))