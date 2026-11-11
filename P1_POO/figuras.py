import math 

class Figuras:
    def __init__(self, x, y, visible = True):
        self.x = x
        self.y = y
        self.visible = visible

    def estaVisible(self):
        return self.visible 

    def mostrar(self):
        self.visible = True
        print("La figura se esta mostrando")

    def ocultar(self):
        self.visible = False 
        print("La figura se esta ocultando")

    def mover(self, x, y):
        self.x = x
        self.y = y 
        print(f"La figura se movio a ({self.x}, {self.y})")

    def calcularArea(self):
        return 0 

class Rectangulos(Figuras):
    def __init__(self, x, y, alto, ancho, visible = True):
        super().__init__(x, y, visible)
        self.alto = alto 
        self.ancho = ancho

    def ocultar(self):
        super().ocultar() 

    def mostrar(self):
        super().mostrar()

    def calcularArea(self):
        return self.alto * self.ancho

class Circulos(Figuras):
    def __init__(self, x, y, radio, visible = True):
        super().__init__(x, y, visible)
        self.radio = radio 

    def ocultar(self):
        super().ocultar()

    def mostrar(self):
        super().mostrar()

    def calcularArea(self):
        return math.pi * self.radio ** 2

rectangulo1 = Rectangulos(3, 4, 10, 20)
circulo1 = Circulos(3, 3, 6)

# Mostrar rectangulo
print("--- RECTANGULO ---")
print("Posicion x: ", rectangulo1.x)
print("Posicion y: ", rectangulo1.y)
print("Visible: ", rectangulo1.estaVisible())
print("Alto: ", rectangulo1.alto)
print("Ancho: ", rectangulo1.ancho)
print("Area: ", rectangulo1.calcularArea())

print()
# Mostrar circulo
print("--- CIRCULO ---")
print("Posicion x: ", circulo1.x)
print("Posicion y: ", circulo1.y)
print("Visible: ", circulo1.estaVisible())
print("Radio: ", circulo1.radio)
print("Area: ", round(circulo1.calcularArea(), 2))