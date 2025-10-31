import tkinter as tk

'''
#funciones
def saludar(funcion,texto):
    funcion.config(
        text=f"¡Bienvenido, {texto}!"
    )

#ventana
ventana=tk.Tk()
ventana.geometry("1280x720")
ventana.title("Entrada \U0001F913")

#titulo
titulo=tk.Label(ventana, text="Ingrese su nombre") #lleva el sufijo "lbl"
titulo.config(
    font=("arial",14,"bold")
)
titulo.pack()

#Texto de instrucción
nombre=tk.StringVar()

#caja de texto para entrar
ingreso=tk.Entry(ventana, textvariable=nombre) #lleva el sufijo "txt"
ingreso.config(
    width=50
)
ingreso.pack(pady=5)

#boton de ingreso
btn_saludar=tk.Button(ventana, text="Saludar", command=lambda:saludar(saludo,nombre.get())) #lleva el sufijo btn
btn_saludar.config(
    font=("arial",10),
    width=10
)
btn_saludar.pack(pady=5)

#titulo de saludo
saludo=tk.Label(ventana, text="")
saludo.config(
    font=("arial",12)
)
saludo.pack(pady=20)


ventana=tk.mainloop()
'''

ventana=tk.Tk()
ventana.geometry("800x600")
ventana.title("Sistema \u270F")

#Funcion
def entrar(funcion, texto):
    funcion.config(
        text=f"Bienvenido al sistema, {texto}",
        bg="#4fa489",
        fg="#01281B",
        width=50,
        height=2,
        font=("Arial",24,"bold")
    )

def borrar(cuadro1, cuadro2, funcion):
    cuadro1.delete(0, tk.END)
    cuadro2.delete(0, tk.END)
    color_defecto=ventana.cget("bg")
#    funcion.destroy() #Puedes borrar todo dentro de lo dibujado con eso
    funcion.config(
        text="",
        bg=color_defecto
    )
    cuadro2.focus()

def salir():
    ventana.quit() #Esta función te permite salir de un programa

#titulo
lbl_titulo=tk.Label(ventana, text="Bienvenido al sistema")
lbl_titulo.config(
    bg="#aaaaaa",
    fg="#333333",
    width=50,
    height=2,
    font=("Arial",36,"bold")
)
lbl_titulo.pack(anchor="n")

#ingreso de nombre
lbl_nombre=tk.Label(ventana, text="Ingrese su nombre")
lbl_nombre.config(
    font=("arial", 12)
)
lbl_nombre.pack(anchor="nw", padx=10, pady=[30,10])

txt_nombre=tk.Entry(ventana)
txt_nombre.config(
    width=50,
#    state="readonly", #permite la inicialización de datos de normal
)
txt_nombre.focus() #Permite inicializar el foco en un cuadro de texto
txt_nombre.pack(anchor="n")

#ingreso de contraseña
lbl_contra=tk.Label(ventana, text="Ingrese su contraseña")
lbl_contra.config(
    font=("arial", 12)
)
lbl_contra.pack(anchor="nw", padx=10, pady=[20,10] )

txt_contra=tk.Entry(ventana, show="•")
txt_contra.config(
    width=50
)
txt_contra.pack(anchor="n")

'''
#boton de ingreso
btn_saludar=tk.Button(ventana, text="Ingresar", command=lambda:entrar(lbl_saludo, txt_nombre.get())) #lleva el sufijo btn
btn_saludar.config(
    font=("arial",10),
    width=10
)
btn_saludar.pack(pady=[15,10])

btn_borrar=tk.Button(ventana, text="Borrar", command=lambda:borrar(txt_nombre,txt_contra,lbl_saludo))
btn_borrar.config(
    font=("arial",10),
    width=10
)
btn_borrar.pack(pady=10)

#Salida
btn_salir=tk.Button(ventana, text="Salir", command=lambda:salir())
btn_salir.config(
    font=("arial",10),
    width=10
)
btn_salir.pack(pady=10)
'''

#Marco de los botones
marco_botones=tk.Frame(ventana)
marco_botones.config(
    width=800,
    height=50,
)
marco_botones.pack_propagate(False)
marco_botones.pack(pady=25)

#boton de ingreso
btn_saludar=tk.Button(marco_botones, text="Ingresar", command=lambda:entrar(lbl_saludo, txt_nombre.get())) #lleva el sufijo btn
btn_saludar.config(
    font=("arial",10),
    width=10
)
btn_saludar.grid(row=0, column=0, padx=5, pady=15) #Adaptando un marco, puedes tratarlo como tabla con esto

btn_borrar=tk.Button(marco_botones, text="Borrar", command=lambda:borrar(txt_nombre,txt_contra,lbl_saludo))
btn_borrar.config(
    font=("arial",10),
    width=10
)
btn_borrar.grid(row=0, column=1, padx=5, pady=15)

#Salida
btn_salir=tk.Button(marco_botones, text="Salir", command=lambda:salir())
btn_salir.config(
    font=("arial",10),
    width=10
)
btn_salir.grid(row=0, column=2, padx=5, pady=15)

#Texto de saludo
lbl_saludo=tk.Label(ventana, text="")
lbl_saludo.pack(anchor="n")

ventana=tk.mainloop()