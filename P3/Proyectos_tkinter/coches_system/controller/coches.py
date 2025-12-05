import os
from model import cochesBD
from tkinter import messagebox

class Coches:
    def __init__(self,marca,color,modelo,velocidad,caballaje,plazas):
       self._marca=marca
       self._color=color
       self._modelo=modelo
       self._velocidad=velocidad
       self._caballaje=caballaje
       self._plazas=plazas
 
    @property
    def marca(self):
       return self._marca
    
    @marca.setter
    def marca(self,marca):
       self._marca=marca
    
    @property
    def color(self):
       return self._color
    
    @color.setter
    def color(self,color):
       self._color=color 

    @property
    def modelo(self):
       return self._modelo

    @modelo.setter
    def modelo(self,modelo):
       self._modelo=modelo

    @property
    def velocidad(self):
       return self._velocidad

    @velocidad.setter
    def velocidad(self,velocidad):
       self._velocidad=velocidad 

    @property
    def caballaje(self):
       return self._caballaje

    @caballaje.setter
    def caballaje(self,caballaje):
       self._caballaje=caballaje

    @property
    def plazas(self):
       return self._plazas

    @plazas.setter
    def plazas(self,plazas):
       self._plazas=plazas                   

    def acelerar(self):
      return "Estas acelerando el coche"

    def frenar(self):
      return "Estas frenando el coche"  


class Camiones(Coches):
   def __init__(self,marca,color,modelo,velocidad,caballaje,plazas,eje,capacidadCarga):
      super().__init__(marca,color,modelo,velocidad,caballaje,plazas)
      self.__eje=eje
      self.__capacidadCarga=capacidadCarga
   
   def cargar(self,tipo_carga):
      self.tipo_carga=tipo_carga
      return self.tipo_carga
   
   def acelerar(self):
       return "Estas acelerando el camion"
   
   def frenar(self):
       return "Estas frenando el camion" 

   @property
   def eje(self):
      return self.__eje
   
   @eje.setter
   def eje(self,eje):
      self.__eje=eje
   
   @property
   def capacidadCarga(self):
      return self.__capacidadCarga
   
   @capacidadCarga.setter
   def capacidadCarga(self,capacidadCarga):
      self.__capacidadCarga=capacidadCarga
      
   
class Camionetas(Coches):
   def __init__(self,marca,color,modelo,velocidad,caballaje,plazas,traccion,cerrada):
      super().__init__(marca,color,modelo,velocidad,caballaje,plazas)
      self.__traccion=traccion
      self.__cerrada=cerrada
   
   def transportar(self,num_pasajeros):
      self.num_pasajeros=num_pasajeros
      return self.num_pasajeros
   
   def acelerar(self):
      return "Estas acelerando la camioneta"
   
   def frenar(self):
      return "Estas frenando la camioneta" 

   @property
   def traccion(self):
      return self.__traccion
   
   @traccion.setter
   def eje(self,traccion):
      self.__traccion=traccion
   
   @property
   def cerrada(self):
      return self.__cerrada
   
   @cerrada.setter
   def cerrada(self,cerrada):
      self.__cerrada=cerrada
   
class funciones():
   @staticmethod
   def respuesta_sql(respuesta):
      if respuesta:
            result=messagebox.showinfo(title="Status", message="Se realizó la acción exitosamente")
      else:
            result=messagebox.showerror(title="Status", message="No se pudo realizar la acción, inténtelo más tarde")


   @staticmethod
   def insertar_vehiculo(tipo,nombre,color,modelo,velocidad,potencia,plaza,extra1,extra2):
      if tipo=="autos":
         resp=cochesBD.Autos.insertar(nombre,color,modelo,velocidad,potencia,plaza)
      elif tipo=="camionetas":
         resp=cochesBD.Camionetas.insertar(nombre,color,modelo,velocidad,potencia,plaza,extra1,extra2)
      elif tipo=="camiones":
         resp=cochesBD.Camiones.insertar(nombre,color,modelo,velocidad,potencia,plaza,extra1,extra2)
      funciones.respuesta_sql(resp)
      if resp:
         return resp
   
   @staticmethod
   def buscar_vehiculo(ide, tipo):
      if ide:
         resp=cochesBD.Base_datos.buscar(ide, tipo)
         if resp:
            funciones.respuesta_sql(resp)
            return True
         else:
            funciones.respuesta_sql(resp)
            return False
      else:
          nada=messagebox.showwarning(title="Status", message="Introduzca una ID")
   
   @staticmethod
   def actualizar_vehiculo(tipo,nombre,color,modelo,velocidad,potencia,plaza,extra1,extra2,ide):
      if ide:
         if tipo=="autos":
            resp=cochesBD.Autos.actualizar(nombre,color,modelo,velocidad,potencia,plaza,ide)
         elif tipo=="camionetas":
            resp=cochesBD.Camionetas.actualizar(nombre,color,modelo,velocidad,potencia,plaza,extra1,extra2,ide)
         elif tipo=="camiones":
            resp=cochesBD.Camiones.actualizar(nombre,color,modelo,velocidad,potencia,plaza,extra1,extra2,ide)
         funciones.respuesta_sql(resp)
         if resp:
            return resp
      else:
          romper=messagebox.showwarning(title="No hay ID", message="No se introdujo una ID")
   
   @staticmethod
   def eliminar_vehiculo(tipo, ide):
      if ide:
         cuidao=messagebox.askyesno(title="Eliminar un vehículo", message="¡Cuidado! ¿Deseas eliminar el vehículo?")
         if cuidao==True:
            if tipo=="autos":
               resp=cochesBD.Autos.eliminar(ide)
            elif tipo=="camionetas":
               resp=cochesBD.Camionetas.eliminar(ide)
            elif tipo=="camiones":
               resp==cochesBD.Camiones.eliminar(ide)
            funciones.respuesta_sql(resp)
            if resp:
               return resp
         else:
             cancelar=messagebox.showinfo(title="Eliminar vehículo", message="Se ha cancelado la operación con éxito")
      else:
         romper=messagebox.showwarning(title="No hay ID", message="No se introdujo una ID")