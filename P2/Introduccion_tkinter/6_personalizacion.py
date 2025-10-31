import tkinter as tk

#Funciones de botón
def iniciartexto(funcion):
    funcion.config(
        text="POO con python",
        bg="#ff5555",
        fg="#9f0000",
        cursor="spider"
    )

def regresartexto(funcion):
    funcion.config(
        text="Bienvenidos a tkinter",
        bg="#55ccff",
        fg="#000066"
    )

#ventana
ventana=tk.Tk()
ventana.geometry("800x600")
ventana.title("Personalizar widgets u objetos \U0001F6A1")

#etiquetas
etiqueta=tk.Label(ventana, text="Bienvenidos a tkinter")
etiqueta.config(
    bg="#55ccff",
    fg="#000066",
    width=50,
    height=4,
    font=("Helvetica",36,"italic"),
    relief="solid",
    border=2
)
etiqueta.pack(pady=25)

#botones
ingresar=tk.Button(ventana,text="Haz click aquí",command=lambda: iniciartexto(etiqueta))
ingresar.config(
    #bg="#eeeeee",
    fg="#121212",
    width=15,
    height=2,
    font=("Arial",12,"bold"),
    relief="groove",
    border=2,
    #activebackground="#cccccc",
    activeforeground="#232323"
)
ingresar.pack(pady=10)

regresar=tk.Button(ventana,text="Regresar valores",command=lambda: regresartexto(etiqueta))
regresar.config(
    #bg="#eeeeee",
    fg="#000000",
    width=15,
    height=2,
    font=("Arial",12,"bold"),
    relief="groove",
    border=2,
    #activebackground="#cccccc",
    activeforeground="#111111"
)
regresar.pack(pady=10)


ventana=tk.mainloop()