import getpass
from model.funciones import Usuarios
import tkinter as tk
from tkinter import messagebox

class Interfaz():
    def __init__(self, ventana):
        ventana.geometry("800x600")
        ventana.title("Gestión de notas ")
        ventana.resizable(False, False)
        self.menu_inicial(ventana)

    @staticmethod
    def limit_mail(p):
        allowed = "0123456789.abcdefghijklmnopqrstuvwxyz@_"
        if all(ch in allowed for ch in p) and p.count("@") <= 1:
            return True
        else:
            return False
    
    @staticmethod
    def limite_correo(ventana):
        end=(ventana.register(Interfaz.limit_mail), "%P")
        return end


    @staticmethod
    def borrarPantalla(ventana):
        for widget in ventana.winfo_children():
            widget.destroy()
    
    @staticmethod
    def esperarTecla():
        espera=messagebox.askok(title="Esperando...", message="Presiona ok para continuar")
    
    def menu_inicial(self, ventana):
        #Borrar ventana
        self.borrarPantalla(ventana)

        #Título
        lbl_titulo=tk.Label(ventana, text=".:: Menu principal ::.")
        lbl_titulo.pack(anchor="n", pady=10)

        #Botones
        btn_registro=tk.Button(ventana, text="Registro", command=lambda:self.menu_registro(ventana))
        btn_registro.config(
            width=12
        )
        btn_registro.pack(pady=15)

        btn_login=tk.Button(ventana, text="Login", command=lambda:self.menu_iniciosesion(ventana))
        btn_login.config(
            width=12
        )
        btn_login.pack(pady=15)

        btn_salir=tk.Button(ventana, text="Salir", command=lambda:ventana.quit())
        btn_salir.config(
            width=12
        )
        btn_salir.pack(pady=15)

    def menu_iniciosesion(self, ventana):
        #borrar ventana
        self.borrarPantalla(ventana)

        #Validación del correo electrónico
        validar=self.limite_correo(ventana)

        #Variables
        correo=tk.StringVar()
        contra=tk.StringVar()

        #titulo
        lbl_title=tk.Label(ventana, text=".:: Inicio de sesión ::.")
        lbl_title.pack(pady=15)

        #Correo
        lbl_correo=tk.Label(ventana, text="Ingrese su correo: ")
        lbl_correo.pack(pady=[15,10])

        txt_correo=tk.Entry(ventana, width=50, textvariable=correo, validate="key", validatecommand=validar)
        txt_correo.pack(pady=10)

        #Contraseña
        lbl_contraseña=tk.Label(ventana, text="Ingrese su contraseña: ")
        lbl_contraseña.pack(pady=[15,10])

        txt_contraseña=tk.Entry(ventana, width=50, textvariable=contra, show="•")
        txt_contraseña.pack(pady=[10,15])
        
        #botones
        btn_entrar=tk.Button(ventana, text="Entrar", command=lambda:Usuarios.inicio_sesion(ventana, correo.get(), contra.get()))
        btn_entrar.config(
            width=12
        )
        btn_entrar.pack(pady=10)

        btn_volver=tk.Button(ventana, text="Volver", command=lambda:self.menu_inicial(ventana))
        btn_volver.config(
            width=12
        )
        btn_volver.pack(pady=10)

    def menu_registro(self, ventana):
        #borrar ventana
        self.borrarPantalla(ventana)

        #Validación del correo electrónico
        validar=self.limite_correo(ventana)

        #Variables
        nombre=tk.StringVar()
        apelli=tk.StringVar()
        correo=tk.StringVar()
        contra=tk.StringVar()

        #titulo
        lbl_title=tk.Label(ventana, text=".:: Registro de usuario ::.")
        lbl_title.pack(pady=15)

        #Nombres
        lbl_nombre=tk.Label(ventana, text="Ingrese sus nombres (Sin apellidos):")
        lbl_nombre.pack(pady=[15,10])

        txt_nombre=tk.Entry(ventana, width=50, textvariable=nombre)
        txt_nombre.pack(pady=10)
        #Apellidos
        lbl_apellido=tk.Label(ventana, text="Ingrese sus apellidos: ")
        lbl_apellido.pack(pady=[15,10])

        txt_apellido=tk.Entry(ventana, width=50, textvariable=apelli)
        txt_apellido.pack(pady=10)

        #Correo
        lbl_correo=tk.Label(ventana, text="Ingrese su correo: ")
        lbl_correo.pack(pady=[15,10])

        txt_correo=tk.Entry(ventana, width=50, textvariable=correo, validate="key", validatecommand=validar)
        txt_correo.pack(pady=10)

        #Contraseña
        lbl_contraseña=tk.Label(ventana, text="Ingrese su contraseña: ")
        lbl_contraseña.pack(pady=[15,10])

        txt_contraseña=tk.Entry(ventana, width=50, textvariable=contra, show="•")
        txt_contraseña.pack(pady=[10,15])
        
        #botones
        btn_entrar=tk.Button(ventana, text="Entrar", command=lambda:Usuarios.registrar(ventana, nombre.get(), apelli.get(), correo.get(), contra.get()))
        btn_entrar.config(
            width=12
        )
        btn_entrar.pack(pady=10)

        btn_volver=tk.Button(ventana, text="Volver", command=lambda:self.menu_inicial(ventana))
        btn_volver.config(
            width=12
        )
        btn_volver.pack(pady=10)
    
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
