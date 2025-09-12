'''
    PRÁCTICA #1 - Implementar el paradigma estructurado vs POO
Elaborar un programa que obtenga el área de un rectángulo
'''

idea1=input("¿Desea entrar al programa estructurado? (si/no): ").lower().strip()
if idea1=="si":
    #Estructurado
    import os

    def AreaBH(base, altura):
        area=base*altura
        return area

    def BorrarPantalla():
        os.system("cls")

    opc="si"
    while opc=="si":
        BorrarPantalla()
        print("\n\t\t -\|Cálculo del área del rectángulo|/-")
        b=float(input("\nIntroduzca la base del rectángulo (Unidades, solo números): "))
        h=float(input("Introduzca la altura del rectángulo (Unidades, solo números): "))
        a=AreaBH(b,h)
        print(f"\n\tEl área del rectángulo con base {b} y altura {h} es de: {a} unidades cuadradas")
        print("\n\n\t¡Operación realizada con éxito!")
        opc=input("¿Desea realizar otro cálculo del área del cuadrado? (si/no): ").lower().strip()

    BorrarPantalla()
    print("\t\tSe ha finalizado el programa \n\n\t\t\t ¡Muchas gracias!")

idea2=input("¿Desea entrar al POO sin atributos? (si/no): ").lower().strip()
if idea2=="si":
    #OO
    import os
    os.system("cls")
    class AreaRectangulos:
        def AreaBH(self,base,altura):
            area=base*altura
            return area
    
    rectangulo1=AreaRectangulos()   #Instanciar un objeto de la clase "AreaRectangulos"
    b=float(input("\nIntroduzca la base del rectángulo (Unidades, solo números): "))
    h=float(input("Introduzca la altura del rectángulo (Unidades, solo números): "))

    print(f"\n\tEl área del rectángulo con base {b} y altura {h} es de: {rectangulo1.AreaBH(b,h)} unidades cuadradas")

idea3=input("¿Desea entrar al POO con atributos? (si/no): ").lower().strip()
if idea3=="si":
    #OO con atributos
    import os
    os.system("cls")
    class AreaRectangulos:
        def __init__(self,base,altura):
            self.base=base
            self.altura=altura
        def AreaBH(self):
            area=self.base*self.altura
            return area
    
    b=float(input("\nIntroduzca la base del rectángulo (Unidades, solo números): "))
    h=float(input("Introduzca la altura del rectángulo (Unidades, solo números): "))
    rectangulo1=AreaRectangulos(b,h)   #Instanciar un objeto de la clase "AreaRectangulos"

    print(f"\n\tEl área del rectángulo con base {b} y altura {h} es de: {rectangulo1.AreaBH()} unidades cuadradas")