class Figuras():
    def __init__(self, x, y, visible):
        self.x=x
        self.y=y
        self.visible=visible

    def estaVisible(self):
        return self.visible
    
    def mostrar(self):
        self.visible=True

    def ocultar(self):
        self.visible=False

    def mover(self, x, y):
        self.x=x
        self.y=y

    def calcularArea(self, num):
        return num