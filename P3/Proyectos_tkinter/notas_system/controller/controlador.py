from model.operaciones import Sesion, Notas
import hashlib
from tkinter import messagebox
from view.interfaz import *

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
    @staticmethod
    def alerta(notificacion):
        if notificacion:
            noti=messagebox.showinfo(title="Registro de notas", message=f"La operación se realizó con éxito")
        else:
            noti=messagebox.showerror(title="Registro de notas", message=f"Se ha producido un error, inténtelo más tarde")


    @staticmethod
    def crear_nota(usuarioid, titulo, descripcion):
        regi=Notas.crear(usuarioid, titulo, descripcion)
        OpeNotas.alerta(regi)
        return regi
    
    @staticmethod
    def mostrar_nota(usuarioid):
        regi=Notas.mostrar(usuarioid)
        return regi
    
    @staticmethod
    def modificar_nota(id, titulo, descripcion):
        regi=Notas.actualizar(id, titulo, descripcion)
        OpeNotas.alerta(regi)
        return regi
    
    @staticmethod
    def eliminar_nota(id):
        regi=Notas.eliminar(id)
        OpeNotas.alerta(regi)
        return regi