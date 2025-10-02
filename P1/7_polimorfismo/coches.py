import os
os.system("cls")

class Coches:
    def __init__(self,mar,col,mod,vel,cab,pla):    
        self._marca=mar
        self._color=col
        self._modelo=mod
        self._velocidad=vel
        self._caballaje=cab
        self._plazas=pla

    @property
    def Marca(self):
        return self._marca
    @Marca.setter
    def Marca(self,mar):
        self._marca=mar

    @property
    def Color(self):
        return self._color
    @Color.setter
    def Color(self,col):
        self._color=col

    @property
    def Modelo(self):
        return self._modelo
    @Modelo.setter
    def Modelo(self,mod):
        self._modelo=mod

    @property
    def Velocidad(self):
        return self._velocidad
    @Velocidad.setter
    def Velocidad(self,vel):
        self._velocidad=vel

    @property
    def Caballaje(self):
        return self._caballaje
    @Caballaje.setter
    def Caballaje(self,cab):
        self._caballaje=cab     

    @property
    def Plazas(self):
        return self._plazas
    @Plazas.setter
    def setPlazas(self,pla):
        self._plazas=pla


    def acelerar(self,ace):
        self._velocidad+=ace
        return f"El carro aceleró a {self._velocidad}"

    def frenar(self,fre):
        self._velocidad-=fre
        return f"El carro frenó a {self._velocidad}"
    
class Camiones(Coches):
    def __init__ (self,mar,col,mod,vel,cab,pla,eje,cap):
        super().__init__(mar,col,mod,vel,cab,pla)
        self.__eje=eje
        self.__capacidad=cap

    @property
    def Eje(self):
        return self.__eje
    @Eje.setter
    def Eje(self,eje):
        self.__eje=eje

    @property
    def CapacidadCarga(self):
        return self.__capacidad
    @CapacidadCarga.setter
    def CapacidadCarga(self,cap):
        self.__capacidad=cap


    def cargar(self,tipo):
        self.__tipo_carga=tipo
        return self.__tipo_carga
    
    def acelerar(self,ace):
        self._velocidad+=ace
        return f"El camión aceleró a {self._velocidad}"

    def frenar(self,fre):
        self._velocidad-=fre
        return f"El camión frenó a {self._velocidad}"
    
class Camionetas(Coches):
    def __init__ (self,mar,col,mod,vel,cab,pla,trac,clo):
        super().__init__(mar,col,mod,vel,cab,pla)
        self.__traccion=trac
        self.__cerrada=clo

    @property
    def Tracción(self):
        return self.__traccion
    @Tracción.setter
    def Eje(self,tra):
        self.__traccion=tra

    @property
    def Cerrado(self):
        return self.__cerrada
    @Cerrado.setter
    def Cerrado(self,cer):
        self.__cerrada=cer


    def transportar(self,pas):
        self.__pasajeros=pas
        return self.__pasajeros
    
    def acelerar(self,ace):
        self._velocidad+=ace
        return f"La camioneta aceleró a {self._velocidad}"

    def frenar(self,fre):
        self._velocidad-=fre
        return f"La camioneta frenó a {self._velocidad}"