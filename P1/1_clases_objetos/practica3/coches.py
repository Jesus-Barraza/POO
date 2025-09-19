'''class Coches:
    __marca=""
    __color=""
    __modelo=""
    __velocidad=0
    __caballaje=0
    __plazas=0
    def acelerar(self,ace):
        self.__velocidad+=ace
        return self.__velocidad

    def frenar(self,fre):
        self.__velocidad-=fre
        return self.__velocidad
    
coche1=Coches()
coche2=Coches()

coche1._Coches__marca="VW"
coche1._Coches__color="Blanco"
coche1._Coches__modelo="2022"
coche1._Coches__velocidad=220
coche1._Coches__caballaje=150
coche1._Coches__plazas=5

coche2._Coches__marca="Nissan"
coche2._Coches__color="Azul"
coche2._Coches__modelo="2020"
coche2._Coches__velocidad=180
coche2._Coches__caballaje=150
coche2._Coches__plazas=6

print(coche1.acelerar(100))
print(coche2.frenar(150))'''

class Coches:
    marca=""
    color=""
    modelo=""
    velocidad=0
    caballaje=0
    plazas=0
    def acelerar(self,ace):
        self.velocidad+=ace
        return self.velocidad

    def frenar(self,fre):
        self.velocidad-=fre
        return self.velocidad
    
coche1=Coches()
coche2=Coches()

coche1.marca="VW"
coche1.color="Blanco"
coche1.modelo="2022"
coche1.velocidad=220
coche1.caballaje=150
coche1.plazas=5

coche2.marca="Nissan"
coche2.color="Azul"
coche2.modelo="2020"
coche2.velocidad=180
coche2.caballaje=150
coche2.plazas=6

print(coche1.acelerar(100))
print(coche2.frenar(150))