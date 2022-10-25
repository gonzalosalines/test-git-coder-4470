# Excepciones multiples

def dividir(a,b):
  return a/b

try:
  a = int(input("Ingrese A: "))
  b = int(input("Ingrese B: "))

  resultado = dividir(1,1)

  print(resultado)

except Exception as error
  print("[!] TIPO DE ERROR: ", type(error.__name__))
  print(f"se ha disparado un error: {error}")