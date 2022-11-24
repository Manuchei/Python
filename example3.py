#-*. coding: utf-8 -*-

#En python si existe la sobrecarga de operadores
class Circle:
    def __init__(self, r):
        self.r = r

    def __add__(self, other):
        return Circle(self.r + other.r)

    def __gt__(self, other):
        return self.r > other.r

    def __pow__(self, other):
        return Circle(self.r  ** other.r)


c1 = Circle(4)
c2 = Circle(6)

c3 = c1 + c2

print(c1>c2)
print(c2>c1)
print(c1<c2)
print((c2**c1).r)