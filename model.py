import sqlite3 as sqli

class Conexion:
  def __init__(self,_nomDB):
    self._nomDB = _nomDB
    self._cnx = sqli.connect(_nomDB)
    self._cs =self._cnx.cursor()
        
    sql = '''
    CREATE TABLE IF NOT EXISTS usuarios(
      id INTEGER PRIMERY KEY, 
      nombre TEXT, 
      apellido TEXT, 
      usuario TEXT,
      correo TEXT, 
      contraseña TEXT)'''
      
    sql2 ='''INSERT INTO usuarios (usuario,contraseña) VALUES (?,?)'''
    usuario = "admin"
    contraseña = "admin"
    self._cs.execute(sql)
    self._cs.execute(sql2,(usuario,contraseña))

class UserAd(Conexion):
  def __init__(self):
    super().__init__("DB/usuarios.db")

  def buscar(self,bUser:str,bCorreo=None):
    if bCorreo != None:
      sql = "SELECT * FROM usuarios WHERE correo=?"
      res = self._cs.execute(sql,(bCorreo,))
    else:
      sql = "SELECT * FROM usuarios WHERE usuario=?"
      res = self._cs.execute(sql,(bUser,))
    
    res = self._cs.fetchone()
    return res
  
  def leer(self): pass
  def registar (self): pass
  def actualizar(self): pass
  def eliminar(self): pass

class User:
  def __init__(self,__id:int,__nombre:str,__apellido:str,__user:str,__correo:str,__contra:str):
    self.__id = __id
    self.__nom = __nombre
    self.__ape = __apellido
    self.__user = __user
    self.__correo = __correo
    self.__contra = __contra
  
  def getId(self): return self.__id
  def getNom(self): return self.__nom
  def getApe(self): return self.__ape
  def getUser(self): return self.__user
  def getCorreo(self): return self.__correo
  def getContra(self): return self.__contra

  def setId(self,id:int): self.__id = id
  def setNom(self,nombre:str): self.__nom = nombre
  def setApe(self,apellido:str): self.__ape = apellido
  def setUser(self,usuario:str): self.__user = usuario
  def setCorreo(self,correo:str): self.__correo = correo
  def setContra(self,contra:str): self.__contra = contra
    
class Producto:
  def __init__(self,__id:int,__nombre:str,__descripcion:str,__cantidad:int,__precio:float):
    self.__id = __id
    self.__nom = __nombre
    self.__desc = __descripcion
    self.__cant = __cantidad
    self.__precio = __precio
        
  def getId(self): return self.__id
  def getNombre(self): return self.__nom
  def getDescripcion(self): return self.__desc
  def getCantidad(self): return self.__cant
  def getPrecio(self): return self.__precio
    
  def setId(self,id:int): self.__id = id
  def setNombre(self,nombre:str): self.__nom = nombre
  def setDescripcion(self,descripcion:str): self.__desc = descripcion
  def setCantidad(self,cantidad:int): self.__cant = cantidad
  def setPrecio(self,precio:float): self.__precio = precio
    