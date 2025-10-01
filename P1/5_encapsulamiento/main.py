#Instanciar los objetos para posterior implementación
#Crear un objeto o instanciar la clase

#Método 1
#import coches

#coche1=coches.Coches("VW", "Blanco", "2022", 220, 150, 5) 
#coche2=coches.Coches("Nissan", "Azul", "2020", 180, 150, 6)
#coche3=coches.Coches("Honda", "", "", 0, 0, 0) 

#método 2
from coches import Coches

num_coches=int(input("¿Cuántos coches desea?"))

for i in range(0,num_coches):
    print(f"\n\t... Datos del coche {i+1} ...")
    marca=input("Ingresa la marca: ").upper()
    color=input("Ingresa el color: ").upper()
    modelo=input("Ingresa el modelo: ").upper()
    velocidad=int(input("Ingresa la velocidad: "))
    potencia=int(input("Ingresa la potencia: "))
    plaza=int(input("Ingresa las plazas: "))

    coche1=Coches(marca, color, modelo, velocidad, potencia, plaza)
    print(f"\tDatos del vehículo: \nMarca: {coche1.getMarca()} \nColor: {coche1.getColor()} \nModelo: {coche1.getModelo()} \nVelocidad: {coche1.getVelocidad()} \nCaballaje: {coche1.getCaballaje()} \nPlaza: {coche1.getPlazas()}")
    print(f"El {coche1.getMarca()} {coche1.getColor()} aceleró de {coche1.getVelocidad()} a {coche1.acelerar(100)}!")

#coche1=Coches("VW", "Blanco", "2022", 220, 150, 5) 
#coche2=Coches("Nissan", "Azul", "2020", 180, 150, 6)
#coche3=Coches("Honda", "", "", 0, 0, 0) 

#print(f"El {coche1.getMarca()} {coche1.getColor()} aceleró de {coche1.getVelocidad()} a {coche1.acelerar(100)}!")
#print(f"El {coche2.getMarca()} {coche2.getColor()} frenó de {coche2.getVelocidad()} a {coche2.frenar(150)}!")

#print(f"\tDatos del vehículo: \nMarca: {coche1.getMarca()} \nColor: {coche1.getColor()} \nModelo: {coche1.getModelo()} \nVelocidad: {coche1.getVelocidad()} \nCaballaje: {coche1.getCaballaje()} \nPlaza: {coche1.getPlazas()}")
#print(f"\tDatos del vehículo: \nMarca: {coche2.getMarca()} \nColor: {coche2.getColor()} \nModelo: {coche2.getModelo()} \nVelocidad: {coche2.getVelocidad()} \nCaballaje: {coche2.getCaballaje()} \nPlaza: {coche2.getPlazas()}")
#print(f"\tDatos del vehículo: \nMarca: {coche3.getMarca()} \nColor: {coche3.getColor()} \nModelo: {coche3.getModelo()} \nVelocidad: {coche3.getVelocidad()} \nCaballaje: {coche3.getCaballaje()} \nPlaza: {coche3.getPlazas()}")
