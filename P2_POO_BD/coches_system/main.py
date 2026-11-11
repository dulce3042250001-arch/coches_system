from coches import coches, cochesBD

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

    def datos_coche(self,tipo):
        self.borrarPantalla()
        print(f"\n\t...Ingresar los datos del {tipo}...")
        cochesito={}
        cochesito["marca"]=input("Marca: ").upper().strip()
        cochesito["color"]=input("Color: ").upper().strip()
        cochesito["modelo"]=input("Modelo: ").upper().strip()
        cochesito["velocidad"]=input("Velocidad (Km/h): ").strip()
        cochesito["potencia"]=input("Potencia (Hp): ").strip()
        cochesito["asientos"]=input("Asientos: ").strip()
        # return marca,color,modelo,velocidad,potencia,asientos
        return cochesito

    def menu_coches(self):
        opc = True 
        while opc:
            self.borrarPantalla()
            opc=self.menu_acciones("Coches")
            match opc:
                case '1':
                    # Solicitar datos
                    cochesito=self.datos_coche("Coche")
                    coches1=coches.Coches(cochesito["marca"],cochesito["color"],cochesito["modelo"],cochesito["velosidad"],cochesito["potencia"],cochesito["asientos"])
                    
                    # Crear objeto de cochesBD y luego insertar BD
                    coches1=cochesBD.CochesBD(cochesito["marca"],cochesito["color"],cochesito["modelo"],cochesito["valosidad"],cochesito["potencia"],cochesito["asientos"]) 
                    respuesta=coches1.insertar() 
                    self.respuesta_sql(respuesta)
                    del coches1
                case '2':
                    self.borrarPantalla()
                    id=input("Ingrese el ID del coche a eliminar: ").strip()
                    #coches1 = cochesBD.CochesBD("","","",0,0,0)
                    respuesta=coches.Coches.eliminar(id)
                    self.respuesta_sql(respuesta)
                    # del coches1
                case '3':
                    self.borrarPantalla()
                    id=input("Ingrese el ID del coche a actualizar: ").strip()
                    cochesito=self.datos_coche("Coche")
                    coches1=coches.Coches(cochesito["marca"],cochesito["color"],cochesito["modelo"],cochesito["velosidad"],cochesito["potencia"],cochesito["asientos"])
                    respuesta=coches1.eliminar(id)
                    self.respuesta_sql(respuesta)
                    # del coches1
                case '4':
                    self.borrarPantalla()
                    registros=coches.Coches.actualizar()
                    num_coche=1
                    if len(registros) >0:
                        for fila in registros:
                            print(f"\n\tCoche #: {num_coche}\n\t\tID: {fila[0]}\n\t\tMraca: {fila[1]}\n\t\tColor: {fila[2]}\n\t\tModelo: {fila[3]}\n\t\tVelocidad: {fila[4]}\n\t\tPotencia: {fila[5]}\n\t\tAsientos: {fila[6]}")
                            num_coche+=1
                            self.esperarTecla()
                    else:
                        print("...POR EL MOMENTO NO SE ENCONTRO INFORMACION...")
                        self.esperarTecla()
                    # del coches1
                case '5':
                    pass 
                case _:
                    self.opcionInvalida()


    def main(self):
        opcion = True 
        while opcion:
            self.borrarPantalla()
            opcion=input("\n\t\t ::: MENU PRINCIPAL :::\n\t1. - Coches\n\t2. - Salir\n\tElige una opcion: ").lower().strip()
            match opcion:
                case '1':
                    self.borrarPantalla()
                    self.menu_coches()
                    self.esperarTecla()
                case '2':
                    self.borrarPantalla()
                    self.terminar()
                    opcion= False
                case _:
                    self.opcionInvalida()

    

if __name__=="__main__":
    app=App()