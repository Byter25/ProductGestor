import customtkinter as ctk
import controller as ctr

class App():
  def __init__(self,root):
    self.root = root    
    self.menu()
    ###############################################################3
    
    self.frmHola = ctk.CTkFrame(root, fg_color="#3B0B0B")
    self.frmHola.pack(fill="both",expand=True)
    
    self.lblHola = ctk.CTkLabel(self.frmHola,text="HOLA MUNDO")
    self.lblHola.pack()
    
    ############################
    #                          #
    #    GESTIONAR PRODUCTO    #
    #                          #
    ############################
    self.frmProduc = ctk.CTkFrame(root)
    
    self.createProd = ctk.CTkFrame(self.frmProduc, fg_color="#3B0B0B", border_width=3)
    self.createProd.pack(side="left",fill="both",expand=True)
    
    self.frameCRUD(self.frmProduc)
    
    self.fc_lblId = ctk.CTkLabel(self.createProd,text="ID ASIGNADO:",width=100,height=30)
    self.fc_entryId = ctk.CTkEntry(self.createProd,width=300)
    
    self.fc_lblNom = ctk.CTkLabel(self.createProd,text="NOMBRE",width=100,height=30)
    self.fc_entryNom = ctk.CTkEntry(self.createProd, width=300)
    
    self.fc_lblDesc = ctk.CTkLabel(self.createProd,text="DESCRIPCION",width=100,height=30)
    self.fc_entryDesc = ctk.CTkEntry(self.createProd, width=300)
    
    fc_lblCant = ctk.CTkLabel(self.createProd,text="CANTIDAD",width=100,height=30)
    fc_entryCant = ctk.CTkEntry(self.createProd, width=300)
    
    fc_lblPrecio = ctk.CTkLabel(self.createProd,text="PRECIO",width=100,height=30)
    fc_entryPrecio = ctk.CTkEntry(self.createProd, width=300)
    
    self.fc_lblId.grid(row=0,column=0,padx=10,pady=10)
    self.fc_entryId.grid(row=0,column=1,padx=10,pady=10)
    self.fc_lblNom.grid(row=1,column=0,padx=10,pady=10)
    self.fc_entryNom.grid(row=1,column=1,padx=10,pady=10)
    self.fc_lblDesc.grid(row=2,column=0,padx=10,pady=10)
    self.fc_entryDesc.grid(row=2,column=1,padx=10,pady=10)
    fc_lblCant.grid(row=3,column=0,padx=10,pady=10)
    fc_entryCant.grid(row=3,column=1,padx=10,pady=10)
    fc_lblPrecio.grid(row=4,column=0,padx=10,pady=10)
    fc_entryPrecio.grid(row=4,column=1,padx=10,pady=10)
    
    #############################
    #                           #
    #     GESTIONAR TABLAS      #
    #                           #
    #############################
    self.frmRead = ctk.CTkFrame(root,fg_color="red")
    self.frameCRUD(self.frmRead)
    
    #################################
    #                               #
    #  Seccion ACTUALIZAR producto  #
    #                               #
    #################################
    self.frmUpdate = ctk.CTkFrame(root,fg_color="black")
    
    ###############################
    #                             #
    #  Seccion Eliminar producto  #
    #                             #
    ###############################
    self.frmDelete = ctk.CTkFrame(root,fg_color="yellow")
    
    
    self.grupoMenu = {self.frmProduc,self.frmRead,self.frmUpdate,self.frmDelete,self.frmHola}
  
  def menu(self):
    ############################
    #                          #
    #       MENU GESTION       #
    #                          #
    ############################ 
    f_Pestañas = ctk.CTkFrame(self.root, height=45, border_width=3)
    f_Pestañas.pack(side="top",fill="x")
    
    lblTitulo = ctk.CTkLabel(f_Pestañas,text="GESTIONAR")
    
    btnProducto = ctk.CTkButton(f_Pestañas, text="PRODUCTO", command=lambda:self.show_frame(self.frmProduc, self.grupoMenu))
    btnUsuario = ctk.CTkButton(f_Pestañas, text="USUARIO", command=lambda:self.show_frame(self.frmRead, self.grupoMenu))
    btnTabla = ctk.CTkButton(f_Pestañas, text="TABLA", command=lambda:self.show_frame(self.frmUpdate, self.grupoMenu))
    btnCliente = ctk.CTkButton(f_Pestañas, text="CLIENTE", command=lambda:self.show_frame(self.frmDelete, self.grupoMenu))
    
    lblTitulo.pack(side="left",expand=True)
    
    btnProducto.pack(side="left", padx=4, pady=5)
    btnUsuario.pack(side="left", padx=4)
    btnTabla.pack(side="left", padx=4)
    btnCliente.pack(side="left", padx=4)
    
    
    ###################################################
          
  def frameCRUD(self,framP):
    frameCrud = ctk.CTkFrame(framP,border_width=5,fg_color="#0A2229")
    frameCrud.pack(side="right",fill="y")
    
    ctk.CTkButton(frameCrud,text="AGREGAR",fg_color="green" ).pack(padx=10,pady=10)
    ctk.CTkButton(frameCrud,text="VER").pack(padx=10,pady=10)
    ctk.CTkButton(frameCrud,text="ACTUALIZAR").pack(padx=10,pady=10)
    ctk.CTkButton(frameCrud,text="ELIMINAR").pack(padx=10,pady=10)
    
    
    
  def show_frame(self,pestana:ctk.CTkFrame,grouPes):
    for pest in grouPes:
        if pest != pestana:
          pest.pack_forget()
        else:
          pestana.pack(fill="both",expand=True)
          
 