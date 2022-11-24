#-*. coding: utf-8 -*-

#funcion de orden superior

colection = [-2,5,7,2]

for elem in colection:
    c = elem**2
    print(c)

    #filter, map, foreach, reduce, ??
    #funcion pura:
    # - No funciona a nada del exterior
    # - para una entrada dada soempre da la misma salida
    def square(n):
        return n**2

    def is_positive(n):
        return n>=0
    r = list( map(square, colection))
    print(r)

    r = list(filter(is_positive, colection))
    print(r)

    r = list(map( lambda n:n**2, colection ) )
    print(r)

    r = list(filter(lambda n:n>0, colection))
    print(r)

    from functools import reduce
    r = reduce(lambda n,m:n+m, colection)
    print(r)




   
        

