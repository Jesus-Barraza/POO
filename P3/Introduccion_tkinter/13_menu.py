import tkinter as tk

#Ventana
ventana=tk.Tk()
ventana.geometry("500x500")
ventana.title("Menu \U0001F414")


#Funciones
def mostrarEstado(funcion, valor):
    funcion.config(text=f"Se {valor}")

#Barra del menú
menubar=tk.Menu(ventana)
ventana.config(menu=menubar) #Esta es una excepción para la configuración de pack

#Archivo del menú
menuarch=tk.Menu(menubar, tearoff=False)
menubar.add_cascade(label="Archivo", menu=menuarch) #Esto permite meter las funciones arriba
menuarch.add_command(label="Nuevo archivo", command=lambda:mostrarEstado(lbl_resultado, "creó un nuevo archivo")) #añade un comando
menuarch.add_command(label="Guardar archivo", command=lambda:mostrarEstado(lbl_resultado, "guardó un archivo"))
menuarch.add_separator() #comando para crear separador
menuarch.add_command(label="Salir", command=lambda:ventana.quit())

#Actividad
menuarch2=tk.Menu(menubar, tearoff=False)
menubar.add_cascade(label="Edición", menu=menuarch2)
menuarch2.add_command(label="Copiar", command=lambda:mostrarEstado(lbl_resultado,"copió el archivo"))
menuarch2.add_command(label="Recortar", command=lambda:mostrarEstado(lbl_resultado,"cortó el archivo"))
menuarch2.add_separator()
menuarch2.add_command(label="Salir", command=lambda:ventana.quit())

#resultado
lbl_resultado=tk.Label(ventana, text="")
lbl_resultado.pack(pady=5)

ventana=tk.mainloop()