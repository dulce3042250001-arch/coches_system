class Personas:
    def __init__(self,nombre,edad,tel):
        self.nombre = nombre
        self.edad = edad
        self.tel = tel

    def info_Personal(self):
        print("Nombre: ", self.nombre)
        print("Edad: ", self.edad)
        print("Tel: ", self.tel)

class Estudiantes(Personas):
    def __init__(self, carrera, matricula):
        self._carrera = carrera
        self._matricula = matricula

    def informar_carrera(self):
        print("Carrera: ", self._carrera)
        print("Matricula: ", self._matricula)

    def info_Personal(self):
        super().info_Personal
        self.informar_carrera()

class Docentes(Personas):
    def __init__(self, modalidad, num_empleado):
        self.__modalidad = modalidad
        self.__num_empleado = num_empleado

    def informar_modalidad(self):
        print("Modalidad: ", self.__modalidad)
        print("Num Empleados: ", self.__num_empleado)

    def info_Personal(self):
        super().info_Personal
        self.informar_modalidad()

estudainte1 = Estudiantes("Ana Torres Guzman", 20, 6181234567, "MECA", 233584768)
docente1 = Docentes("Daniel Fuentes Loera", 40, 6183335678, "TI", 123)

estudiante1.info_Personal()
docente1.infor_Personal()