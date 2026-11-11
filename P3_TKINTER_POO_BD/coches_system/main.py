from coches import coches
from tkinter import Label,Entry,Button
import tkinter as tk
from tkinter import messagebox

class App:
    def __init__(self, ventana):
        self.ventana=ventana
        self.ventana.title("Gestion de Coches")
        self.ventana.geometry("600x600")
        self.ventana.resizable(0,0)
        self.main()

    # Vistas o Views del Sistema...
    def borrarPantalla(self):
        for widge in self.ventana.winfo_children():
            widge.destroy()

    def main(self):
        self.borrarPantalla()
        Label(self.ventana,text="::: MENU PRINCIPAL :::").pack(pady=20)
        Button(self.ventana,text="1.- Coches", command=self.menu_acciones).pack(pady=10)
        Button(self.ventana,text="2.- Salir", command=self.ventana.quit).pack(pady=10)

    def menu_acciones(self):
        self.borrarPantalla()
        tipo="Cohes"
        Label(self.ventana,text=f"...::: MENU de {tipo} :::...").pack(pady=10)
        Button(self.ventana,text="1.- Agregar", command=self.insertar_coche_view).pack(pady=10)
        Button(self.ventana,text="2.- Borrar", command=self.eliminar_coche_view).pack(pady=10)
        Button(self.ventana,text="3.- Modificar", command=self.modificar_coches_view).pack(pady=10)
        Button(self.ventana,text="4.- Mostrar", command=self.consultar_coche_view).pack(pady=10)
        Button(self.ventana,text="5.- Regresar", command=self.main).pack(pady=10)

    def insertar_coche_view(self):
        self.borrarPantalla()
        Label(self.ventana,text="...Ingresar los datos del Coche...").pack(pady=10)
        Label(self.ventana,text="Marca: ").pack(pady=5)
        self.marca=Entry(self.ventana)
        self.marca.focus()
        self.marca.pack(pady=5)

        Label(self.ventana,text="Color: ").pack(pady=5)
        self.color=Entry(self.ventana)
        self.color.pack(pady=5)

        Label(self.ventana,text="Modelo: ").pack(pady=5)
        self.modelo=Entry(self.ventana)
        self.modelo.pack(pady=5)

        Label(self.ventana,text="Velocidad: ").pack(pady=5)
        self.velocidad=Entry(self.ventana)
        self.velocidad.pack(pady=5)

        Label(self.ventana,text="Potencia: ").pack(pady=5)
        self.potencia=Entry(self.ventana)
        self.potencia.pack(pady=5)

        Label(self.ventana,text="Asientos: ").pack(pady=5)
        self.asientos=Entry(self.ventana)
        self.asientos.pack(pady=5)

        Button(self.ventana,text="Agregar", command=self.insertar_coche_controller).pack(pady=5)
        Button(self.ventana,text="Regresar", command=self.menu_acciones).pack(pady=5)

    def eliminar_coche_view(self):
        self.borrarPantalla()
        Label(self.ventana,text="... Ingresar el ID del coche a eliminar ...")

    def consultar_coche_view(self):
        self.borrarPantalla()
        Label(self.ventana, text="..: Consultar Coches :..").pack(pady=10)
        filas = ""
        filas=self.consultar_coche_controller(filas)
        Label(self.ventana, text=f"{filas}").pack(pady=5)
        Button(self.ventana, text="..: Consultar :..", command=self.menu_acciones).pack(pady=5)

    def modificar_coche_view(self):
        self.borrarPantalla()
        Label(self.ventana, text="INGRESAR EL ID DEL COCHE A MODIFICAR").pack(pady=10)
        self.id=Entry(self.ventana)
        self.id.focus()
        self.id.pack(pady=5)

        Label(self.ventana,text="...Ingresar los datos del Coche...").pack(pady=10)
        Label(self.ventana,text="Marca: ").pack(pady=5)
        self.marca=Entry(self.ventana)
        self.marca.focus()
        self.marca.pack(pady=5)

        Label(self.ventana,text="Color: ").pack(pady=5)
        self.color=Entry(self.ventana)
        self.color.pack(pady=5)

        Label(self.ventana,text="Modelo: ").pack(pady=5)
        self.modelo=Entry(self.ventana)
        self.modelo.pack(pady=5)

        Label(self.ventana,text="Velocidad: ").pack(pady=5)
        self.velocidad=Entry(self.ventana)
        self.velocidad.pack(pady=5)

        Label(self.ventana,text="Potencia: ").pack(pady=5)
        self.potencia=Entry(self.ventana)
        self.potencia.pack(pady=5)

        Label(self.ventana,text="Asientos: ").pack(pady=5)
        self.asientos=Entry(self.ventana)
        self.asientos.pack(pady=5)

        Button(self.ventana,text="Modificar", command="").pack(pady=5)
        Button(self.ventana,text="Regresar", command=self.menu_acciones).pack(pady=5)

    def consultar_coche_controller(self,filas):
        registros=coches.Coches.consultar()
        num_coche=1
        if len(registros)>0:
            for fila in registros:
                filas=filas+(f"\n\tCoche #: {num_coche}\nID: {fila[0]}\tMarca: {fila[1]}\tColor: {fila[2]}\nModelo: {fila[3]}\nVelocidad: {fila[4]}\nPotencia: {fila[5]}\nAsientos: {fila[6]}")
                num_coche+=1
            else:
                messagebox.showarning(title="..:: AVISO ::..",message=".. NO SE ENCONTRO INFORMACION EN LA BD ..")
            return filas

    def insertar_coche_controller(self):
        self. marca=self.marca.get()
        self.color=self.color.get()
        self.modelo=self.modelo.get()
        self.velocidad=self.velocidad.get()
        self.potencia=self.potencia.get()
        self.asientos=self.asientos.get()
        coches1=coches.Coches(self.marca.get(),self.color.get(),self.modelo.get(),self.velocidad.get(),self.potencia.get(),self.asientos.get())
        respuesta=coches1.insertar()
        self.respuesta_sql(respuesta) 
        del coches1 

    def modificar_coche_controller(self):
        self.id=self.id.get()
        coches1=coches.Coches(self.marca.get(),self.color.get(),self.modelo.get(),self.velocidad.get(),self.potencia.get(),self.asientos.get())
        respuesta=coches1.actualizar()
        self.respuesta_sql(respuesta) 
        del coches1 

    def respuesta_sql(self, respuesta):
        if respuesta:
            messagebox.showinfo(title="..:: Exitoso ::..", message="...¡ACCION REALIZADA CON EXITO!...")
        else:
            messagebox.showinfo(title="..:: Verifique Por Favor ::..", message="...¡ESTA ACCION NO PUDE REALIZARCE!...")

# Controlador o Controller del Sistema...
if __name__=="__main__":
    ventana=tk()
    app=App(ventana)
    ventana.mainloop()