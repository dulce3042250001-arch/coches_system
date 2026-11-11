import tkinter as tk

font = ('Arial',12)

ventana = tk.Tk()
ventana.title("Ventana Principal")
ventana.geometry("400x300")

# Declaracion de variables
nombre = tk.StringVar()

# Label
label = tk.Label(ventana, text= "Hola Mundo", font=font, background="#08fb74")
# label.confing(text= "Hola Python")
label.pack(pady=30)

# Button
def saludar():
    label.config(text= "Hola Python")

def get_nombre():
    nombre = entrada.get()
    label.config(text = f"Nombre {nombre}")
btn = tk.Button(ventana, text = "Saludar", command=saludar, font=font)
btn.pack(pady=10)

# Input caja de texto
entrada = tk.Entry(ventana, textvariable=nombre, font=font, width=30)
entrada.pack(pady=10)

btn1 = tk.Button(ventana, text = "Obtener", command=get_nombre, font=font)
btn1.pack()

ventana.mainloop() 