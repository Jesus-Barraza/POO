#Importaciones
import math
from tkinter import messagebox 
from model import operaciones
from model.conexionDB import result

#Controlador o controller
class mensajes():
    @staticmethod
    def respuesta_sql(respuesta):
        if respuesta:
            notificacion=messagebox.showinfo(title="Resultado", message="La operación se ha realizado con éxito")
        elif respuesta=="Zero":
            notificacion=messagebox.showerror(title="Dividir entre 0", icon="warning", message="No se puede dividir entre 0")
        else:
            notificacion=messagebox.showinfo(title="Resultado", message="Se ha cancelado la operación con éxito")

    @staticmethod
    def operaciones(n1, n2, sim):
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
            except ZeroDivisionError as error:
                return False
            else:
                return [n1, n2, sim, res]

    @staticmethod
    def insertarDato(n1, n2, sim):
        ope=mensajes.operaciones(float(n1), float(n2), sim)
        if ope:
            mensaje=f"la operación {ope[0]} {ope[2]} {ope[1]} es de {ope[3]}"
            notificacion=messagebox.showinfo(title="Resultado", icon="info", message=mensaje)
            if result:
                resultado=messagebox.askquestion(message="\n¿Quieres guardar la operación en la BD?", icon="question", title="Base de datos")
                if resultado=="yes":
                    entrada=operaciones.Operaciones(n1,n2,sim,ope[3])
                    mensajes.respuesta_sql(True)
        else:
            divisionzero=messagebox.showerror(title="Dividir entre 0", message="No se puede dividir un número entre 0")
                    

    @staticmethod
    def eliminarDato(id):
        if result:
            if id:
                aviso=messagebox.askquestion(title="CUIDADO!", icon="warning", message=f"\n ¿Desea borrar la operación {id}?")
                if aviso=="yes":
                    operaciones.Operaciones.eliminar(id)
                    mensajes.respuesta_sql(True)
                else:
                    mensajes.respuesta_sql(False)
            else:
                sinid=messagebox.showwarning(title="No introdujo una ID", message="No hay una ID válida para cambiar")
        else:
            error=messagebox.showerror(title="No hay conexión", message="No se puede conectar a la BD, inténtelo más tarde")

    @staticmethod
    def cambiarDato(id, n1, n2, sim):
        ope=mensajes.operaciones(float(n1), float(n2), sim)
        if ope:
            if result:
                if id:
                    operaciones.Operaciones.actualizar(id, n1, n2, sim, ope[3])
                    mensajes.respuesta_sql(True)
                else:
                    sinid=messagebox.showwarning(title="No introdujo una ID", message="No hay una ID válida para cambiar")
            else:
                mensajes.respuesta_sql(False)
        else:
            divisionzero=messagebox.showerror(title="Dividir entre 0", message="No se puede dividir un número entre 0")