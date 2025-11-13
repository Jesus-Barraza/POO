#Importaciones
import math
from tkinter import messagebox 


#Controlador o controller
class mensajes():
    @staticmethod
    def suma(n1, n2):
        mensaje=f"la suma {n1} + {n2} es de {n1+n2}"
        notificacion=messagebox.showinfo(message=mensaje, icon="info", title="Resultado de la suma (+)")

    @staticmethod
    def resta(n1, n2):
        mensaje=f"la resta {n1} - {n2} es de {n1-n2}"
        notificacion=messagebox.showinfo(message=mensaje, icon="info", title="Resultado de la resta (-)")

    @staticmethod
    def multiplicacion(n1, n2):
        mensaje=f"la multiplicacion {n1} x {n2} es de {n1*n2}"
        notificacion=messagebox.showinfo(message=mensaje, icon="info", title="Resultado de la multiplicacion (x)")

    @staticmethod
    def division(n1, n2):
        try:
            mensaje=f"la division {n1} / {n2} es de {n1/n2}"
            notificacion=messagebox.showinfo(message=mensaje, icon="info", title="Resultado de la division (/)")
        except ZeroDivisionError:
            notificacion=messagebox.showwarning(title="División de 0", message="No se puede dividir un número entre 0", icon="warning")

    @staticmethod
    def potencia(n1, n2):
        mensaje=f"la potencia {n1} ^ {n2} es de {n1**n2}"
        notificacion=messagebox.showinfo(message=mensaje, icon="info", title="Resultado de la potencia (^)")

    @staticmethod
    def raiz(n1, n2):
        try:
            mensaje=f"la raiz {n2} √ {n1} es de {n1**(1/n2)}"
            notificacion=messagebox.showinfo(message=mensaje, icon="info", title="Resultado de la raiz (√)")
        except:
            notificacion=messagebox.showwarning(title="Potencia al infinito", message="No se puede potenciar un número al infinito", icon="warning")
