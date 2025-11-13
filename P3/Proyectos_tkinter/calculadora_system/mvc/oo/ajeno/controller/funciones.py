#Importaciones
import math
from tkinter import messagebox 
from model import operaciones


#Controlador o controller
class mensajes():
    @staticmethod
    def operacion(n1, n2, sim):
        try:
            if sim=="+":
                res=n1+n2
            elif sim=="-":
                res=n1-n2
            elif sim=="x":
                res=n1*n2
            elif sim=="/":
                res=n1/n2
            elif sim=="^":
                res=n1**n2
            elif sim=="√":
                res=n1**(1/n2)
        except ZeroDivisionError:
            notificacion=messagebox.showerror(title="Dividir entre 0", icon="warning", message="No se puede dividir entre 0")
        else:
            mensaje=f"la operación {n1} {sim} {n2} es de {res}"
            entrada=operaciones.Operaciones(n1,n2,sim,res)
            if entrada:
                notificacion=messagebox.showinfo(title="Resultado", icon="info", message=mensaje) 
            else:
                notificacion=messagebox.showinfo(title="Resultado (SIN GUARDAR)", icon="info", message=mensaje)