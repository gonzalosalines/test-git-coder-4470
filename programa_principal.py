#import  modulo
from modulo import sumar,restar
from atleta import Atleta

num1 =int(input("Ingrese nun 1: "))
num2 =int(input("Ingrese nun 2: "))

resultado = modulo.sumar(num1,num2)
print(resultado)

corredor = Atleta("leonel", "Gareis", 1.82, 92, "222222")
print(corredor)




