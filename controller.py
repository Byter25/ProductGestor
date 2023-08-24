import model
from view import error as e
sUser = model.UserAd()

def logear(vtn,lUser:str,lContra:str):
  if lContra != "":
    user = sUser.buscar(bUser=lUser)
    if user != None:
      userLog = model.User(user[0],user[1],user[2],user[3],user[4],user[5])
      if userLog.getContra() == lContra:
        print("bienvenido")
      else:
        e.Error(vtn,msj='INCORRECTO')
    else:
      e.Error(vtn,msj='USUARIO NO REGISTRADO')
  else:
    e.Error(vtn,msj='CAMPOS INCOMPLETOS')

def registrar():
  pass

def recordar():
  pass