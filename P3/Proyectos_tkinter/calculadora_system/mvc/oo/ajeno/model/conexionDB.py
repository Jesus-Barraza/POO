import mysql.connector
from mysql.connector import Error
from tkinter import messagebox

try:
    conexion=mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="bd_operaciones_basicas"
    )
    if conexion.is_connected():
        cursor=conexion.cursor(buffered=True)
        result=True
except Error as e:
    error=messagebox.showerror(message=f"Ocurrió el error {e}, inténtelo más tarde", icon="error", title="Hubo un error al conectar a la base de datos")
    result=False