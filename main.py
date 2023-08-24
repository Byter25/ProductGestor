from view import login as l,index as i 
import customtkinter as ctk

# ctk.set_appearance_mode("system")
# ctk.set_default_color_theme("green")

recordarme = True

vtn = ctk.CTk()

vtn.title("Gestor de Productos")
vtn.iconbitmap("assets/logo.ico")

# vtn.update_idletasks()

if recordarme:
  app = i.App(vtn)
  wight = 1080
  height = 600

else:
  app = l.Login(vtn)
  vtn.resizable(width=False,height=False)
  wight = 500
  height = 600

x = (vtn.winfo_screenwidth() // 2) - (wight // 2)
y = (vtn.winfo_screenheight() // 2) - (height // 2)


vtn.geometry(f"{wight}x{height}+{x}+{y}")
vtn.mainloop()