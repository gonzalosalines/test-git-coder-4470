class Atleta:

    deporte = None

    def __init__(self, nombre, apellido, altura, peso, telefono):
        

        self.nombre = nombre
        self.apellido = apellido
        self.__altura = altura
        self.__peso = peso
        self.telefono = telefono
        
        # Agregar IMC
        self.imc = self.__calcular_imc()

def __calcular_imc(self):

        valor_imc = self.__peso / (self.__altura ** 2)

        if valor_imc < 18.5:
            return "Peso inferior"
        elif 18.5 <= valor_imc < 25:
            return "Normal"
        elif 25 <= valor_imc < 30:
            return "Sobrepeso"
        elif 30 <= valor_imc < 35:
            return "Obesidad"
        else:
            return "Obesidad Extrema"

    # Metodos GET y SET para atributos privados
def set_peso(self, nuevo_peso):
        self.__peso = nuevo_peso
        self.imc = self.__calcular_imc()

def get_peso(self):
    return self.__peso

def set_altura(self, nueva_altura):
        self.__altura = nueva_altura
        self.imc = self.__calcular_imc()

def get_altura(self):
    return self.__altura

def __str__(self):
    return f"{self.apellido}, {self.nombre} -> {self.imc}"
