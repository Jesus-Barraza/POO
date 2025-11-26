from model.conexionBD import *
import hashlib

class Sesion():
    @staticmethod
    def registrar(nombre,apellidos,email,password):
        try:
            cursor.execute(
                "insert into usuarios values(null,%s,%s,%s,%s,%s)",
                (nombre,apellidos,email,password,"NOW()")
            )
            conexion.commit()
            usuario=Sesion.iniciar_sesion(email, password)
            if usuario:
               return usuario
            else:
               return None
        except:
            return None  

    @staticmethod
    def iniciar_sesion(email, contrasena):
        try:
            cursor.execute(
                "select id, nombre, apellidos from usuarios where email=%s and password=%s",
                (email,contrasena)
            )
            usuario=cursor.fetchone()
            if usuario:
                return usuario
            else:
                return None      
        except:
            return None         

class Notas():  
    @staticmethod
    def crear(usuario_id, titulo, descripcion):
        try:
          cursor.execute(
            "insert into notas values(null,%s,%s,%s,NOW())",
            (usuario_id,titulo,descripcion)
          )
          conexion.commit()
          return True
        except:
          return False

    @staticmethod
    def mostrar(usuario_id):
        try:
          cursor.execute(
            "select * from notas where usuario_id=%s",
            (usuario_id,)
          )
          return cursor.fetchall()
        except:    
          return []

    @staticmethod
    def actualizar(id, titulo, descripcion):
       try:
         cursor.execute(
            "update notas set titulo=%s,descripcion=%s where id=%s",
            (titulo,descripcion,id)
         )
         conexion.commit()
         return True
       except: 
         return False
    
    @staticmethod
    def eliminar(id):
        try:
          cursor.execute(
            "delete from notas where id=%s",
            (id,)
          ) 
          conexion.commit() 
          return True  
        except:    
          return False
        
