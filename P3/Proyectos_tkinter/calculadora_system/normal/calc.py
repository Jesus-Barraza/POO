'''
    Crear una calculadora:
    1.- 2 campos de texto
    2.- 4* botones para las operaciones
    3.- Mostrar el resultado en una alerta
'''

#Importaciones
from funcion import Calculadora
import tkinter as tk
from tkinter import messagebox

#Controlador o controller
def operacion(n1, n2, ope):
    try:
        if ope=="suma":
            sim="+" 
            res=Calculadora.suma(n1, n2)
        elif ope=="resta":
            sim="-"
            res=Calculadora.resta(n1, n2)
        elif ope=="multiplica":
            sim="x"
            res=Calculadora.multiplicacion(n1, n2)
        elif ope=="divide":
            sim="/"
            res=Calculadora.division (n1, n2)
        elif ope=="potencia":
            sim="^"
            res=Calculadora.potenciacion(n1, n2)
        elif ope=="raiz":
            sim="√"
            res=Calculadora.raiz(n1, n2)
    except ZeroDivisionError:
        notificacion=messagebox.showerror(title="Dividir entre 0", icon="warning", message="No se puede dividir entre 0")
    else:
        mensaje=f"la {ope} {n1} {sim} {n2} es de {res}"
        notificacion=messagebox.showinfo(title="Resultado", icon="info", message=mensaje)    

#ventana
ventana=tk.Tk()
ventana.geometry("900x600")
ventana.title("Calculadora básica \U0001F5A9")
ventana.resizable(False, False)

#variables
n1=tk.IntVar()
n2=tk.IntVar()

#limitar las cajas de texto
def limit(p):
    if p.isdigit():
        return True
    elif p==".":
        return True
    else:
        return False
    
verificacion= (ventana.register(limit), "%P")

#cajas de texto
txt_numero1=tk.Entry(ventana, textvariable=n1, validatecommand=verificacion, validate="key")
txt_numero1.config(
    width=20,
    justify="right"
)
txt_numero1.pack(side="top", pady=[15,5])

txt_numero2=tk.Entry(ventana, textvariable=n2, validatecommand=verificacion, validate="key")
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
btn_suma=tk.Button(frame_btn, text="+", command=lambda:operacion(n1.get(), n2.get(), "suma"))
btn_suma.config(
    width=5
)
btn_suma.grid(row=0, column=0, padx=5, pady=5)

btn_resta=tk.Button(frame_btn, text="-", command=lambda:operacion(n1.get(), n2.get(), "resta"))
btn_resta.config(
    width=5
)
btn_resta.grid(row=0, column=1, padx=5, pady=5)

btn_multi=tk.Button(frame_btn, text="x", command=lambda:operacion(n1.get(), n2.get(), "multiplica"))
btn_multi.config(
    width=5
)
btn_multi.grid(row=1, column=0, padx=5, pady=5)

btn_divi=tk.Button(frame_btn, text="/", command=lambda:operacion(n1.get(), n2.get(), "divide"))
btn_divi.config(
    width=5
)
btn_divi.grid(row=1, column=1, padx=5, pady=5)

btn_potencia=tk.Button(frame_btn, text="^", command=lambda:operacion(n1.get(), n2.get(), "potencia"))
btn_potencia.config(
    width=5
)
btn_potencia.grid(row=2, column=0, padx=5, pady=5)

btn_raiz=tk.Button(frame_btn, text="√", command=lambda:operacion(n1.get(), n2.get(), "raiz"))
btn_raiz.config(
    width=5
)
btn_raiz.grid(row=2, column=1, padx=5, pady=5)

btn_boton=tk.Button(ventana, text="Salir del programa", command=ventana.quit)
btn_boton.pack(pady=15)

ventana=tk.mainloop()