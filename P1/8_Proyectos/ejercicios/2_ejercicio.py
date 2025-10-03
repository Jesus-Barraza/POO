'''
Realizar un programam en el cual se declaren dos valores enteros por teclado utilizando el metodo __init__. Calcular después la suma, resta, multiplicación y división. Utilizar un método para cada una e imprimir los resultados obtenidos. Llamar a la clase "Calculadora"
'''

'''class Calculadora():
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2

    #lo puse como "properties" en vez de "property", diré la frase de La Beriso - Imagínate (minuto 00:47)
    @property
    def numero1(self):
        return self.num1
    @numero1.setter
    def numero1(self,n1):
        self.num1=n1

    @property
    def numero2(self):
        return self.num2
    @numero2.setter
    def numero2(self,n2):
        self.num2=n2


    def suma(self):
        sum=self.num1+self.num2
        return sum
    def resta(self):
        res=self.num1-self.num2
        return res
    def multiplicacion(self):
        mul=self.num1*self.num2
        return mul
    def division(self):
        div=self.num1/self.num2
        return div

a=int(input("Ingrese el primer número: "))
b=int(input("Ingrese el segundo número: "))

valor1=Calculadora(a,b)

#se me olvidó los paréntesis, ese error ni es del paradigma OO, creo que voy a persona3
print(f"suma:{valor1.suma()}, \nresta:{valor1.resta()}, \nmultiplicación:{valor1.multiplicacion()}, \ndivisión{valor1.division()}")'''

class Calculadora():
    def __init__(self):
        self._numero1=int(input("Ingrese el primer numero"))
        self._numero2=int(input("Ingrese el segundo numero"))


    @property
    def numero1(self):
        return self._numero1
    @numero1.setter
    def numero1(self,n1):
        self._numero1=n1
    @property
    def numero2(self):
        return self._numero2
    @numero2.setter
    def numero2(self,n2):
        self._numero2=n2


    def sumar(self):
        return self._numero1+self._numero2
    def restar(self):
        return self._numero1-self._numero2
    def multiplicar(self):
        return self._numero1*self._numero2
    def dividir(self):
        return self._numero1/self._numero2
    
valor1=Calculadora()
print(f"suma:{valor1.sumar()}, \nresta:{valor1.restar()}, \nmultiplicación:{valor1.multiplicar()}, \ndivisión:{valor1.dividir()}")