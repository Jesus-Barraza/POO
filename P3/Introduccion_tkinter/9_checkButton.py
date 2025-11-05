import tkinter as tk

#Ventana
ventana=tk.Tk()
ventana.geometry("500x500")
ventana.title("Check button \U0001F600")

#Funciones lógicas
opcion=tk.IntVar() #Esto permite guardar datos en un valor lógico

#funcion
def mostrarEstado(funcion, opc):
    if opc.get():
        temp="Activadas"
    else:
        temp="Desactivadas"

    funcion.config(
        text=f"Notificaciones {temp}"
    )

#Cuadro de verificación
checkboton=tk.Checkbutton(ventana, text="¿Desea recibir notificaciones?", variable=opcion, onvalue=True, offvalue=False) #La variable permite ingresar datos, en activación este genera un valor, si no genera otro
checkboton.config(
    font=("Arial",12)
)
checkboton.pack(pady=5)

#Boton
btn_confirmacion=tk.Button(ventana, text="Confirmar", command=lambda:mostrarEstado(lbl_notificacion, opcion))
btn_confirmacion.config(
    font=("arial",10),
    width=10
)
btn_confirmacion.pack(anchor="n", pady=5)

#Texto
lbl_notificacion=tk.Label(ventana, text="")
lbl_notificacion.config(
    font=("Arial", 12)
)
lbl_notificacion.pack(pady=10)

ventana=tk.mainloop()