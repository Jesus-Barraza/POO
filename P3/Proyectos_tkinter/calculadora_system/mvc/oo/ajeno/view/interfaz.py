#Importaciones
import tkinter as tk
from tkinter import messagebox
from controller import funciones
from model import operaciones

class Interfaz():
    def __init__(self,ventana):
        ventana.geometry("800x600")
        ventana.title("Calculadora básica \U0001F5A9")
        ventana.resizable(False, False)
        self.menu_agregar(ventana)

    @staticmethod
    def borrarPantalla(ventana):
        for widget in ventana.winfo_children():
            widget.destroy()

    def submenu(self,ventana):
        #Barra del menú
        menubar=tk.Menu(ventana)
        ventana.config(menu=menubar)

        #Archivo del menú
        menuarch=tk.Menu(menubar, tearoff=False)
        menubar.add_cascade(label="Operaciones", menu=menuarch)
        menuarch.add_command(label="Agregar", command=lambda:(
            Interfaz.borrarPantalla(ventana),
            self.menu_agregar(ventana)
        ))
        menuarch.add_command(label="Mostrar", command=lambda:(
            Interfaz.borrarPantalla(ventana),
            self.menu_mostrar(ventana)
        ))
        menuarch.add_command(label="Cambiar", command=lambda:(
            Interfaz.borrarPantalla(ventana),
            self.menu_cambiar(ventana)
        ))
        menuarch.add_command(label="Borrar", command=lambda:(
            Interfaz.borrarPantalla(ventana),
            self.menu_borrar(ventana)
        ))
        menuarch.add_separator()
        menuarch.add_command(label="Salir", command=lambda:ventana.quit())


    def menu_agregar(self,ventana):
        #Barra del menú
        self.submenu(ventana)

        #variables
        n1=tk.StringVar()
        n2=tk.StringVar()

        #limitar las cajas de texto
        def limit(p):
            allowed = "0123456789."
            if all(ch in allowed for ch in p) and p.count(".") <= 1:
                return True
            else:
                return False
    
        verificacion=(ventana.register(limit), "%P")

        #cajas de texto
        txt_numero1=tk.Entry(ventana, textvariable=n1, validate="key", validatecommand=verificacion)
        txt_numero1.config(
            width=20,
            justify="left"
        )
        txt_numero1.focus()
        txt_numero1.pack(side="top", pady=[15,5])

        txt_numero2=tk.Entry(ventana, textvariable=n2, validate="key", validatecommand=verificacion)
        txt_numero2.config(
            width=20,
            justify="left"
        )
        txt_numero2.pack(side="top", pady=[5,15])

        #matriz
        frame_btn=tk.Frame(ventana)
        frame_btn.config(
            width=400,
            height=200
        )
        frame_btn.pack(pady=5)

        #botones
        btn_suma=tk.Button(frame_btn, text="+", command=lambda:funciones.mensajes.insertarDato(n1.get(), n2.get(), "+"))
        btn_suma.config(
            width=5
        )
        btn_suma.grid(row=0, column=0, padx=5, pady=5)

        btn_resta=tk.Button(frame_btn, text="-", command=lambda:funciones.mensajes.insertarDato(n1.get(), n2.get(), "-"))
        btn_resta.config(
            width=5
        )
        btn_resta.grid(row=0, column=1, padx=5, pady=5)

        btn_multi=tk.Button(frame_btn, text="x", command=lambda:funciones.mensajes.insertarDato(n1.get(), n2.get(), "x"))
        btn_multi.config(
            width=5
        )
        btn_multi.grid(row=1, column=0, padx=5, pady=5)

        btn_divi=tk.Button(frame_btn, text="/", command=lambda:funciones.mensajes.insertarDato(n1.get(), n2.get(), "/"))
        btn_divi.config(
            width=5
        )
        btn_divi.grid(row=1, column=1, padx=5, pady=5)

        btn_potencia=tk.Button(frame_btn, text="^", command=lambda:funciones.mensajes.insertarDato(n1.get(), n2.get(), "^"))
        btn_potencia.config(
            width=5
        )
        btn_potencia.grid(row=2, column=0, padx=5, pady=5)

        btn_raiz=tk.Button(frame_btn, text="√", command=lambda:funciones.mensajes.insertarDato(n1.get(), n2.get(), "√"))
        btn_raiz.config(
            width=5
        )
        btn_raiz.grid(row=2, column=1, padx=5, pady=5)

        btn_boton=tk.Button(ventana, text="Salir del programa", command=ventana.quit)
        btn_boton.pack(pady=15)
        
    def menu_borrar(self,ventana):
        #barra del menu
        self.submenu(ventana)

        #variables
        ide=tk.StringVar()

        #Limitar las cajas de texto
        def limit(p):
            if p.isdigit():
                return True
            else:
                return False
            
        verificacion=(ventana.register(limit), "%P")

        #Título
        lbl_titulo=tk.Label(ventana, text="\n .:: Borrar una operación ::.")
        lbl_titulo.pack(pady=5)

        lbl_text=tk.Label(ventana, text="Inserte la ID de la operación a borrar:")
        lbl_text.pack(pady=[5,15])

        #Cuadro de texto
        txt_id=tk.Entry(ventana, textvariable=ide, validatecommand=verificacion, validate="key")
        txt_id.config(
            width=20,
            justify="left"
        )
        txt_id.focus()
        txt_id.pack(anchor="n", pady=[15,25])

        #matriz de botones
        frame_btn=tk.Frame(ventana)
        frame_btn.config(
            width=400,
            height=200
        )
        frame_btn.pack(pady=5)

        #botones
        btn_eliminar=tk.Button(frame_btn, text="Eliminar", command=lambda:funciones.mensajes.eliminarDato(ide.get()))
        btn_eliminar.config(
            width=10
        )
        btn_eliminar.grid(row=0, column=0, padx=25)

        btn_volver=tk.Button(frame_btn, text="Volver", command=lambda:(self.borrarPantalla(ventana), self.menu_agregar(ventana)))
        btn_volver.config(
            width=10
        )
        btn_volver.grid(row=0, column=1, padx=25)

    def menu_mostrar(self, ventana):
        #barra del menu
        self.submenu(ventana)

        #lista de textos
        lis=operaciones.Operaciones.mostrar()

        #textos
        lbl_titulo=tk.Label(ventana, text=".:: Historial de operaciones ::.")
        lbl_titulo.pack(pady=[15, 20])

        for col in lis:
            lbl_lista=tk.Label(ventana, text=f"Operación {col[0]}: Fecha: {col[1]} \n {col[2]} {col[4]} {col[3]} = {col[5]}")
            lbl_lista.pack(pady=5)

        #Botón
        btn_volver=tk.Button(ventana, text="Volver", command=lambda:(self.borrarPantalla(ventana), self.menu_agregar(ventana)))
        btn_volver.config(
            width=10
        )
        btn_volver.pack(pady=10)

    def menu_cambiar(self, ventana):
        #barra del menu
        self.submenu(ventana)
        
        #opciones
        simbolos=["+","-","*","/","^","√"]
        
        #variables
        ide=tk.StringVar()
        num1=tk.StringVar()
        num2=tk.StringVar()
        sign=tk.StringVar()
        sign.set(simbolos[0])

        #Limitar las cajas de texto
        def limit(p):
            if p.isdigit():
                return True
            else:
                return False
        
        verificacion=(ventana.register(limit), "%P")

        def limitnum(p):
            allowed = "0123456789."
            if all(ch in allowed for ch in p) and p.count(".") <= 1:
                return True
            else:
                return False
            
        verificacionNum=(ventana.register(limitnum), "%P")

        #Título
        lbl_titulo=tk.Label(ventana, text="\n .:: Cambiar una operación ::.")
        lbl_titulo.pack(pady=5)

        #Matriz de botones
        frame_cambio=tk.Frame(ventana)
        frame_cambio.config(
            width=400,
            height=400
        )
        frame_cambio.pack(pady=[15,5])

        #Textos
        lbl_id=tk.Label(frame_cambio, text="ID de la operación a cambiar:")
        lbl_id.grid(row=0, column=0, padx=15, pady=5)

        lbl_num1=tk.Label(frame_cambio, text="Nuevo número 1:")
        lbl_num1.grid(row=1, column=0, padx=15, pady=5)

        lbl_num2=tk.Label(frame_cambio, text="Nuevo número 2:")
        lbl_num2.grid(row=2, column=0, padx=15, pady=5)

        lbl_sign=tk.Label(frame_cambio, text="Inserte el nuevo signo:")
        lbl_sign.grid(row=3, column=0, padx=15, pady=5)

        #Cuadros de texto
        txt_id=tk.Entry(frame_cambio, textvariable=ide, validatecommand=verificacion, validate="key")
        txt_id.config(
            width=20,
            justify="left"
        )
        txt_id.focus()
        txt_id.grid(row=0, column=1)

        txt_num1=tk.Entry(frame_cambio, textvariable=num1, validatecommand=verificacionNum, validate="key")
        txt_num1.config(
            width=20,
            justify="left"
        )
        txt_num1.focus()
        txt_num1.grid(row=1, column=1)

        txt_num2=tk.Entry(frame_cambio, textvariable=num2, validatecommand=verificacionNum, validate="key")
        txt_num2.config(
            width=20,
            justify="left"
        )
        txt_num2.focus()
        txt_num2.grid(row=2, column=1)

        #Lista de opciones
        opt_signo=tk.OptionMenu(frame_cambio, sign, *simbolos)
        opt_signo.grid(row=3, column=1)

        #matriz de botones
        frame_btn=tk.Frame(ventana)
        frame_btn.config(
            width=400,
            height=200
        )
        frame_btn.pack(pady=5)

        #botones
        btn_guardar=tk.Button(frame_btn, text="Guardar", command=lambda:funciones.mensajes.cambiarDato(ide.get(), num1.get(), num2.get(), sign.get()))
        btn_guardar.config(
            width=10
        )
        btn_guardar.grid(row=0, column=0, padx=25)

        btn_volver=tk.Button(frame_btn, text="Volver", command=lambda:(self.borrarPantalla(ventana), self.menu_agregar(ventana)))
        btn_volver.config(
            width=10
        )
        btn_volver.grid(row=0, column=1, padx=25)
