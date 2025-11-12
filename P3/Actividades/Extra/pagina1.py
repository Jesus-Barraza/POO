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
                print("\n\t\t..:: CALCULADORA BÁSICA :::. \n\t 1.- Suma \n\t 2.- Resta \n\t 3.- Multip