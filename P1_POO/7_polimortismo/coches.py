class Coches:
    pass

class Camionetas(Coches):
    pass 

class Camiones(Coches):
    def __init__(self, marca, color, modelo, velocidad, potencia, asientos, eje, capacidadCarga):
        super().__init__(marca, color, modelo, velocidad, potencia, asientos)
        self.__eje = eje
        self.__capacidadCarga = capacidadCarga 

class CamionesCarga(Camiones):
    def __init__(self, marca, color, modelo, velocidad, potencia, asientos, eje, capacidadCarga, tipo_carga):
        super().__init__(marca, color, modelo, velocidad, potencia, asientos, eje, capacidadCarga)
        self.__tipo_carga = tipo_carga 

        def acelerar(self):
            self.velocidad -= 1
            print("Eestoy acelerando")

        def getTipo_carga(self):
            return self.__tipo_carga  

        def getTipo_carga(self, Tipo_carga):
            return self.__tipo_carga  

camionescarga1 = CamionesCarga("Star", "Rojo", 2026, 180, 200, 2, 2, 2500, "Materiales")
print(camionescarga1._velocidad)        

