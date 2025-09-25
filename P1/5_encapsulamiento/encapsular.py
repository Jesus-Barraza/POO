'''
Encapsulamiento - Es un pilar de la POO que permite indicar cuál es la manera de poder utilizar los atributos y métodos de una clase a la hora de usar en objetos/herencia
'''
import os
os.system("cls")

class Clase:
    atrib_pub="Soy un atributo público" #Un atributo público puede ser usado por todos
    _atrib_pro="Soy un atributo protegido" #Un atributo protegido es usado solo a los que pertenecen a la clase
    __atrib_pri="Soy un atributo privado" #Un atributo privado no puede ser usado fuera de la clase
    
    def __init__(self,color,tamano):
        self.__color=color
        self.__tamano=tamano

    @property
    def color(self):
        return self.__color
    @color.setter
    def color(self,col):
        self.__color=col

    @property
    def tamano(self):
        return self.__tamano
    @tamano.setter
    def color(self,tam):
        self.__tamano=tam

    @property
    def publico(self):
        return self.atrib_pub
    @publico.setter
    def publico(self,pub):
        self.atrib_pub=pub

    @property
    def protegido(self):
        return self._atrib_pro
    @protegido.setter
    def protegido(self,pro):
        self._atrib_pro=pro

    @property
    def privado(self):
        return self.__atrib_pri
    @privado.setter
    def privado(self,pri):
        self.__atrib_pri=pri

#Utilizando la clase
obj=Clase("verde","pequeño")
print(obj.publico)
print(obj.protegido)
print(obj.privado) #No es posible leer/cambiar el valor de un objeto privado sin un getter/setter

#print(obj.atrib_pub) #No es bueno acceder a los valores directamente
#print(obj._atrib_pro)
#print(obj._Clase__atrib_pri) #Este caso es poco común de usar y no recomendable

#print(obj) #En este caso te sale el valor de ubicación del objeto en binario (escrito por hexadecimal)
print(obj.color, obj.tamano)
obj.color="Amarillo"
print(obj.tamano)