from concexionBD import cursor, conexion

class Estudiantes:

    def insertar(self,nombre,nota):
        try:
            cursor.execute("insert into estudiantes values(null, %s,%s)", (self._nombre,self._nota))
            conexion.commit()
            return True
        
        except:
            return False 

    @staticmethod
    def consultar():
        try:
            cursor.execute("select * from estudiantes")
            return cursor.fetchall()
        except:
            return []

    @staticmethod
    def eliminar(id):
        try:
            cursor.execute("delete * from estudiantes where id=%s", (id,))
            conexion.commit() 
            return True
        except:
            return False
        

    def actualizar(self,nombre,nota,id):
        try:
            cursor.execute("pudate from estudiantes set nombre=%s,nota=%s where id=%s",(self._nombre,self._nota,id,))
            conexion.commit() 
            return True
        except:
            return False