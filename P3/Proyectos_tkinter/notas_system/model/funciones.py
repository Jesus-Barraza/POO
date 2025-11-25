from controller.operaciones import Sesion, Notas
import hashlib
from tkinter import messagebox

class Usuarios():
    @staticmethod
    def codigo(contrasena):
        contra=hashlib.sha256(contrasena.encode()).hexdigest()
        return contra

    @staticmethod
    def inicio_sesion(ventana, correo, contra):
        contra=Usuarios.codigo(contra)
        user=Sesion.iniciar_sesion(correo, contra)
        if user:
            return True
        else:
            noti=messagebox.showerror(title="Inicio-sesión", message="No se ha encontrado el usuario correspondiente")

    @staticmethod
    def registrar(ventana, nombre, apellido, correo, contra):
        contra=Usuarios.codigo(contra)
        regi=Sesion.registrar(nombre, apellido, correo, contra)
        if regi:
            return True
        else:
            noti=messagebox.showerror(title="Registro", message="No se ha podido registrar al usuario, inténtelo más tarde")
            

