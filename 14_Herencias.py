
class Animal:

    def __init__(self,edad,especie):
        self.edad = edad
        self.especie = especie

    def hablar(self):
        pass

    def moversr(self):
        pass

    def describeme(self):
        print(f"Soy un animal del tipo {type(self).__name__}")



class Perro(Animal):

    def __init__(self, nombre):
        self.nombre = nombre

        #pasando valores a la clase padre
        super().__init__(edad, especie)          


    def hablar(self):
        print("Guau!")

    def describeme(self):
        variable = super().describeme()
        return "Soy lamedor de bolas", variable #returnanod una tupla al separa por comas

perrito = Perro(5,"canino", "zeuz")

print(perrito.edad, perrito.especie)
perrito.describeme()

perrito.hablar()

print(perrito.describeme())