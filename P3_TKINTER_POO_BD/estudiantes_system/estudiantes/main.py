from estudiantes import estudiantes
from tkinter import Tk,Label,Entry,Button
from tkinter import messagebox

class App:
    def __init__(self, ventana):
        self.ventana=ventana
        self.ventana.title("Gestion de Coches")
        self.ventana.geometry("600x600")
        self.ventana.resizable(0,0)
        self.main()

    def borrarPantalla(self):
        for widge in self.ventana.winfo_children():
            widge.destroy()

    def menu_acciones(self):
        self.borrarPantalla()
        tipo="Estudiantes"
        Label(self.ventana,text=f"...::: MENU de {tipo} :::...").pack(pady=10)
        Button(self.ventana,text="1.- Agregar", command=self.insertar_estudiante_view).pack(pady=10)
        Button(self.ventana,text="2.- Borrar", command=self.eliminar_estudiante_view).pack(pady=10)
        Button(self.ventana,text="3.- Modificar", command=self.modificar_estudiante_view).pack(pady=10)
        Button(self.ventana,text="4.- Mostrar", command=self.consultar_estudiante_view).pack(pady=10)
        Button(self.ventana,text="5.- Regresar", command=self.main).pack(pady=10)

    def insertar_estudiante_view(self):
            self.borrarPantalla()
            Label(self.ventana,text="...Ingresar los datos del Estudiante...").pack(pady=10)
            Label(self.ventana,text="Nombre: ").pack(pady=5)
            self.nombre=Entry(self.ventana)
            self.nombre.focus()
            self.nombre.pack(pady=5)
    
            Label(self.ventana,text="Nota: ").pack(pady=5)
            self.nota=Entry(self.ventana)
            self.nota.pack(pady=5)
    
            Button(self.ventana,text="Agregar", command=self.insertar_estudiante_controller).pack(pady=5)
            Button(self.ventana,text="Regresar", command=self.menu_acciones).pack(pady=5)

    def eliminar_estudiante_view(self):
        self.borrarPantalla()
        Label(self.ventana,text="... Ingresar el ID del coche a eliminar ...")
    
    def insertar_estudiante_controller(self):
        self.nombre=self.nombre.get()
        self.nota=self.nota.get()
        estudiante=estudiante.Estudiantes(self.nombre.get(),self.nota.get())
        respuesta=estudiante.insertar()
        self.respuesta_sql(respuesta) 
        del coches1 

    def consultar_estudiante_view(self):
        self.borrarPantalla()
        Label(self.ventana, text="..: Consultar Estudiantes :..").pack(pady=10)
        filas = ""
        filas=self.consultar_estudiante_controller(filas)
        Label(self.ventana, text=f"{filas}").pack(pady=5)
        Button(self.ventana, text="..: Consultar :..", command=self.menu_acciones).pack(pady=5)

    def consultar_estudiante_controller(self,filas):
        registros=estudiante.Estudiantes.consultar()
        num_estudiante=1
        if len(registros)>0:
            for fila in registros:
                filas=filas+(f"\n\tCoche #: {num_estudiante}\nID: {fila[0]}\tNombre: {fila[1]}\tNota: {fila[2]}")
                num_estudiante+=1
            else:
                messagebox.showarning(title="..:: AVISO ::..",message=".. NO SE ENCONTRO INFORMACION EN LA BD ..")
            return filas

    def modificar_estudiante_view(self):
            self.borrarPantalla()
            Label(self.ventana, text="INGRESAR EL ID DEL ESTUDIANTE A MODIFICAR").pack(pady=10)
            self.id=Entry(self.ventana)
            self.id.focus()
            self.id.pack(pady=5)
    
            Label(self.ventana,text="...Ingresar los datos del Estudiante...").pack(pady=10)
            Label(self.ventana,text="Nombre: ").pack(pady=5)
            self.marca=Entry(self.ventana)
            self.marca.focus()
            self.marca.pack(pady=5)
    
            Label(self.ventana,text="Nota: ").pack(pady=5)
            self.color=Entry(self.ventana)
            self.color.pack(pady=5)
    
            Button(self.ventana,text="Modificar", command="").pack(pady=5)
            Button(self.ventana,text="Regresar", command=self.menu_acciones).pack(pady=5)

    def modificar_coche_controller(self):
        self.id=self.id.get()
        estudiante=estudiante.Estudiantes(self.nombre.get(),self.nota.get())
        respuesta=estudiante.actualizar()
        self.respuesta_sql(respuesta) 
        del estudiante
    
    def respuesta_sql(self, respuesta):
        if respuesta:
            messagebox.showinfo(title="..:: Exitoso ::..", message="...¡ACCION REALIZADA CON EXITO!...")
        else:
            messagebox.showinfo(title="..:: Verifique Por Favor ::..", message="...¡ESTA ACCION NO PUDE REALIZARCE!...")

    def menu_estudiantes(self):
        opc = True 
        while opc:
            self.borrarPantalla()
            opc=self.menu_acciones("Estudiantes")
            match opc:
                case '1':
                    estudiantito=self.datos_estudiante("Estudiante")
                    estudiante1=estudiante.Estudiantes(estudiantito["Nombre"],estudiantito["Nota"])
                    estudiante1=estudiante.Estudiantes(estudiantito["Nombre"],estudiantito["Nota"]) 
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
                    estudiante1=estudiante.Estudiantes(estudiantito["Nombre"],estudiantito["Nota"])
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
        self.borrarPantalla()
        Label(self.ventana,text="::: MENU PRINCIPAL :::").pack(pady=20)
        Button(self.ventana,text="1.- Estudiantes", command="").pack(pady=10)
        Button(self.ventana,text="2.- Salir", command=self.ventana.quit).pack(pady=10)


if __name__=="__name__":
    ventana=Tk()
    app=App(ventana)
    ventana.mainloop()
