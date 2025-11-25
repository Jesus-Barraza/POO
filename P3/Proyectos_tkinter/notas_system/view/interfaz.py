import getpass
from model import funciones
import tkinter as tk
from tkinter import messagebox

class Interfaz():
    def __init__(self, ventana):
        ventana.geometry("800x600")
        ventana.title("Gestión de notas ")
        ventana.resizable(False, False)
        self.menu_inicial(ventana)

    @staticmethod
    def borrarPantalla(ventana):
        for widget in ventana.winfo_children():
            widget.destroy()
    
    @staticmethod
    def esperarTecla():
        espera=messagebox.askokcancel(title="Esperando...", message="Presiona ok para continuar")
        if true:
            return True
        else:
            return False
    
    def menu_inicial(self, ventana):
        #Borrar ventana
        self.borrarPantalla(ventana)

        #Título
        lbl_titulo=tk.Label(ventana, text=".:: Menu principal ::.")
        lbl_titulo.pack(anchor="n", pady=10)

        #Botones
        btn_registro=tk.Button(ventana, text="Registro", command="")
        btn_registro.config(
            width=12
        )
        btn_registro.pack(pady=15)

        btn_login=tk.Button(ventana, text="Login", command="")
        btn_login.config(
            width=12
        )
        btn_login.pack(pady=15)

        btn_salir=tk.Button(ventana, text="Salir", command=lambda:ventana.quit())
        btn_salir.config(
            width=12
        )
        btn_salir.pack(pady=15)
    
    def menu_notas(self,usuario_id,nombre,apellidos):
     while True:
        Interfaz.borrarPantalla()
        print(f"\n \t \t \t Bienvenido {nombre} {apellidos}, has iniciado sesión ...")
        print("""
                  \n \t 
                      .::  Menu Notas ::. 
                  1.- Crear 
                  2.- Mostrar
                  3.- Cambiar
                  4.- Eliminar
                  5.- Regresar 
                  """)
        opcion = input("\t\t Elige una opción: ").upper()

        if opcion == '1' or opcion=="CREAR":
            Interfaz.borrarPantalla()
            print(f"\n \t .:: Crear Nota ::. ")
            titulo=input("\tTitulo: ")
            descripcion=input("\tDescripción: ")
            #Agregar codigo
            resultado=nota.Nota.crear(usuario_id,titulo,descripcion)
            if resultado:
                print(f"\n \t \t.::La Nota {titulo} se creo Correctamente ::.")
            else:
                print(f"\n \t \t** No fue posible crear la nota ... vuelva a intentarlo **...") 
            Interfaz.esperarTecla()    
        elif opcion == '2' or opcion=="MOSTRAR":
            Interfaz.borrarPantalla()
            #Agregar codigo  
            registros=nota.Nota.mostrar(usuario_id)
            if len(registros)>0:
                print(f"\n\t {nombre} {apellidos}, tus notas son: ")
                num_notas=1
                for fila in registros:
                   print(f"\nNota: {num_notas} \nID: {fila[0]}.- Titulo: {fila[2]}         Fecha de Creación: {fila[4]} \nDescripción: {fila[3]}") 
                   num_notas+=1    
            else:
                print(f"\n \t \t** No existen notas para el usuario ... vuelva a intentarlo **...")
            Interfaz.esperarTecla()
        elif opcion == '3' or opcion=="CAMBIAR":
            Interfaz.borrarPantalla()
            print(f"\n \t .:: {nombre} {apellidos}, vamos a modificar un Nota ::. \n")
            id = input("\t \t ID de la nota a actualizar: ")
            titulo = input("\t Nuevo título: ")
            descripcion = input("\t Nueva descripción: ")
            #Agregar codigo
            resultado=nota.Nota.actualizar(id,titulo,descripcion)
            if resultado:
                print(f"\n \t \t.::Nota Actualizada Correctamente ::.")
            else:
                print(f"\n \t \t** No fue posible actualizar la nota ... vuelva a intentarlo **...")  
            Interfaz.esperarTecla()      
        elif opcion == '4' or opcion=="ELIMINAR":
            Interfaz.borrarPantalla()
            print(f"\n \t .:: {nombre} {apellidos}, vamos a borrar un Nota ::. \n")
            id = input("\t \t ID de la nota a eliminar: ")
            #Agregar codigo
            resultado=nota.Nota.eliminar(id)
            if resultado:
                print(f"\n \t \t.::Nota Eliminada Correctamente ::.")
            else:
                print(f"\n \t \t** No fue posible eliminar la nota ... vuelva a intentarlo **...")  
            Interfaz.esperarTecla()    
        elif opcion == '5' or opcion=="SALIR":
            break
        else:
            print("\n \t \t Opción no válida. Intenta de nuevo.")
            Interfaz.esperarTecla()
