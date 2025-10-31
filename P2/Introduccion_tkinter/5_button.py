import tkinter as tk

#cambio de texto
def cambiarTexto():
    label_nombre.config(text="Nombre: Barraza Torres Jesús Daniel")
    label_password.config(text="Contraseña: ········")

def regresarTexto():
    label_nombre.config(text="Nombre: ...")
    label_password.config(text="Contraseña: ...")

#Ventana
ventana=tk.Tk()
ventana.geometry("800x600")
ventana.title("Uso de botones, marcos y etiquetas \U0001F480")

#marcos
#marco_superior=tk.Frame(ventana, width=800, height=50, bg="#3434af", relief="solid", border=2)
marco_superior=tk.Frame(ventana)
marco_superior.config(
    width=800, 
    height=50, 
    bg="#3434af", 
    relief="solid", 
    border=2
) #se recomienda que dentro del formato config se encuentren las configuraciones
marco_superior.pack_propagate(False)
marco_superior.pack(side="top")

#etiqueta
titulo=tk.Label(marco_superior)
titulo.config(
    text="Inicio de sesión",
    font=("Arial",20),
    fg="#ffffff",
    bg="#3434af"
)
titulo.pack(anchor="center")

label_nombre=tk.Label(ventana, text="Nombre: ...")
label_nombre.pack(pady=10)

label_password=tk.Label(ventana, text="Contraseña: ...")
label_password.pack(pady=10)

#botones
confirmar=tk.Button(ventana, text="Aceptar", command=cambiarTexto).pack(pady=30)
regresar=tk.Button(ventana, text="Regresar", command=regresarTexto).pack(pady=10)

ventana=tk.mainloop()