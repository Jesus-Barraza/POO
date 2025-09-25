'''
Método constructor - Con este método se inicializa un objeto cuando es creado con valores iniciales
'''

import os
os.system("cls")

class Coches:
    #Método constructor modo 1
    # def __init__(self):    
    #     self.__marca=""
    #     self.__color=""
    #     self.__modelo=""
    #     self.__velocidad=0
    #     self.__caballaje=0
    #     self.__plazas=0


    #Método constructor modo 2
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
    
coche1=Coches("VW", "Blanco", "2022", 220, 150, 5) #Con el método constructor el número de datos es fijo y no se puede agregar más
coche2=Coches("Nissan", "Azul", "2020", 180, 150, 6)
coche3=Coches("Honda", "", "", 0, 0, 0) #Para elementos vacíos, deja directamente el valor en blanco ("") o en 0, al menos que uses datos vacíos

#coche1.setMarca("VW")
#coche1.setColor("Blanco")
#coche1.setModelo("2022")
#coche1.setVelocidad(220)
#coche1.setCaballaje(150)
#coche1.setPlazas(5)

#coche2.setMarca("Nissan")
#coche2.setColor("Azul")
#coche2.setModelo("2020")
#coche2.setVelocidad(180)
#coche2.setCaballaje(150)
#coche2.setPlazas(6)

#coche3.setMarca("Honda")

print(f"El {coche1.getMarca()} {coche1.getColor()} aceleró de {coche1.getVelocidad()} a {coche1.acelerar(100)}!")
print(f"El {coche2.getMarca()} {coche2.getColor()} frenó de {coche2.getVelocidad()} a {coche2.frenar(150)}!")

print(f"\tDatos del vehículo: \nMarca: {coche1.getMarca()} \nColor: {coche1.getColor()} \nModelo: {coche1.getModelo()} \nVelocidad: {coche1.getVelocidad()} \nCaballaje: {coche1.getCaballaje()} \nPlaza: {coche1.getPlazas()}")
print(f"\tDatos del vehículo: \nMarca: {coche2.getMarca()} \nColor: {coche2.getColor()} \nModelo: {coche2.getModelo()} \nVelocidad: {coche2.getVelocidad()} \nCaballaje: {coche2.getCaballaje()} \nPlaza: {coche2.getPlazas()}")
print(f"\tDatos del vehículo: \nMarca: {coche3.getMarca()} \nColor: {coche3.getColor()} \nModelo: {coche3.getModelo()} \nVelocidad: {coche3.getVelocidad()} \nCaballaje: {coche3.getCaballaje()} \nPlaza: {coche3.getPlazas()}")
