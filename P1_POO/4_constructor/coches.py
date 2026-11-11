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

# Multiples objetos/instancias
coche1 = Coches()
coche2 = Coches() 

print(f"El color del coche 1 es: {coche1.color}")
print(f"El color del coche 2 es: {coche2.color}")

for i in range(1,11):
    coche1.acelerar() 