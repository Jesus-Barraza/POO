from model import cochesBD
from controller import coches
import os
import tkinter as tk
from tkinter import messagebox

class Menu:
    def __init__(self, ventana):
        ventana.geometry("800x600")
        ventana.resizable(False, False)
        self.main(ventana)

    @staticmethod
    def borrarPantalla(ventana):
        for widget in ventana.winfo_children():
            widget.destroy()

    def menu_acciones(self,tipo):
        print(f"\n\t\t.::  Menu de {tipo} ::.\n\t1.- Insertar \n\t2.- Consultar\n\t3.- Actualizar\n\t4.- Eliminar\n\t5.- Regresar ")
        opcion = input("\t\t Elige una opción: ").upper().strip()
        return opcion

    def menu_autos(self, ventana):
        while True:
            self.borrarPantalla(ventana)
            opcion=self.menu_acciones("Autos")
            if opcion == '1' or opcion=="INSERTAR":
                self.borrarPantalla(ventana)
                marca,color,modelo,velocidad,caballaje,plazas=self.autos()
                #Agregar a BD
                auto=cochesBD.Autos(marca,color,modelo,velocidad,caballaje,plazas)
                respuesta=auto.insertar()
                self.respuesta_sql(respuesta) 
                self.esperarTecla()    
            elif opcion == '2' or opcion=="CONSULTAR":
                self.borrarPantalla(ventana)  
                registros=cochesBD.Autos.consultar()
                if len(registros)>0:
                    num_autos=1
                    for fila in registros:
                        print(f"\nAuto #{num_autos} con ID: {fila[0]} \nMarca: {fila[1]} \nColor: {fila[2]} Modelo: {fila[3]} \nVelocidad: {fila[4]} \nPotencia: {fila[5]}\nPlazas: {fila[6]}") 
                        num_autos+=1    
                    self.esperarTecla()
                else:
                    print(f"\n \t \t... ¡ No existen datos que mostrar, por el momento ! ...")
                    self.esperarTecla()            
            elif opcion == '3' or opcion=="ACTUALIZAR":
                self.borrarPantalla(ventana)
                print(f"\n \t .:: Actualizar Auto ::. \n")
                id=input("\nID: ")
                marca,color,modelo,velocidad,caballaje,plazas=self.autos() 
                respuesta=cochesBD.Autos.actualizar(marca,color,modelo,velocidad,caballaje,plazas,id)
                self.respuesta_sql(respuesta)  
                self.esperarTecla()      
            elif opcion == '4' or opcion=="ELIMINAR":
                self.borrarPantalla(ventana)
                print(f"\n \t .:: Eliminar Auto ::. \n")
                id=input("\nID: ")
                respuesta=cochesBD.Autos.eliminar(id)
                self.respuesta_sql(respuesta)  
                self.esperarTecla()    
            elif opcion == '5' or opcion=="SALIR":
                break
            else:
                print("\n \t \t Opción no válida. Intenta de nuevo.")
                self.esperarTecla()

    def menu_camionetas(self, ventana):
        while True:
            self.borrarPantalla(ventana)
            opcion=self.menu_acciones("Camionetas")
            if opcion == '1' or opcion=="INSERTAR":
                self.borrarPantalla(ventana)
                marca,color,modelo,velocidad,caballaje,plazas,traccion,cerrada=self.camionetas()
                respuesta=cochesBD.Camionetas.insertar(marca,color,modelo,velocidad,caballaje,plazas,traccion,cerrada)
                self.respuesta_sql(respuesta) 
                self.esperarTecla()    
            elif opcion == '2' or opcion=="CONSULTAR":
                self.borrarPantalla(ventana)  
                registros=cochesBD.Camionetas.consultar()
                if len(registros)>0:
                    num_autos=1
                    for fila in registros:
                        print(f"\nCamioneta #{num_autos} con ID: {fila[0]} \nMarca: {fila[1]} \nColor: {fila[2]} Modelo: {fila[3]} \nVelocidad: {fila[4]} \nPotencia: {fila[5]}\nPlazas: {fila[6]}\nTracción: {fila[7]}\nCerrada: {fila[8]}") 
                        num_autos+=1    
                    self.esperarTecla()
                else:
                    print(f"\n \t \t... ¡ No existen datos que mostrar, por el momento ! ...")
                    self.esperarTecla()            
            elif opcion == '3' or opcion=="ACTUALIZAR":
                self.borrarPantalla(ventana)
                print(f"\n \t .:: Actualizar Camioneta ::. \n")
                id=input("\nID: ")
                marca,color,modelo,velocidad,caballaje,plazas,traccion,cerrada=self.camionetas()
                respuesta=cochesBD.Camionetas.actualizar(marca,color,modelo,velocidad,caballaje,plazas,traccion,cerrada,id)
                self.respuesta_sql(respuesta)
                self.esperarTecla()      
            elif opcion == '4' or opcion=="ELIMINAR":
                self.borrarPantalla(ventana)
                print(f"\n \t .:: Eliminar Camioneta ::. \n")
                id=input("\nID: ")
                respuesta=cochesBD.Camionetas.eliminar(id)
                self.respuesta_sql(respuesta) 
                self.esperarTecla()    
            elif opcion == '5' or opcion=="SALIR":
                break
            else:
                print("\n \t \t Opción no válida. Intenta de nuevo.")
                self.esperarTecla()

    def menu_camiones(self, ventana):
        while True:
            self.borrarPantalla(ventana)
            opcion=self.menu_acciones("Camiones")
            if opcion == '1' or opcion=="INSERTAR":
                self.borrarPantalla(ventana)
                marca,color,modelo,velocidad,caballaje,plazas,eje,capacidadCarga=self.camiones()
                respuesta=cochesBD.Camiones.insertar(marca,color,modelo,velocidad,caballaje,plazas,eje,capacidadCarga)
                self.respuesta_sql(respuesta)
                self.esperarTecla()    
            elif opcion == '2' or opcion=="CONSULTAR":
                self.borrarPantalla(ventana)  
                registros=cochesBD.Camiones.consultar()
                if len(registros)>0:
                    num_autos=1
                    for fila in registros:
                        print(f"\nCamion # {num_autos} con ID: {fila[0]} \nMarca: {fila[1]} \nColor: {fila[2]} Modelo: {fila[3]} \nVelocidad: {fila[4]} \nPotencia: {fila[5]}\nPlazas: {fila[6]}\nNo. ejes: {fila[7]}\nCapacidad de Carga: {fila[8]}") 
                        num_autos+=1    
                    self.esperarTecla()
                else:
                    print(f"\n \t \t... ¡ No existen datos que mostrar, por el momento ! ...")
                    self.esperarTecla()            
            elif opcion == '3' or opcion=="ACTUALIZAR":
                self.borrarPantalla(ventana)
                print(f"\n \t .:: Actualizar Camion ::. \n")
                id=input("\nID: ")
                marca,color,modelo,velocidad,caballaje,plazas,eje,capacidadCarga=self.camiones()
                #Actualizar BD
                respuesta=cochesBD.Camiones.actualizar(marca,color,modelo,velocidad,caballaje,plazas,eje,capacidadCarga,id)
                self.respuesta_sql(respuesta)
                self.esperarTecla()      
            elif opcion == '4' or opcion=="ELIMINAR":
                self.borrarPantalla(ventana)
                print(f"\n \t .:: Eliminar Camion ::. \n")
                id=input("\nID: ")
                respuesta=cochesBD.Camiones.eliminar(id)
                self.respuesta_sql(respuesta)  
                self.esperarTecla()    
            elif opcion == '5' or opcion=="SALIR":
                break
            else:
                print("\n \t \t Opción no válida. Intenta de nuevo.")
                self.esperarTecla()

    def main(self, ventana):
        #Borrar pantalla
        self.borrarPantalla(ventana)

        #funciones
        def salida(ventana):
            salir=messagebox.showinfo(title="Saliendo del programa", message="¡Gracias por utilizar el sistema!")
            ventana.quit()

        #titulo    
        lbl_titulo=tk.Label(ventana, text=".:: Menu Principal ::.\n\nElige un opción: ")
        lbl_titulo.pack(pady=[10,15])

        #botones
        btn_autos=tk.Button(ventana, text="Autos", command=lambda:self.menu_autos(ventana))
        btn_autos.config(width=12)
        btn_autos.pack(pady=10)

        btn_camionetas=tk.Button(ventana, text="Camionetas", command=lambda:self.menu_camionetas(ventana))
        btn_camionetas.config(width=12)
        btn_camionetas.pack(pady=10)

        btn_camiones=tk.Button(ventana, text="Camionetas", command=lambda:self.menu_camiones(ventana))
        btn_camiones.config(width=12)
        btn_camiones.pack(pady=[10,15])

        btn_salir=tk.Button(ventana, text="Salir", command=lambda:salida(ventana))
        btn_salir.config(width=10)
        btn_salir.pack(pady=15)