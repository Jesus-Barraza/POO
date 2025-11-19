#Importaciones
import math
from tkinter import messagebox 
from model import operaciones
from model.conexionDB import result

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
            #entrada=operaciones.Operaciones(n1,n2,sim,res)
            #if entrada:
                #notificacion=messagebox.showinfo(title="Resultado", icon="info", message=mensaje) 
            #else:
            #    notificacion=messagebox.showinfo(title="Resultado (SIN GUARDAR)", icon="info", message=mensaje)
            notificacion=messagebox.showinfo(title="Resultado", icon="info", message=mensaje)
            if result:
                resultado=messagebox.askquestion(message="\n¿Quieres guardar la operación en la BD?", icon="question", title="Base de datos")
                if resultado=="yes":
                    entrada=operaciones.Operaciones(n1,n2,sim,res)
                    notificacion=messagebox.showinfo(title="Resultado", message="La operación ha sido guardado con éxito")

    @staticmethod
    def eliminarDato(id):
        if result:
            if id:
                aviso=messagebox.askquestion(title="CUIDADO!", icon="warning", message=f"\n ¿Desea borrar la operación {id}?")
                if aviso=="yes":
                    operaciones.Operaciones.eliminar(id)
                    notificacion=messagebox.showinfo(title="Resultado", message=f"Se borró el registro {id} con éxito")
                else:
                    notificacion=messagebox.showinfo(title="Resultado", message="Se ha cancelado la operación con éxito")