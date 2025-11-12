#Importaciones
import math

class Calculadora():
    @staticmethod
    def suma(n1,n2):
        return n1+n2
    
    @staticmethod
    def resta(n1,n2):
        return n1-n2
    
    @staticmethod
    def multiplicacion(n1,n2):
        return n1*n2
    
    @staticmethod
    def division(n1,n2):
        return n1/n2

    @staticmethod
    def potenciacion(n1,n2):
        return n1**n2

    @staticmethod
    def raiz(n1,n2):
        return n1**(1/n2)