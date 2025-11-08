import tkinter as tk
import os #Función que ya conoces no ma-
from PIL import Image, ImageTk

#Ventana
ventana=tk.Tk()
ventana.geometry("1280x720")
ventana.title("Imagenes \U0001F4F7")

#Funcion
def mensaje(tipo, funcion):
    funcion.config(text=f"{tipo}")

# Obtener la ruta absoluta del directorio donde está este archivo .py
#ruta_base = os.path.dirname(os.path.abspath(__file__))
ruta_base = os.path.dirname(os.path.abspath(path="E:\\Archivo\\POO\\P3\\Actividades\\Extra"))
#E:\\Archivo\\POO\\P3\\Actividades\\Extra\\

# Construir la ruta completa al archivo de imagen
ruta_imagen = os.path.join(ruta_base, "Extra\\Logo_utd - copia.png")

#Imágenes
'''
#Primera forma: librería de tkinter ya incluída
#Photoimage solo permite archivos con al extensión .png, .gif, .pgm y .ppm

#imagen=tk.PhotoImage(file="E:\\Archivo\\POO\\P3\\Actividades\\Extra\\Logo_utd - copia.png")
imagen=tk.PhotoImage(file=ruta_imagen)

#Incluir o mostrar ventana
etiqueta=tk.Label(ventana, image=imagen, text="Somos bufalos UTD", compound="top")
etiqueta.pack(pady=5)

btn=tk.Button(ventana, image=imagen, command=lambda:mensaje("Hola python", resultado))
btn.pack(pady=5)

resultado=tk.Label(ventana, text="")
resultado.pack(pady=5)

ventana=tk.mainloop()
'''

#Segunda forma: Pillow
#Es necesario instalar la siguiente libreria: 
# pip install --upgrade pillow
# pip install --upgrade pip


# Abrir imagen con PIL
#img = Image.open("/Users/dagfiscal/python/programacion_oo_2025/P2_TKINTER_POO/DFG/INTRODUCCION_TKINTER/logo_utd.png")
img = Image.open(ruta_imagen)
img = img.resize((300, 100))  # Redimensionar (opcional)
imagen_tk = ImageTk.PhotoImage(img)

# Colocar imagen dentro de una etiqueta y boton
etiqueta = tk.Label(ventana, image=imagen_tk).pack()
boton=tk.Button(ventana, image=imagen_tk,).pack()

ventana.mainloop()