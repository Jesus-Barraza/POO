from coches import *
import os

coche1=Coches("VW","Blanco","2020",220,200,5)
#print(coche1.Marca,coche1.acelerar(120))

camioneta1=Camionetas("Reanult","Amarillo","2025",240,250,8,"Delantera",True)
#print(camioneta1.Marca, camioneta1.acelerar(100))

camion1=Camiones("Dina","Negro","2020",180,300,12,8,2500)
#print(camion1.Marca,camion1.acelerar(50))


def vehiculos(tipo):
    print(f"\n\t...Ingresar los datos del vehículo de tipo {tipo}...")
    marca=input("Marca: ").upper()
    color=input("Color: ").upper()
    modelo=input("Modelo: ").upper()
    velocidad=int(input("Velocidad: "))
    potencia=int(input("Potencia: "))
    plaza=int(input("n° plazas: "))
    return marca,color,modelo,velocidad,potencia,plaza

def imprimir(vehiculo):
    print(f"\tDatos del vehículo: \nMarca: {vehiculo.Marca} \nColor: {vehiculo.Color} \nModelo: {vehiculo.Modelo} \nVelocidad: {vehiculo.Velocidad} \nCaballaje: {vehiculo.Caballaje} \nPlaza: {vehiculo.Plazas}")

def coche():
    marca,color,modelo,velocidad,potencia,plaza=vehiculos("coches")

    vehiculo=Coches(marca, color, modelo, velocidad, potencia, plaza)
    imprimir(vehiculo)

def camiones():
    marca,color,modelo,velocidad,potencia,plaza=vehiculos("camiones")
    eje=int(input(f"N° de ejes: "))
    capacidad=int(input("Capacidad de carga: "))

    vehiculo=Camiones(marca, color, modelo, velocidad, potencia, plaza, eje, capacidad)
    imprimir(vehiculo)
    print(f"Ejes: {vehiculo.Eje} \nCapacidad de carga: {vehiculo.CapacidadCarga}")

def camionetas():
    marca,color,modelo,velocidad,potencia,plaza=vehiculos("camionetas")
    traccion=int(input(f"Tracción: "))
    cerrada=input("¿Cerrada? (si/no): ").upper().strip()
    if cerrada=="SI":
        cerrada=True
    else:
        cerrada=False

    vehiculo=Camionetas(marca, color, modelo, velocidad, potencia, plaza, traccion, cerrada)
    imprimir(vehiculo)
    print(f"Tracción: {vehiculo.Tracción} \nCerrado: {vehiculo.Cerrado}")


veh=True
while veh:
    os.system("cls")
    print("\n\t\tMenú principal")
    veh=input("Elija el tipo de vehículo a trabajar: \n1.-Coches\n2.-Camionetas\n3.-Camiones\n4.-Salir\n\n(1-4): ").strip()
    
    match veh:
        case "1":
            os.system("cls")
            coche()
            input("Oprima enter para continuar...")
        case "2":
            os.system("cls")
            camionetas()
            input("Oprima enter para continuar...")
        case "3":
            os.system("cls")
            camiones()
            input("Oprima enter para continuar...")
        case "4":
            os.system("cls")
            print("¡Gracias por usar el SW!")
            input("Oprima enter para continuar...")
            veh=False
        case _:
            os.system("cls")
            print("Opción no válida, inténtelo de nuevo")
            input("Oprima enter para continuar...")
    

