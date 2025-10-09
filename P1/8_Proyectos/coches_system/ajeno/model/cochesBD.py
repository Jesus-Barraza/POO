from conexionBD import *

#Forma 1
class Autos:
    def __init__(self,marca,color,modelo,velocidad,caballaje,plazas):
        self._marca=marca
        self._color=color
        self._modelo=modelo
        self._velocidad=velocidad
        self._caballaje=caballaje
        self._plazas=plazas

    def insertar(self):
        try:
           cursor.execute(
               "insert into autos values(null,%s,%s,%s,%s,%s,%s)",
               (self._marca,self._color,self._modelo,self._velocidad,self._caballaje,self._plazas)
            )
           conexion.commit()
           return True
        except:  
           return False   


#Forma 2
class Camionetas():

    @staticmethod
    def insertar (marca,color,modelo,velocidad,caballaje,plazas,traccion,cerrada):
        try:
            cursor.execute(
                "insert into camionetas values(null,%s,%s,%s,%s,%s,%s,%s,%s)",
               (marca,color,modelo,velocidad,caballaje,plazas,traccion,cerrada)
            )
            conexion.commit()
            return True
        except:
            return False

class Camiones():

    @staticmethod
    def insertar(marca,color,modelo,velocidad,caballaje,plazas,ejes,capacidadCarga):
        try:
            cursor.execute(
                "insert into camiones values(null,%s,%s,%s,%s,%s,%s,%s,%s)",
               (marca,color,modelo,velocidad,caballaje,plazas,ejes,capacidadCarga)
            )
            conexion.commit()
            return True
        except:
            return False