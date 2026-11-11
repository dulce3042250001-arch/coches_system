'''Ejemplo 1: Crear una clase (con molde para crear mas objetos) llamada Coches y apartir de la clase
crear objetos o instancias (coche) con cracteristicas similares (marca,color, modelo,velocidad,potencia,
asientos) y con los operaciones de acelerar y frenar. Que los atributos y metodos sean publicos.
- muestre el color de los coches
- que los operaciones disminuyan o aumentan la velocidad segun sea el caso y hay jugar con los metodos e
imprimir la velocidad final.'''

print("\033c")
class Coches:
    marca = ""
    color = "Blanco" 
    modelo = ""
    velocidad = 100
    potencia = 0
    asientos = 0

    def acelerar(self):
        self.velocidad += 1
        print(f"Ahora la velocidad es: {self.velocidad}")

    def frenar(self):
        self.velocidad -= 1
        print(f"Ahora la velocidad es: {self.velocidad}")

coche1 = Coches()
coche2 = Coches() 

print(f"El color del coche 1 es: {coche1.color}")
print(f"El color del coche 2 es: {coche2.color}")

for i in range(1,11):
    coche1.acelerar() 