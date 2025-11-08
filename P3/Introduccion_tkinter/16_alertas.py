import tkinter as tk
from tkinter import messagebox

#Ventana
ventana=tk.Tk()
ventana.geometry("500x500")
ventana.title("Imagenes \u23F0")

def alerta1():
    nombreObtenido=cadena.get()
    etiqueta.config(text=f"{nombreObtenido}")
    resultado=messagebox.showinfo(message=f"{nombreObtenido}",icon="INFFO")

def alerta2():
    resultado=messagebox.askquestion(message="¿Quires continuar ejecutando la aplicación?",icon="question")
    if resultado!="yes":
        ventana.destroy()
    
   

cadena=tk.StringVar()
caja1=tk.Entry(ventana, textvariable=cadena)
caja1.pack()

boton1=tk.Button(ventana, text="Alerta", command=alerta1)
boton1.pack()


boton2=tk.Button(ventana, text="Otra Alerta", command=alerta2)
boton2.pack()

etiqueta=tk.Label(ventana, text="")
etiqueta.pack()


ventana=tk.mainloop()