#Importaciones
import tkinter as tk
from tkinter import messagebox
from controller import funciones

class App():
    def __init__(self):
        self.menu_calculadora()

    def menu_calculadora(self):
        #ventana
        ventana=tk.Tk()
        ventana.geometry("900x600")
        ventana.title("Calculadora básica \U0001F5A9")
        ventana.resizable(False, False)

        #variables
        n1=tk.IntVar()
        n2=tk.IntVar()

        #cajas de texto
        txt_numero1=tk.Entry(ventana, textvariable=n1)
        txt_numero1.config(
            width=20,
            justify="right"
        )
        txt_numero1.pack(side="top", pady=[15,5])

        txt_numero2=tk.Entry(ventana, textvariable=n2)
        txt_numero2.config(
            width=20,
            justify="right"
        )
        txt_numero2.pack(side="top", pady=[5,15])

        #matriz
        frame_btn=tk.Frame(ventana)
        frame_btn.config(
            width=400,
            height=200
        )
        frame_btn.pack(pady=5)

        #botones
        btn_suma=tk.Button(frame_btn, text="+", command=lambda:funciones.mensajes.suma(n1.get(), n2.get()))
        btn_suma.config(
            width=5
        )
        btn_suma.grid(row=0, column=0, padx=5, pady=5)

        btn_resta=tk.Button(frame_btn, text="-", command=lambda:funciones.mensajes.resta(n1.get(), n2.get()))
        btn_resta.config(
            width=5
        )
        btn_resta.grid(row=0, column=1, padx=5, pady=5)

        btn_multi=tk.Button(frame_btn, text="x", command=lambda:funciones.mensajes.multiplicacion(n1.get(), n2.get()))
        btn_multi.config(
            width=5
        )
        btn_multi.grid(row=1, column=0, padx=5, pady=5)

        btn_divi=tk.Button(frame_btn, text="/", command=lambda:funciones.mensajes.division(n1.get(), n2.get()))
        btn_divi.config(
            width=5
        )
        btn_divi.grid(row=1, column=1, padx=5, pady=5)

        btn_potencia=tk.Button(frame_btn, text="^", command=lambda:funciones.mensajes.potencia(n1.get(), n2.get()))
        btn_potencia.config(
            width=5
        )
        btn_potencia.grid(row=2, column=0, padx=5, pady=5)

        btn_raiz=tk.Button(frame_btn, text="√", command=lambda:funciones.mensajes.raiz(n1.get(), n2.get()))
        btn_raiz.config(
            width=5
        )
        btn_raiz.grid(row=2, column=1, padx=5, pady=5)

        btn_boton=tk.Button(ventana, text="Salir del programa", command=ventana.quit)
        btn_boton.pack(pady=15)

        ventana=tk.mainloop()