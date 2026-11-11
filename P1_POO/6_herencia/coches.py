class Coches:
    pass

class Camiones(Coches):
    def __init__(self, marca, color, modelo, velocidad, potencia, asientos, eje, capacidadCarga):
        super().__init__(marca, color, modelo, velocidad, potencia, asientos)
        self.__eje = eje
        self.__capacidadCarga = capacidadCarga 