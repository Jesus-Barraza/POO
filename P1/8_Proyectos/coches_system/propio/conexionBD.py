import mysql.connector

try:
    conexion=mysql.connector.connect(
        host="::1",
        user="root",
        password="",
        database="bd_coches",
    )
    cursor=conexion.cursor(buffered=True)
except:
    print("No fue posible conectarse a la base de datos")