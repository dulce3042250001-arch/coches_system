from concexionBD import cursor, conexion

class Estudiantes:
    def __init__(self, nombre, nota):
        self._nombre=nombre
        self._nota=nota

    # que se puede agregar en get y set para que se pueda utilizar como si estuvieramos utilizando el metodo directamente
    # se utiliza un arroba y algo mas (tema decoradores get y set)
    # metodos estaticos se pueden utilizar sin haber creado un objeto (metodos estaticos)
    @property
    def nombre(self):
        return self._nombre

    @property
    def nota(self):
        return self._nota

    @nombre.setter
    def nombre(self,nombre):
        return self._nombre=nombre

    @nota.setter
    def nota(self,nota):
        return self._nota=nota

    def insertar(self):
        try:
            cursor.execute("insert into estudiantes values(null, %s,%s)", (self._nombre,self._nota))
            conexion.commit()
            return True
        
        except:
            return False 

    @staticmethod
    def consultar(id):
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
        

    def actualizar(self, id):
        try:
            cursor.execute("pudate from estudiantes set nombre=%s,nota=%s where id=%s",(self._nombre,self._nota,id,))
            conexion.commit() 
            return True
        except:
            return False