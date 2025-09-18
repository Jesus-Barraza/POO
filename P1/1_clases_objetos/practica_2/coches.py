#Importaciones
import os
def borrar():
    os.system("cls")

#Clase de coches
class Coches:
    #Metodo constructor que inicia los valores cuando se instancia un obj de la clase
    def __init__(self,Color,Marca,Velocidad): 
        self.Color = str(Color) #Atributos del objeto
        self.Marca = str(Marca)
        self.Velocidad = int(Velocidad)

    #Metodos del objeto
    def acelerar(self,ace):
        self.Velocidad=self.Velocidad+ace
        return self.Velocidad

    def frenar(self,fre):
        self.Velocidad=self.Velocidad-fre
        return self.Velocidad

    def tocar_claxon(self):
        print(f"Se ha tocado el claxon!")

#Instanciar o crear objetos de la clase coches
coche1=Coches("Rojo", "Toyota", 120)
coche2=Coches("Amarillo", "Nissan", 220)

borrar()
print(f"Los valores del obj 1 son: color:{coche1.Color}, marca:{coche1.Marca}, velocidad:{coche1.Velocidad}")
print(f"El coche 1 aceleró de: {coche1.Velocidad} a {coche1.acelerar(50)}")
print(f"Los valores del obj 2 son: color:{coche2.Color}, marca:{coche2.Marca}, velocidad:{coche2.Velocidad}")
print(f"El coche 2 frenó de: {coche2.Velocidad} a {coche2.frenar(100)}")
coche1.tocar_claxon()