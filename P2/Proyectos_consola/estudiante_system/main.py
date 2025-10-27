import conexionDB
from model import estudiante

class App():
    def __init__(self):
        self.menu()

    @staticmethod
    def borrarPantalla():
        import os
        os.system("cls")

    @staticmethod
    def pulsarTecla():
        input("Presione enter para continuar")

    @staticmethod
    def respuesta_sql(dato):
        if dato:
            print("Se realizó la acción con éxito")
        else:
            print("Ocurrió un error, inténtelo de nuevo")

    @staticmethod
    def menu_opciones_estudiantes():
        print("\n\t Resultados de la calificación")
        opcion=input("\n1-Registrar Alumno \n2-Mostrar lista de Notas \n3-Actualizar alumno \n4-Eliminar alumno \n5-Ver nota\n6-Salir (1-6): ").strip()
        return opcion
    
    def datos_estudiantes(self):
        nombre=input("Ingrese el nombre del alumno:")
        nota=input("Inserte la calificación: ")
        return nombre, nota

    def menu_estudiantes(self):
        opc=True
        while opc:
            self.borrarPantalla()
            opc=self.menu_opciones_estudiantes()
            if opc=="1":
                self.borrarPantalla()
                dato=self.datos_estudiantes()
                self.respuesta_sql(estudiante.Estudiante.insertar(dato[0],dato[1]))
                self.pulsarTecla()
            elif opc=="2":
                self.borrarPantalla()
                estudiante.Estudiante.mostrar()
                self.pulsarTecla()
            elif opc=="3":
                self.borrarPantalla()
                estudiante.Estudiante.mostrar()
                id=int(input("Ingrese la ID del alumno a actualizar: "))
                dato=self.datos_estudiantes()
                self.respuesta_sql(estudiante.Estudiante.actualizar(dato[0],dato[1],id))
                self.pulsarTecla()
            elif opc=="4":
                self.borrarPantalla()
                estudiante.Estudiante.mostrar()
                id=int(input("Inserte el ID del alumno a eliminar: "))
                self.respuesta_sql(estudiante.Estudiante.eliminar(id))
                self.pulsarTecla()
            elif opc=="5":
                self.borrarPantalla()
                estudiante.Estudiante.mostrar()
                id=int(input("Ingrese la ID del estudiante: "))
                estudiante.Estudiante.impresion(id)
                self.pulsarTecla()
            elif opc=="6":
                self.borrarPantalla()
                print("Se ha finalizado la ejecución del programa")
                opc=False
            else:
                print("La selección no es válida, inténtelo de nuevo")
                self.pulsarTecla()
                opc=True

    def menu(self):
        self.menu_estudiantes()

if __name__ == "__main__":
    if conexionDB.connect()==True:
        main=App()