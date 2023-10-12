import customtkinter as ctk
 
class Error():
  def __init__(self,vtn,msj):
    
    error = ctk.CTkToplevel()
    error.title("ERROR")
    error.iconbitmap(default="assets/error.ico")
    
    
    lblMsj = ctk.CTkLabel(error,text=msj,text_color="red",font=("",20,"bold"))
    lblMsj.place(relx=0.5,rely=0.5,anchor="center")
    error.resizable(width=False,height=False)
    
    wight:int = 300
    height:int = 50

    x = (vtn.winfo_screenwidth() // 2) - (wight // 2)
    y = (vtn.winfo_screenheight() // 2) - (height // 2)
    
    error.geometry(f"{wight}x{height}+{x+300}+{y}")
    error.grab_set()