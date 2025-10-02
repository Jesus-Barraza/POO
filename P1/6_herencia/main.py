from coches import Coches,Camiones,Camionetas

coche1=Coches("VW","Blanco","2020",220,200,5)
print(coche1.Marca,coche1.acelerar(120))

camioneta1=Camionetas("Reanult","Amarillo","2025",240,250,8,"Delantera",True)
print(camioneta1.Marca, camioneta1.acelerar(100))

camion1=Camiones("Dina","Negro","2020",180,300,12,8,2500)
print(camion1.Marca,camion1.acelerar(50))

#num_coches=int(input("¿Cuántos coches desea?"))

#for i in range(0,num_coches):
#    print(f"\n\t... Datos del coche {i+1} ...")
#    marca=input("Ingresa la marca: ").upper()
#    color=input("Ingresa el color: ").upper()
#    modelo=input("Ingresa el modelo: ").upper()
#    velocidad=int(input("Ingresa la velocidad: "))
#    potencia=int(input("Ingresa la potencia: "))
#    plaza=int(input("Ingresa las plazas: "))

#    coche1=Coches(marca, color, modelo, velocidad, potencia, plaza)
#    print(f"\tDatos del vehículo: \nMarca: {coche1.getMarca()} \nColor: {coche1.getColor()} \nModelo: {coche1.getModelo()} \nVelocidad: {coche1.getVelocidad()} \nCaballaje: {coche1.getCaballaje()} \nPlaza: {coche1.getPlazas()}")
#    print(f"El {coche1.getMarca()} {coche1.getColor()} aceleró de {coche1.getVelocidad()} a {coche1.acelerar(100)}!")

