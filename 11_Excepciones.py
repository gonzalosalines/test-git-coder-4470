#por el profe
# Caso 1: B = 0
# Caso 2: A o B no sean de tipo numerico 

def dividir(a, b):

     # Validamos caso 1
     if b == 0:
          return None
     
     # Validamos caso 2
     if not ((type(a) == int or type(a) == float) and (type(b) == int or type(b) == float)):
          return None

     return a/b


print( dividir(1,2) )
print( dividir(1,0) )
print( dividir("1",2) )
print( dividir("1",[2]) )