print("\033c")

# Clase coches
class Coches:
    def __init__(self, color, marca, velocidad):
        self.__color = color
        self.__marca = marca
        self.__velocidad = velocidad

    def acelerar(self):
        pass 

    def frenar(self):
        pass 

    def tocar_claxon(self):
        pass 

# Instanciar o crear objetos de la clase coches
coche1=Coches('Blanco', 'VW', 220)
coche2=Coches('Azul', 'Nissan', 180)

print("El color del coche 1 es: {coche1.color}")
