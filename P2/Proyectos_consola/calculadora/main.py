#Programa de operaciones matemáticas

#Importaciones
import os
from model import calculadora


class App():
    def __init__(self):
        self.menu()

    @staticmethod
    def borrarPantalla():
        os.system("cls")

    @staticmethod
    def esperarTecla():
        input("\n... Oprima enter para continuar ...")

    def menu(self):
        opera=0
        while opera!=7:
            try:
                self.borrarPantalla()
                print("\n\t\t..:: CALCULADORA BÁSICA :::. \n\t 1.- Suma \n\t 2.- Resta \n\t 3.- Multiplicacion \n\t 4.- Division \n\t 5.- Potencia \n\t 6.- Raiz \n\t 7.-Salir")
                opera=int(input("\n\t\t Selecciona un opción:  "))

                if opera>=1 and opera<=6:
                        #entrada
                    self.borrarPantalla()
                    print("\n\t Ingrese los numeros: ")
                    num1=float(input("Número #1: "))
                    num2=float(input("Número #2: "))

                    ope=""
                    if opera==1:
                        ope=f"{num1} + {num2} = {round(calculadora.Calculadora.suma(num1,num2),3)}"
                    elif opera==2:
                        ope=f"{num1} - {num2} = {round(calculadora.Calculadora.resta(num1,num2),3)}"
                    elif opera==3:
                        ope=f"{num1} * {num2} = {round(calculadora.Calculadora.multiplicacion(num1,num2),3)}"
                    elif opera==4:
                        try:
                            ope=f"{num1} / {num2} = {round(calculadora.Calculadora.division(num1,num2),3)}"
                        except TypeError:
                            ope=f"{calculadora.Calculadora.division(num1,num2)}"
                    elif opera==5:
                        ope=f"{num1} ^ {num2} = {round(calculadora.Calculadora.potenciacion(num1,num2),3)}"
                    elif opera==6:
                        try:
                            ope=f"raiz {num2} de {num1} = {round(calculadora.Calculadora.raiz(num1,num2),3)}"
                        except TypeError:
                            ope=f"Este número entra en el rango de los imaginarios"
                    else:
                        print("Este operacion no existe")

                    print(f"\n\t\t {ope}")
                    self.esperarTecla()

                elif opera==7:
                    self.borrarPantalla()
                    print("\n\t\t..::Terminó la ejecución del SW::..")

                else:
                    print("\n\tOperación no válida, vuelva a intentarlo otra vez")
                    self.esperarTecla()
            except ValueError:
                print("\n\tIngrese solo valores numéricos")
                self.esperarTecla()
            except:
                print("\n\tOperación no válida, vuelva a intentarlo otra vez")
                self.esperarTecla() 

if __name__=="__main__":
    app=App()