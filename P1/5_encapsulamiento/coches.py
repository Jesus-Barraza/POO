import os
os.system("cls")

class Coches:
    def __init__(self,mar,col,mod,vel,cab,pla):    
        self.__marca=mar
        self.__color=col
        self.__modelo=mod
        self.__velocidad=vel
        self.__caballaje=cab
        self.__plazas=pla

    def getMarca(self):
        return self.__marca
    def setMarca(self,mar):
        self.__marca=mar

    def getColor(self):
        return self.__color
    def setColor(self,col):
        self.__color=col

    def getModelo(self):
        return self.__modelo
    def setModelo(self,mod):
        self.__modelo=mod

    def getVelocidad(self):
        return self.__velocidad
    def setVelocidad(self,vel):
        self.__velocidad=vel

    def getCaballaje(self):
        return self.__caballaje
    def setCaballaje(self,cab):
        self.__caballaje=cab     

    def getPlazas(self):
        return self.__plazas
    def setPlazas(self,pla):
        self.__plazas=pla


    def acelerar(self,ace):
        self.__velocidad+=ace
        return self.__velocidad

    def frenar(self,fre):
        self.__velocidad-=fre
        return self.__velocidad
    
