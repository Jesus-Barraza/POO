'''
Los múltiples objetos utilizan más de un objeto
'''

import os
os.system("cls")

class Coches:
    __marca=""
    __color=""
    __modelo=""
    __velocidad=0
    __caballaje=0
    __plazas=0

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

#Múltiples objetos
coche1=Coches()
coche2=Coches()
coche3=Coches()

coche1.setMarca("VW")
coche1.setColor("Blanco")
coche1.setModelo("2022")
coche1.setVelocidad(220)
coche1.setCaballaje(150)
coche1.setPlazas(5)
coche1.num_serie="BTCRG590ZM0R" #Sin constructor, puedes meter datos aleatorios

coche2.setMarca("Nissan")
coche2.setColor("Azul")
coche2.setModelo("2020")
coche2.setVelocidad(180)
coche2.setCaballaje(150)
coche2.setPlazas(6)

coche3.setMarca("Honda")

print(f"El {coche1.getMarca()} {coche1.getColor()} aceleró de {coche1.getVelocidad()} a {coche1.acelerar(100)}!")
print(f"El {coche2.getMarca()} {coche2.getColor()} frenó de {coche2.getVelocidad()} a {coche2.frenar(50)}!")

print(f"\tDatos del vehículo: \nMarca: {coche1.getMarca()} \nColor: {coche1.getColor()} \nModelo: {coche1.getModelo()} \nVelocidad: {coche1.getVelocidad()} \nCaballaje: {coche1.getCaballaje()} \nPlaza: {coche1.getPlazas()}")
print(f"\tDatos del vehículo: \nMarca: {coche2.getMarca()} \nColor: {coche2.getColor()} \nModelo: {coche2.getModelo()} \nVelocidad: {coche2.getVelocidad()} \nCaballaje: {coche2.getCaballaje()} \nPlaza: {coche2.getPlazas()}")

print(f"\n{coche3.getMarca()}")