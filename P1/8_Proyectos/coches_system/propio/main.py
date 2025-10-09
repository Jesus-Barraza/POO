#Instanciar los objetos para posterior implementarlos 
from model import coches,cochesBD
import os

def BorrarPantalla():
    os.system("cls")
def EsperarTecla():
    input(f"\n\t... Oprima una tecla para continuar ...")

def datos_autos(tipo):
    BorrarPantalla()
    print(f"\n\t ...Ingresar los datos del Vehiculo de tipo: {tipo}")
    marca=input("Marca: ").upper()
    color=input("Color: ").upper()
    modelo=input("Modelo: ").upper()
    velocidad=int(input("Velocidad: "))
    potencia=int(input("Potencia: "))
    plazas=int(input("No. de plazas: "))
    return marca,color,modelo,velocidad,potencia,plazas

def imprimir_datos_vehiculo(marca,color,modelo,velocidad,potencia,plazas):
    print(f"\n\tDatos del Vehiculo: \n Marca:{marca} \n color: {color} \n Modelo: {modelo} \n velocidad: {velocidad} \n caballaje: {potencia} \n plazas: {plazas}")

def autos():
    marca,color,modelo,velocidad,potencia,plazas=datos_autos("Auto")
    coche=coches.Coches(marca,color,modelo,velocidad,potencia,plazas)
    imprimir_datos_vehiculo(coche.marca,coche.color,coche.modelo,coche.velocidad,coche.caballaje,coche.plazas)
    #Agregar en la base de datos
    auto=cochesBD.Coches(coche.marca,coche.color,coche.modelo,coche.velocidad,coche.caballaje,coche.plazas)
    resp=auto.insertar()
    if resp:
        print("Registro insertado correctamente")
    else:
        print("No fue posible insertar el registro, intenta nuevamente")

def camionetas():
    marca,color,modelo,velocidad,potencia,plazas=datos_autos("Camioneta")
    traccion=input("Traccion: ").upper()
    cerrada=input("¿Cerrada (Si/No)?: ").upper().strip()
    if cerrada=="SI":
        cerrada=True
    else:
        cerrada=False    
    coche=coches.Camionetas(marca,color,modelo,velocidad,potencia,plazas,traccion,cerrada)
    imprimir_datos_vehiculo(coche.marca,coche.color,coche.modelo,coche.velocidad,coche.caballaje,coche.plazas)
    print(f"traccion: {coche.traccion}\n cerrada: {coche.cerrada}")

def camiones():
    marca,color,modelo,velocidad,potencia,plazas=datos_autos("Camiones")
    eje=int(input("No. de ejes: "))
    capacidadCarga=int(input("Capacidad de carga: "))
    coche=coches.Camiones(marca,color,modelo,velocidad,potencia,plazas,eje,capacidadCarga)
    imprimir_datos_vehiculo(coche.marca,coche.color,coche.modelo,coche.velocidad,coche.caballaje,coche.plazas)
    print(f"#Ejes: {coche.eje}\n Capacidad de carga: {coche.capacidadCarga}")

def main():
    opcion=True
    while opcion:
        opcion=input("\n\t\t ::: Menu Principal ::.\n\t1.-Autos\n\t2.-Camionetas\n\t3.-Camiones\n\t4.-Salir\n\tElige un opción: ").lower().strip()
        match opcion:
            case "1":
                BorrarPantalla()
                autos()
                EsperarTecla()
            case "2":
                BorrarPantalla()
                camionetas()
                EsperarTecla()  
            case "3":
                BorrarPantalla()
                camiones()
                EsperarTecla()
            case "4":
                BorrarPantalla()
                input("\n\t\tSalir del Sistema")
                opcion=False   
            case _:
                BorrarPantalla()
                input("\n\tOpcion invalida ... vuelva a intertarlo ... ")      

if __name__=="__main__":
    BorrarPantalla()
    main()
