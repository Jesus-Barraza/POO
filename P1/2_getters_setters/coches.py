'''
Crear los métodos setters y getters. Estos métodos son importante y necesarios en todas las clases para que el programador interactúe con los valores de los atributos a travéz de estos métodos.
Digamos que es la manera más adecuada y recomendada para solicitar un valor (get) y/o para ingresar o cambiar un valor (set) a un atributo en particular de la clase a través de un objetos.

En teoría se debería de crear un método getter y setter por cada atributo que contenga la clase.

Los métodos get siempre regresan valor, es decir el valor de la propiedad a través del return

Por otro lado, el método set siempre recibe parámetros para cambiar o modificar el valor del atributo o propiedad en cuestión
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

    #Forma 1
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

    #Forma 2
    @property
    def marca(self):
        return self.__marca
    @marca.setter
    def marca(self,mar):
        self.__marca=mar
    
    @property
    def color(self):
        return self.__color
    @color.setter
    def color(self,col):
        self.__color=col

    @property
    def modelo(self):
        return self.__modelo
    @modelo.setter
    def modelo(self,mod):
        self.__modelo=mod

    @property
    def velocidad(self):
        return self.__velocidad
    @velocidad.setter
    def velocidad(self,vel):
        self.__velocidad=vel

    @property
    def caballaje(self):
        return self.__caballaje
    @caballaje.setter
    def caballaje(self,cab):
        self.__caballaje=cab

    @property
    def plazas(self):
        return self.__plazas
    @plazas.setter
    def plazas(self,pla):
        self.__plazas=pla


    def acelerar(self,ace):
        self.__velocidad+=ace
        return self.__velocidad

    def frenar(self,fre):
        self.__velocidad-=fre
        return self.__velocidad
    
coche1=Coches()
coche2=Coches()
#coche3=Coches()

#coche1.marca="VW"
#coche1.color="Blanco"
#coche1.modelo="2022"
#coche1.velocidad=220
#coche1.caballaje=150
#coche1.plazas=5

coche1.setMarca("VW")
coche1.setColor("Blanco")
coche1.setModelo("2022")
coche1.setVelocidad(220)
coche1.setCaballaje(150)
coche1.setPlazas(5)

#coche2.marca="Nissan"
#coche2.color="Azul"
#coche2.modelo="2020"
#coche2.velocidad=180
#coche2.caballaje=150
#coche2.plazas=6

coche2.marca="Nissan"
coche2.color="Azul"
coche2.modelo="2020"
coche2.velocidad=180
coche2.caballaje=150
coche2.plazas=6

#coche3.modelo="Honda"

print(f"El {coche1.getMarca()} {coche1.getColor()} aceleró de {coche1.getVelocidad()} a {coche1.acelerar(100)}!")
print(f"El {coche2.getMarca()} {coche2.getColor()} frenó de {coche2.getVelocidad()} a {coche2.frenar(50)}!")

print(f"\tDatos del vehículo: \nMarca: {coche1.getMarca()} \nColor: {coche1.getColor()} \nModelo: {coche1.getModelo()} \nVelocidad: {coche1.getVelocidad()} \nCaballaje: {coche1.getCaballaje()} \nPlaza: {coche1.getPlazas()}")
print(f"\tDatos del vehículo: \nMarca: {coche2.marca} \nColor: {coche2.color} \nModelo: {coche2.modelo} \nVelocidad: {coche2.velocidad} \nCaballaje: {coche2.caballaje} \nPlaza: {coche2.plazas}")