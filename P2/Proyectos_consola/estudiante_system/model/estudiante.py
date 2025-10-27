'''Realizar un programa que conste de una clase llamada Estudiante, que tenga como atributos el nombre y la nota del alumno. Definir los métodos para inicializar sus atributos, imprimirlos y mostrar un mensaje con el resultado de la nota y si ha aprobado o no'''
from conexionDB import *

class Estudiante():
#    def __init__(self, nombre, nota):
#        self._nombre=nombre
#        self._nota=nota

#    @property
#    def nombre(self):
#        return self._nombre
#    @nombre.setter
#    def nombre(self,nom):
#        self._nombre=nom

#    @property
#    def nota(self):
#        return self._nota
#    @nota.setter
#    def nota(self,note):
#        self._nota=note


    @staticmethod
    def evaluacion(nota):
        if nota >=7.0 and nota<=10.0:
            return "APROBATORIA"
        elif nota>=0.0 and nota<7.0:
            return "REPROBATORIA"
        else:
            return "INVÁLIDA"
    
    @staticmethod
    def impresion(ld):
        try:
            cursor.execute(
                "select nombre,nota from estudiante where id=%s",
                (ld,)
            )
            alumno=cursor.fetchone()
        except:
            print("Ocurrió un error al obtener el alumno, inténtelo más tarde")
        else:
            resultado=Estudiante.evaluacion(alumno[1])
            print(f"La calificación {alumno[1]} de {alumno[0]} es {resultado}")

    @staticmethod
    def insertar(nombre,nota):
        try:
            cursor.execute(
            "insert into estudiante values(null,%s,%s)",
            (nombre,nota)
          )
            conexion.commit()
            return True
        except:
            return False

    @staticmethod
    def mostrar():
        cursor.execute(
            "select * from estudiante"
        )
        print(cursor.fetchall())

    @staticmethod
    def actualizar(nombre,nota,id):
        try:
            cursor.execute(
                "update estudiante set nombre=%s, nota=%s where id=%s",
                (nombre,nota,id)
            )
            conexion.commit()
            return True
        except:
            return False

    @staticmethod
    def eliminar(id):
        try:
            cursor.execute(
            "delete from estudiante where id=%s",
            (id,)
          )
            conexion.commit()
            return True
        except:
            return False