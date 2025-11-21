from . import conexionDB

class Operaciones():
    def __init__(self, n1, n2, sim, res):
        self._n1=n1
        self._n2=n2
        self._sim=sim
        self._res=res
        self.insertar()

    def insertar(self):    
        try:
          conexionDB.cursor.execute(
            "insert into operaciones values(null,NOW(),%s,%s,%s,%s)",
            (self._n1,self._n2,self._sim,self._res)
          )
          conexionDB.conexion.commit()
          return True
        except:
          return False

    @staticmethod
    def mostrar():
        try:
          conexionDB.cursor.execute(
            "select * from operaciones"
          )
          return conexionDB.cursor.fetchall()
        except:
          return []

    @staticmethod
    def actualizar(id, n1, n2, sim, res):
       Operaciones.mostrar()
       try:
         conexionDB.cursor.execute(
            "update operaciones set fecha=NOW(),numero1=%s,numero2=%s,operacion=%s,resultado=%s where id=%s",
            (n1,n2,sim,res,id)
         )
         conexionDB.conexion.commit()
         return True
       except: 
         return False
    
    @staticmethod
    def eliminar(id):
        Operaciones.mostrar()
        try:
          conexionDB.cursor.execute(
            "delete from operaciones where id=%s",
            (id,)
          ) 
          conexionDB.conexion.commit() 
          return True  
        except:    
          return False
        
