

class Universidad():
    def __init__(self, nombre_uni):
        self._nombre_uni=nombre_uni

    @property
    def nombre_uni(self):
        return self._nombre_uni
    @nombre_uni.setter
    def nombre_uni(self, nom):
        self._nombre_uni=nom

class Carrera():
    def __init__(self, especialidad):
        self._especialidad=especialidad

    @property
    def especialidad(self):
        return self._especialidad
    @especialidad.setter
    def especialidad(self, esp):
        self._especialidad=esp

class Estudiante(Universidad, Carrera):
    def __init__(self, nombre, edad, nombre_uni, especialidad):
        self._nombre=nombre
        self._edad=edad
        Universidad.__init__=nombre_uni
        Carrera.__init__=especialidad

    @property
    def nombre(self):
        return self._nombre   
    @nombre.setter
    def nombre(self, nom):
        self._nombre=nom

    @property
    def edad(self):
        return self._edad
    @edad.setter
    def edad(self, eda):
        self._edad=eda

persona=Estudiante("Joaquin", 19, "UTD", "TI")
print(persona.nombre, persona.edad, persona.nombre_uni, persona.especialidad)