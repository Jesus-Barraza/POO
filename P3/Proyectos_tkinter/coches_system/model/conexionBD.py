import mysql.connector
from tkinter import messagebox

try:
    #Conectar con la BD en MySQL
    conexion=mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='bd_coches'
    )
    #Crear un objeto de tipo cursor que se pueda reutilizar nuevamente
    cursor=conexion.cursor(buffered=True)
except error as e:
    respuestasql=messagebox.showerror(title="Status SQL", message=f"Ocurrió un error {e}, inténtelo más tarde")