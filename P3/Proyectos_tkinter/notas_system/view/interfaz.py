import getpass
from controller.controlador import Usuarios, OpeNotas
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

        #Validación de inicio de sesión
        def validar_sesion(ventana, correo, contra):
            conf=Usuarios.inicio_sesion(correo, contra)
            if conf:
                self.menu_notas(ventana, conf[0], conf[1], conf[2])

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
        btn_entrar=tk.Button(ventana, text="Entrar", command=lambda:validar_sesion(ventana, correo.get(), contra.get()))
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

        #validación de registro
        def registrar_sesion(ventana, nombre, apelli, correo, contra):
            conf=Usuarios.registrar(nombre, apelli, correo, contra)
            if conf:
                self.menu_notas(ventana, conf[0], nombre, apelli)

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
        btn_entrar=tk.Button(ventana, text="Entrar", command=lambda:registrar_sesion(ventana, nombre.get(), apelli.get(), correo.get(), contra.get()))
        btn_entrar.config(
            width=12
        )
        btn_entrar.pack(pady=10)

        btn_volver=tk.Button(ventana, text="Volver", command=lambda:self.menu_inicial(ventana))
        btn_volver.config(
            width=12
        )
        btn_volver.pack(pady=10)
    
    def menu_notas(self,ventana,id_usuario,nombre,apellidos):
        self.borrarPantalla(ventana)

        #Titulo
        lbl_titulo=tk.Label(ventana, text=f".:: bienvenido {nombre} {apellidos}, has iniciado sesión::.")
        lbl_titulo.pack(pady=[15,25])

        #botones
        btn_agragar=tk.Button(ventana, text="Crear una nota", command=lambda:self.crear_nota(ventana, id_usuario, nombre, apellidos))
        btn_agragar.config(
            width=18
        )
        btn_agragar.pack(pady=15)

        btn_mostrar=tk.Button(ventana, text="Mostrar mis notas", command=lambda:self.mostrar_nota(ventana, id_usuario, nombre, apellidos))
        btn_mostrar.config(
            width=18
        )
        btn_mostrar.pack(pady=15)

        btn_cambiar=tk.Button(ventana, text="Modificar una nota", command=lambda:self.modificar_nota(ventana, id_usuario, nombre, apellidos))
        btn_cambiar.config(
            width=18
        )
        btn_cambiar.pack(pady=15)

        btn_eliminar=tk.Button(ventana, text="Eliminar una nota", command=lambda:self.borrar_nota(ventana, id_usuario, nombre, apellidos))
        btn_eliminar.config(
            width=18
        )
        btn_eliminar.pack(pady=15)

        btn_volver=tk.Button(ventana, text="Volver", command=lambda:self.menu_iniciosesion(ventana))
        btn_volver.config(
            width=12
        )
        btn_volver.pack(pady=10)

    def crear_nota(self, ventana, id_usuario, nombre, apellidos):
        self.borrarPantalla(ventana)

        #Variables
        titulo=tk.StringVar()
        texto=tk.StringVar()

        #Validar nota
        def validar_nota(id_usuario, titulo, desc):
            vali=OpeNotas.crear_nota(id_usuario, titulo, desc)
            if vali:
                self.menu_notas(ventana, id_usuario, nombre, apellidos)

        #Titulo
        lbl_title=tk.Label(ventana, text=".:: Crear nota ::.")
        lbl_title.pack(pady=[15, 25])

        #Titulo de la nota
        lbl_titulo=tk.Label(ventana, text="Titulo:")
        lbl_titulo.pack(pady=10)

        txt_titulo=tk.Entry(ventana, textvariable=titulo)
        txt_titulo.config(
            width=50
        )
        txt_titulo.pack(pady=[10, 20])

        #Texto de la nota
        lbl_texto=tk.Label(ventana, text="Descripción:")
        lbl_texto.pack(pady=10)

        txt_texto=tk.Entry(ventana, textvariable=texto)
        txt_texto.config(
            width=50
        )
        txt_texto.pack(pady=[10, 20])

        #Botones
        btn_crear=tk.Button(ventana, text="Guardar", command=lambda:validar_nota(id_usuario, titulo.get(), texto.get()))
        btn_crear.config(
            width=16
        )
        btn_crear.pack(pady=10)

        btn_volver=tk.Button(ventana, text="Volver", command=lambda:self.menu_notas(ventana, id_usuario, nombre, apellidos))
        btn_volver.config(
            width=12
        )
        btn_volver.pack(pady=10)

    def mostrar_nota(self, ventana, id_usuario, nombre, apellidos):
        self.borrarPantalla(ventana)

        #Titulo
        lbl_titulo=tk.Label(ventana, text=f"{nombre} {apellidos}, tus notas son:")
        lbl_titulo.pack(pady=[15,25])

        #Texto
        registros=OpeNotas.mostrar_nota(id_usuario)
        if len(registros)>0:
            num_notas=1
            for fila in registros:
                #Numero
                lbl_num=tk.Label(ventana, text=f"{num_notas}")
                lbl_num.pack(pady=5)
                num_notas+=1 

                #Matriz
                marco_texto=tk.Frame(ventana)
                marco_texto.config(
                width=400,
                height=30
                )
                marco_texto.pack()
                
                #Textos
                lbl_1=tk.Label(marco_texto, text=f"ID: {fila[0]}")
                lbl_1.grid(row=0, column=0, pady=5, padx=10)

                lbl_2=tk.Label(marco_texto, text=f"Titulo: {fila[2]}")
                lbl_2.grid(row=0, column=1, pady=5, padx=10)

                lbl_3=tk.Label(marco_texto, text=f"Fecha: {fila[4]}")
                lbl_3.grid(row=0, column=2, pady=5, padx=10)

                lbl_4=tk.Label(ventana, text=f"{fila[3]}")
                lbl_4.pack(pady=[5,20])
        else:
            lbl_noti=tk.Label(ventana, text="No hay notas registrada por el momento")
            lbl_noti.pack(pady=10)

        #botones
        btn_volver=tk.Button(ventana, text="Volver", command=lambda:self.menu_notas(ventana, id_usuario, nombre, apellidos))
        btn_volver.config(
            width=12
        )
        btn_volver.pack(pady=10)
                
    def modificar_nota(self, ventana, id_usuario, nombre, apellidos):
        self.borrarPantalla(ventana)

        #Variables
        ide=tk.StringVar()
        titulo=tk.StringVar()
        texto=tk.StringVar()

        #Validar nota
        def validar_nota(id, titulo, desc):
            vali=OpeNotas.modificar_nota(id, titulo, desc)
            if vali:
                self.menu_notas(ventana, id_usuario, nombre, apellidos)

        #Titulo
        lbl_title=tk.Label(ventana, text=f".:: {nombre} {apellidos}, vamos a modificar una nota ::.")
        lbl_title.pack(pady=[15, 25])

        #Id
        lbl_id=tk.Label(ventana, text="ID de la nota a modificar:")
        lbl_id.pack(pady=10)

        txt_id=tk.Entry(ventana, textvariable=ide)
        txt_id.config(
            width=20
        )
        txt_id.pack(pady=[10,20])

        #Titulo de la nota
        lbl_titulo=tk.Label(ventana, text="Nuevo titulo:")
        lbl_titulo.pack(pady=10)

        txt_titulo=tk.Entry(ventana, textvariable=titulo)
        txt_titulo.config(
            width=50
        )
        txt_titulo.pack(pady=[10, 20])

        #Texto de la nota
        lbl_texto=tk.Label(ventana, text="Nueva descripción:")
        lbl_texto.pack(pady=10)

        txt_texto=tk.Entry(ventana, textvariable=texto)
        txt_texto.config(
            width=50
        )
        txt_texto.pack(pady=[10, 20])

        #Botones
        btn_mod=tk.Button(ventana, text="Guardar", command=lambda:validar_nota(ide.get(), titulo.get(), texto.get()))
        btn_mod.config(
            width=16
        )
        btn_mod.pack(pady=10)

        btn_volver=tk.Button(ventana, text="Volver", command=lambda:self.menu_notas(ventana, id_usuario, nombre, apellidos))
        btn_volver.config(
            width=12
        )
        btn_volver.pack(pady=10)

    def borrar_nota(self, ventana, id_usuario, nombre, apellidos):
        self.borrarPantalla(ventana)

        #Variables
        ide=tk.StringVar()

        #Validar nota
        def validar_nota(id):
            vali=OpeNotas.eliminar_nota(id)
            if vali:
                self.menu_notas(ventana, id_usuario, nombre, apellidos)

        #Titulo
        lbl_title=tk.Label(ventana, text=f".:: {nombre} {apellidos}, vamos a eliminar una nota ::.")
        lbl_title.pack(pady=[15, 25])

        #Id
        lbl_id=tk.Label(ventana, text="ID de la nota a eliminar:")
        lbl_id.pack(pady=10)

        txt_id=tk.Entry(ventana, textvariable=ide)
        txt_id.config(
            width=20
        )
        txt_id.pack(pady=[10,20])

        #Botones
        btn_eliminar=tk.Button(ventana, text="Eliminar", command=lambda:validar_nota(ide.get()))
        btn_eliminar.config(
            width=16
        )
        btn_eliminar.pack(pady=10)

        btn_volver=tk.Button(ventana, text="Volver", command=lambda:self.menu_notas(ventana, id_usuario, nombre, apellidos))
        btn_volver.config(
            width=12
        )
        btn_volver.pack(pady=10)