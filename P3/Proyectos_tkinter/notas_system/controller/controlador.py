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
            noti=messagebox.showinfo(title="Inicio-sesión", message=f"{user[1]} {user[2]}, has iniciado sesión correctamente")
            return user
        else:
            noti=messagebox.showerror(title="Inicio-sesión", message="No se ha encontrado el usuario correspondiente")
            return None

    @staticmethod
    def registrar(ventana, nombre, apellido, correo, contra):
        contra=Usuarios.codigo(contra)
        regi=Sesion.registrar(nombre, apellido, correo, contra)
        if regi:
            noti=messagebox.showinfo(title="Inicio-sesión", message=f"{regi[1]} {regi[2]}, has registrado correctamente")
            return regi
        else:
            noti=messagebox.showerror(title="Registro", message="No se ha podido registrar al usuario, inténtelo más tarde")
            return None
        
class OpeNotas():
    def __init__(self, titulo, descripcion):
        self.crear_nota(titulo, descripcion)
        
    @staticmethod
    def alerta(notificacion):
        if notificacion:
            noti=messagebox.showinfo(title="Registro de notas", message=f"{nombres} {apellido}, La operación se realizó con éxito")
        else:
            noti=messagebox.showerror(title="Registro de notas", message=f"{nombres} {apellido}, Se ha producido un error, inténtelo más tarde")


    @staticmethod
    def crear_nota(usuarioid, titulo, descripcion):
        regi=Notas.crear(usuarioid, titulo, descripcion)
        OpeNotas.alerta(regi)
        return regi

    
    @staticmethod
    def mostrar_nota(usuarioid):
        regi=Notas.mostrar(usuarioid)
        return regi
    

    def modificar_nota(id, titulo, descripcion):
        regi=Notas.actualizar(id, titulo, descripcion)
        OpeNotas.alerta(regi)
        return regi
    
    @staticmethod
    def eliminar_nota(id):
        regi=Notas.eliminar(id)
        OpeNotas.alerta(regi)
        return regi