from estudiantes import estudiante

class App:
    def __init__(self):
        self.main()

    def borrarPantalla(self):
        print("\033c")

    def esperarTecla(self):
        input("...Oprima cualquier tecla para continuar...")

    def terminar(self):
        input("...::: ¡GRACIAS POR UTILIZAR NUESTRO SISTEMA, \n vuelva pronto! :::...")

    def opcionInvalida(self):
        input("...::: ¡OPCION INVALIDA, INTENTELO DE NUEVO! :::...")

    def menu_acciones(self):
        print("\n\t\t\t...::: MENU PRINCIPAL :::...\n")
        opcion=input("\n\t 1.- Agrgar \n\t 2.- Borrar \n\t 3.- Modificar \n\t 4.- Mostrar \n\t 5.- Salir \n\tElige una Opcion: ").strip()
        return opcion 
    
    def respuesta_sql(self, respuesta):
        if respuesta:
            input("\n\t...¡ACCION REALIZADA VON EXITO!...")
        else:
            input("\n\t...¡ESTA ACCION NO PUDO REALIZARSE EN ESTE MOMENTO!...")

    def datos_estudiante(self,tipo):
        self.borrarPantalla()
        print(f"\n\t...Ingresar los datos del {tipo}...")
        estudiantito={}
        estudiantito["nombre"]=input("Nombre: ").upper().strip()
        estudiantito["Nota"]=input("Nota (Calificacion): ").strip()
        # return nombre,nota
        return estudiantito

    def menu_estudiantes(self):
        opc = True 
        while opc:
            self.borrarPantalla()
            opc=self.menu_acciones("Estudiantes")
            match opc:
                case '1':
                    estudiantito=self.datos_estudiante("Estudiante")
                    estudiante1=coches.Coches(estudiantito["Nombre"],estudiantito["Nota"])
                    estudiante1=cochesBD.CochesBD(estudiantito["Nombre"],estudiantito["Nota"]) 
                    respuesta=estudiante1.insertar("",0) 
                    self.respuesta_sql(respuesta)
                    del estudiante1
                case '2':
                    self.borrarPantalla()
                    id=input("Ingrese el ID del estudiante a eliminar: ").strip()
                    respuesta=estudiante.Estudiantes.eliminar(id)
                    self.respuesta_sql(respuesta)
                    # del estudiante1
                case '3':
                    self.borrarPantalla()
                    id=input("Ingrese el ID del estudiante a actualizar: ").strip()
                    estudiantito=self.datos_estudiante("Estudiante")
                    estudainte1=estudiante.Estudiantes(estudiantito["Nombre"],estudiantito["Nota"])
                    respuesta=estudiante1.actualizar()
                    self.respuesta_sql(respuesta)
                    del estudiante1
                case '4':
                    self.borrarPantalla()
                    registros=estudiante.Estudiantes.consultar()
                    num_estudiante=1
                    if len(registros) >0:
                        for fila in registros:
                            print(f"\n\tEstudiante #: {num_estudiante}\n\t\tID: {fila[0]}\n\t\tNombre: {fila[1]}\n\t\tNota: {fila[2]}")
                            num_estudiante+=1
                            self.esperarTecla()
                    else:
                        print("...POR EL MOMENTO NO SE ENCONTRO INFORMACION...")
                        self.esperarTecla()
                case '5':
                    pass 
                case _:
                    self.opcionInvalida()


    def main(self):
        opcion = True 
        while opcion:
            self.borrarPantalla()
            opcion=input("\n\t\t ::: MENU PRINCIPAL :::\n\t1. - Estudiantes\n\t2. - Salir\n\tElige una opcion: ").lower().strip()
            match opcion:
                case '1':
                    self.borrarPantalla()
                    self.menu_estudiantes()
                    self.esperarTecla()
                case '2':
                    self.borrarPantalla()
                    self.terminar()
                    opcion= False
                case _:
                    self.opcionInvalida()


if __name__=="__name__":
    app=App()