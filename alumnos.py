print("\033c")

class Alumnos:
    _nombre = ""
    _edad = 0
    _calificacion = 0

    # Metodos publicos
    def mostrarDatos(self, nombre, edad, calificacion):
        print(f"Nombre: {nombre}")
        print(f"Edad: {edad}")
        print(f"Calificacion: {calificacion}")

    def estaAprobado(self, calificacion):
        if calificacion >= 6:
            cadena = "APROBADO"
        else:
            cadena = "NO APROBADO"
        return cadena

# Crear objetos
alumno1 = Alumnos()
alumno2 = Alumnos() 