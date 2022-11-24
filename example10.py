#docstring
def add(n1,n2):
    """ Este metodo suma 2 números """

    """
     >>>add(5,2)
    7
    
    """
   
    
    
   
    return n1+n2
print(add(4,2))

print(' El nombre del método ', add.__name__)
print(' Lo que hace el método ', add.__doc__)
#python -m doctest -v example10.py