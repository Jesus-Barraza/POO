import tkinter as tk
from tkinter import ttk #Hay una librería alterna que no se encuentra en tkinter

#Ventana
ventana=tk.Tk()
ventana.geometry("500x500")
ventana.title("Porgress bar \U0001F50B")

#Funciones
def mostrarEstado(funcion):
    funcion.config(text=f"¡La carga ha finalizado!")

def progreso(funcion, texto):
    funcion["value"]=0
    ventana.update()
    for i in range (101):
        barra_progreso["value"]=i
        ventana.update()
        ventana.after(50)
        # Cuando llegue al 100%, mostrar el mensaje
        if i == 100:
            mostrarEstado(texto)

def reinicio(funcion, texto):
    funcion["value"]=0
    texto.config(text="")  # Limpiar el texto
    ventana.update()

#Barra de progreso
barra_progreso=ttk.Progressbar(ventana, mode="determinate", length=300)
barra_progreso.pack(pady=5)

#botones
btn_carga=tk.Button(ventana, text="iniciar progreso", command=lambda:progreso(barra_progreso, lbl_resultado))
btn_carga.pack(pady=5)

btn_reinicio=tk.Button(ventana, text="reiniciar progreso", command=lambda:reinicio(barra_progreso, lbl_resultado))
btn_reinicio.pack(pady=5)

#resultado
lbl_resultado=tk.Label(ventana, text="")
lbl_resultado.pack(pady=5)

ventana=tk.mainloop()