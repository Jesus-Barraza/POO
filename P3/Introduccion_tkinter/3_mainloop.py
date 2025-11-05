#Importaciones
import tkinter as tk

#Ventana
ventana=tk.Tk()
ventana.geometry("600x400")
ventana.title("Uso del mainloop \U0001F5FF")

#Marcos
rojo=tk.Frame(ventana, width=600, height=67, bg="#ff0000", relief="raised", border=5).pack()
naranja=tk.Frame(ventana, width=600, height=67, bg="#ffaa00", relief="raised", border=5).pack()
amarillo=tk.Frame(ventana, width=600, height=67, bg="#ffff00", relief="raised", border=5).pack()
verde=tk.Frame(ventana, width=600, height=67, bg="#00ff00", relief="raised", border=5).pack()
azul=tk.Frame(ventana, width=600, height=67, bg="#0000ff", relief="raised", border=5).pack()
morado=tk.Frame(ventana, width=600, height=67, bg="#aa00ff", relief="raised", border=5).pack()

#Fin del loop
ventana.mainloop()