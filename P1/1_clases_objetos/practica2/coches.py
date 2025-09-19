#Importaciones
import os
def borrar():
    os.system("cls")

#Clase de coches
class Coches:
    #Metodo constructor que inicia los valores cuando se instancia un obj de la clase
    def __init__(self,Color,Marca,Velocidad): 
        self.__Color = str(Color) #Atributos del objeto
        self.__Marca = str(Marca)
        self.__Velocidad = int(Velocidad)

    #Metodos del objeto
    def acelerar(self,ace):
        self.__Velocidad=self.__Velocidad+ace
        return self.__Velocidad

    def frenar(self,fre):
        self.__Velocidad=self.__Velocidad-fre
        return self.__Velocidad

    def tocar_claxon(self):
        print(f"El coche {self.__Marca} {self.__Color} ha tocado el claxon!")

#Instanciar o crear objetos de la clase coches
coche1=Coches("Rojo", "Toyota", 120)
coche2=Coches("Amarillo", "Nissan", 220)

borrar()
#print(f"Los valores del obj 1 son: color:{coche1.Color}, marca:{coche1.Marca}, velocidad:{coche1.Velocidad}")
#print(f"El coche 1 aceleró de: {coche1.Velocidad} a {coche1.acelerar(50)}")
#print(f"Los valores del obj 2 son: color:{coche2.Color}, marca:{coche2.Marca}, velocidad:{coche2.Velocidad}")
#print(f"El coche 2 frenó de: {coche2.Velocidad} a {coche2.frenar(100)}")
print(coche1.acelerar(50))
print(coche2.frenar(100))
coche1.tocar_claxon()