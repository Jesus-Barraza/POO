import tkinter as tk

ventana=tk.Tk()
ventana.geometry("600x400")
ventana.title("Distribución \U0001F914")

#Opción 1 - Pack() con side=left o right
"""#usuario
'''lbl_nombre=tk.Label(ventana, text="Ingrese su nombre de usuario")
lbl_nombre.config(
    font=("calibri",14)
)
lbl_nombre.pack(anchor="nw", pady=[15,5])'''
    #También puedes hacerlo sin variables
tk.Label(ventana, text="Ingrese su nombre de usuario", font=("calibri",14)).pack(anchor="nw", pady=[15,5])

txt_nombre=tk.Entry(ventana)
txt_nombre.config(
    width=50
)
txt_nombre.pack(pady=[5,15])

#contraseña
tk.Label(ventana, text="Ingrese la contraseña", font=("calibri",14)).pack(anchor="nw", pady=[15,5])

txt_nombre=tk.Entry(ventana, show="•")
txt_nombre.config(
    width=50
)
txt_nombre.pack(pady=[5,15])"""

#opcion 2: usar grid()
#marco
marco_texto=tk.Frame(ventana)
marco_texto.config(
    width=400,
    height=200
)
marco_texto.pack()

#usuario
tk.Label(marco_texto, text="Ingrese su nombre de usuario", font=("calibri",14)).grid(row=0, column=0, pady=[15,5])

txt_nombre=tk.Entry(marco_texto)
txt_nombre.config(
    width=50
)
txt_nombre.grid(row=0, column=1, pady=[15,5])

#contraseña
tk.Label(marco_texto, text="Ingrese la contraseña", font=("calibri",14)).grid(row=1, column=0, pady=[15,5])

txt_nombre=tk.Entry(marco_texto, show="•")
txt_nombre.config(
    width=50
)
txt_nombre.grid(row=1, column=1, pady=[5,15])

ventana=tk.mainloop()