from model.operaciones import Sesion, Notas
import hashlib
from tkinter import messagebox

class Usuarios():
    @staticmethod
    def codigo(contrasena):
        contra=hashlib.sha256(contrasena.encode()).hexdigest()
        return contra

    @staticmethod
    def inicio_sesion(correo, contra):
        contra=Usuarios.codigo(contra)
        user=Sesion.iniciar_sesion(correo, contra)
        if user:
            return user
        else:
            noti=messagebox.showerror(title="Inicio-sesión", message="No se ha encontrado el usuario correspondiente")
            return None

    @staticmethod
    def registrar(ventana, nombre, apellido, correo, contra):
        contra=Usuarios.codigo(contra)
        regi=Sesion.registrar(nombre, apellido, correo, contra)
        if regi:
            return regi
        else:
            noti=messagebox.showerror(title="Registro", message="No se ha podido registrar al usuario, inténtelo más tarde")
            return None
        
class OpeNotas():
    def __init__(self, usuarioid, titulo, descripcion):
        self.crear_nota(usuarioid, titulo, descripcion)
        
    @staticmethod
    def crear_nota(usuarioid, titulo, descripcion):
        regi=Notas.crear(usuarioid, titulo, descripcion)
        if regi:
            noti=messagebox.showinfo(title="Registro de notas", message="Se agregó la nota con éxito", icon="info")
        else:
            noti=messagebox.showerror(title="Registro de notas", message="Se ha producido un error, inténtelo más tarde")
        return regi
    
    @staticmethod
    def mostrar_nota(usuarioid):
        regi=Notas.mostrar(usuarioid)
        return regi