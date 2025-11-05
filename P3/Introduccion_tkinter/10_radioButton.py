import tkinter as tk

#Ventana
ventana=tk.Tk()
ventana.geometry("500x500")
ventana.title("Radio button \U0001F4FB")

#Variable de opcion
opcion=tk.StringVar()

#funcion
def mostrarEstado(funcion, opc):
    funcion.config(
        text=f"Opción seleccionada: {opc.get()}"
    )

#Botón de radio
radio_boton1=tk.Radiobutton(ventana, text="Opción 1", variable=opcion, value="Opcion 1")
radio_boton1.pack(pady=5)
radio_boton2=tk.Radiobutton(ventana, text="Opción 2", variable=opcion, value="Opcion 2")
radio_boton2.pack(pady=5)
radio_boton3=tk.Radiobutton(ventana, text="Opción 3", variable=opcion, value="Opcion 3")
radio_boton3.pack(pady=5)

#Boton
btn_seleccion=tk.Button(ventana, text="Mostrar selección", command=lambda:mostrarEstado(lbl_notificacion, opcion))
btn_seleccion.config(
    font=("arial",10),
    width=15
)
btn_seleccion.pack(anchor="n", pady=5)

#Texto
lbl_notificacion=tk.Label(ventana, text="")
lbl_notificacion.config(
    font=("Arial", 12)
)
lbl_notificacion.pack(pady=10)

ventana=tk.mainloop()