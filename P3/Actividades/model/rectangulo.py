from . import figura

class Rectangulos(figura.Figuras):
    def __init__(self, x, y, visible, alto, ancho):
        super().__init__(x, y, visible)
        self.__alto=alto
        self.__ancho=ancho
    
    @property
    def alto(self):
        return self.__alto
    @alto.setter
    def alto(self, h):
        self.__alto=h

    @property
    def ancho(self):
        return self.__ancho
    @ancho.setter
    def ancho(self, b):
        self.__ancho=b

    def ocultar(self):
        self.visible=False

    def mostrar(self):
        self.visible=True

    def calcularArea(self):
        area=self.__alto*self.__ancho
        return f"El área del rectángulo es de {area}"
    