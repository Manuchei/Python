#list comprehension
list=[2,-1,8,2]
#Devuelve la lista sin negativos
result=[value for value in list if value >= 0]
print(result)
#Devuelve la lista elevada al cuadrado
result2=[value**2 for value in list if value]
print(result2)
#Devuelve la lista multiplicada por dos pero sin nummeros negativos
result3=[value*2 for value in list if value>=0]
print(result3)
