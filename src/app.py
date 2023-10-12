from customtkinter import CTk
from src.views.index import App
from src.views.login import Login
def inicializa():
  recordarme = False

  vtn = CTk()

  vtn.title("Gestor de Productos")
  vtn.iconbitmap("assets/logo.ico")
  # vtn.update_idletasks()
  if recordarme:
    app = App(vtn)
    wight = 1080
    height = 600
  else:
    app = Login(vtn)
    vtn.resizable(width=False,height=False)
    wight = 500
    height = 600

  x = (vtn.winfo_screenwidth() // 2) - (wight // 2)
  y = (vtn.winfo_screenheight() // 2) - (height // 2)


  vtn.geometry(f"{wight}x{height}+{x}+{y}")
  vtn.mainloop()