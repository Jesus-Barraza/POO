import os
os.system("cls")

class profesores:
    def __init__ (self,name,xp,numero):
        self.__nombre_profesor=name
        self.__experiencia=xp
        self.__num_profesor=numero

    @property
    def nombre_profesor (self):
        return self.__nombre_profesor
    @nombre_profesor.setter
    def nombre_profesor (self,nom):
        self.__nombre_profesor=nom

    @property
    def experiencia (self):
        return self.__experiencia
    @experiencia.setter
    def experiencia (self,exp):
        self.__experiencia=exp

    @property
    def numero_profesor (self):
        return self.__num_profesor
    @numero_profesor.setter
    def numero_profesor (self,num):
        self.__num_profesor=num


    def impartir(self):
        print(f"El profesor {self.__nombre_profesor} impartirá la clase!")
    
    def evaluar(self):
        print(f"¡Atención toda la clase! ¡{self.__nombre_profesor} evaluará sus esfuerzos!")

class cursos:
    def __init__ (self,name,code,credit):
        self.__nombre_curso=name
        self.__codigo=code
        self.__creditos=credit

    @property
    def nombre_curso (self):
        return self.__nombre_curso
    @nombre_curso.setter
    def nombre_curso (self,nom):
        self.__nombre_curso=nom

    @property
    def codigo (self):
        return self.__codigo
    @codigo.setter
    def codigo (self,cod):
        self.__experiencia=cod

    @property
    def creditos (self):
        return self.__creditos
    @creditos.setter
    def creditos (self,cdt):
        self.__creditos=cdt


    def asignar(self):
        print(f"Alguien se asignó a la clase {self.__nombre_curso}!")

class alumnos:
    def __init__ (self,name,age,mat):
        self.__nombre_alumno=name
        self.__edad=age
        self.__matricula=mat

    @property
    def nombre_alumno (self):
        return self.__nombre_alumno
    @nombre_alumno.setter
    def nombre_alumno (self,nom):
        self.__nombre_alumno=nom

    @property
    def edad (self):
        return self.__edad
    @edad.setter
    def edad (self,eda):
        self.__edad=eda

    @property
    def matricula (self):
        return self.__matricula
    @matricula.setter
    def matricula (self,id):
        self.__matricula=id


    def inscribirse (self):
        print(f"¡{self.__nombre_alumno} se ha inscrito a un curso!")
    
    def estudiar(self):
        print(f"{self.__nombre_alumno} ha decidido estudiar, bien hecho :)")

profesor1=profesores("Ana Torres Guzman", 40, 123)
profesor2=profesores("Daniel Contreras", 35, 124)
curso1=cursos("POO", 100, 6)
curso2=cursos("FOSO", 101, 4)
alumno1=alumnos("Juan Correa Simental", 25, 100123)
alumno2=alumnos("María Serrano Mata", 22, 100124)

print(f"{profesor1.nombre_profesor}, {profesor1.experiencia}, {profesor1.numero_profesor}")
print(f"{profesor2.nombre_profesor}, {profesor2.experiencia}, {profesor2.numero_profesor}")
print(f"{curso1.nombre_curso}, {curso1.codigo}, {curso1.creditos}")
print(f"{curso2.nombre_curso}, {curso2.codigo}, {curso2.creditos}")
print(f"{alumno1.nombre_alumno}, {alumno1.edad}, {alumno1.matricula}")
print(f"{alumno2.nombre_alumno}, {alumno2.edad}, {alumno2.matricula}")

profesor1.impartir()
profesor2.evaluar()
curso1.asignar()
curso2.asignar()
alumno1.inscribirse()
alumno2.estudiar()