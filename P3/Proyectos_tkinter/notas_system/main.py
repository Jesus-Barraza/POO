'''
1-Paradigma OO
2-Implementar el MVC
3-App de escritorio con interfaz gráfica
'''
from view.interfaz import *
import tkinter as tk

class App():
   def __init__(self, ventana):
      Interfaz(ventana)

if __name__ == "__main__":
   ventana=tk.Tk()
   app=App(ventana)
   ventana=tk.mainloop()
