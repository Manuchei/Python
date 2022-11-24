#-*. coding: utf-8 -*-

#Herencia multiple

class Animal:
    def __init__(self, name):
        self.name=name
    def __eat(self):
        pass
    @staticmethod
    def max_time_live():
        return 400
    @classmethod
    def min_time_live(cls):
        return 10


class Npc:
    def __init__(self, vida):
        self.vida = vida
    
class Duck(Animal, Npc):
    def __init__(self, name, vida):
        #self.name=name
        #super().__init__(self,name)
        Animal.__init__(self, name,)
        Npc.__init__(self, vida)

lucas = Duck('lucas', '100')
print(lucas.max_time_live())
print(lucas.min_time_li)



