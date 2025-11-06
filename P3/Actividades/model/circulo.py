from . import figura

class Circulos(figura.Figuras):
    def __init__(self, x, y, visible, radio):
        super().__init__(x, y, visible)
        self.__radio=radio
    
    @property
    def radio(self):
        return self.__radio
    @radio.setter
    def radio(self, r):
        self.__radio=r

    def ocultar(self):
        self.visible=False

    def mostrar(self):
        self.visible=True

    def calcularArea(self):
        import math
        area=math.pi*(self.__radio*self.__radio)
        return f"El área del rectángulo es de {area}"
