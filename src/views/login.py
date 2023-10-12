from PIL import Image, ImageTk
import customtkinter as ctk
import src.controllers.controller as ctr
class Login():
  def __init__(self,vtn):
    # ---INICIADO DE LA APLICACION---
    vtn.lift()
    # DEFNICION
    logoPil = Image.open("assets/icon-gestion.png")
    logo = ctk.CTkImage(light_image= logoPil,dark_image=logoPil,size=(200,200))
    lblImage = ctk.CTkLabel(vtn,image=logo,text="")
    lblUser = ctk.CTkLabel(vtn,text="USUARIO")
    lblContra = ctk.CTkLabel(vtn,text="CONTRASEÑA")
    entryUser = ctk.CTkEntry(vtn,width=300)
    entryContra = ctk.CTkEntry(vtn,width=300)
    btnLog = ctk.CTkButton(vtn,text="Logear",command=lambda:ctr.logear(vtn = vtn,lUser=entryUser.get(),
                                                                       lContra=entryContra.get()))
    checkRecordar = ctk.CTkCheckBox(vtn,text="Recordarme")
    
    
    # INVOCACION
    lblImage.place(relx=0.5,rely=0.2,anchor="center")
    lblUser.place(relx=0.5,rely=0.45,anchor="center")
    entryUser.place(relx=0.5,rely=0.5,anchor="center")
    lblContra.place(relx=0.5,rely=0.6,anchor="center")
    entryContra.place(relx=0.5,rely=0.65,anchor="center")
    checkRecordar.place(relx=0.5,rely=0.75,anchor="center")
    btnLog.place(relx=0.5,rely=0.8,anchor="center")
    
    
    # vtn.overrideredirect(True)
    # vtn.wm_attributes("-topmost", 1)
