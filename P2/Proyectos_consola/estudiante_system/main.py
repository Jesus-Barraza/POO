import conexionDB
import funciones
from model import estudiante

def menu():
    ini=True
    while ini:
        funciones.borrarPantalla()
        print("\n\t Resultados de la calificación")
        ini=input("\n1-Registrar Alumno \n2-Mostrar lista de Notas \n3-Actualizar alumno \n4-Eliminar alumno \n5-Ver nota\n6-Salir (1-6): ").strip()
        if ini=="1":
            funciones.borrarPantalla()
            persona=estudiante.Estudiante(input("Ingrese el nombre del alumno: "), float(input("Ingrese la calificación: ")))
            res=persona.insertar(persona.nombre, persona.nota)
            if res:
                print("Se ha insertado el alumno con éxito")
            else:
                print("Ocurrió un error, inténtelo de nuevo")
            funciones.pulsarTecla()
        elif ini=="2":
            funciones.borrarPantalla()
            estudiante.Estudiante.mostrar()
            funciones.pulsarTecla()
        elif ini=="3":
            funciones.borrarPantalla()
            estudiante.Estudiante.mostrar()
            id=int(input("Ingrese la ID del alumno a actualizar: "))
            alumno=estudiante.Estudiante(input("Ingrese el nombre actualizado: "), float(input("Ingrese la nueva calificación del alumno: ")))
            res=alumno.actualizar(alumno.nombre, alumno.nota, id)
            if res:
                print("Se actualizó el alumno con éxito")
            else:
                print("Ocurrió un error, inténtelo de nuevo")
            funciones.pulsarTecla()
        elif ini=="4":
            funciones.borrarPantalla()
            estudiante.Estudiante.mostrar()
            id=int(input("Inserte el ID del alumno a eliminar: "))
            res=estudiante.Estudiante.eliminar(id)
            if res:
                print("Se eliminó el alumno con éxito")
            else:
                print("Ocurrió un error, inténtelo más tarde")
            funciones.pulsarTecla()
        elif ini=="5":
            funciones.borrarPantalla()
            estudiante.Estudiante.mostrar()
            id=int(input("Ingrese la ID del estudiante: "))
            estudiante.Estudiante.impresion(id)
            funciones.pulsarTecla()
        elif ini=="6":
            funciones.borrarPantalla()
            print("Se ha finalizado la ejecución del programa")
            ini=False
        else:
            print("La selección no es válida, inténtelo de nuevo")
            funciones.pulsarTecla()
            ini=True

if __name__ == "__main__":
    if conexionDB.connect()==True:
        menu()