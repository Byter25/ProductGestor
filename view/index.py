import customtkinter as ctk
import controller as ctr
import model as m
class App():
  def __init__(self,root):
    self.root = root    
    self.menu()    
    ############################
    #    GESTIONAR PRODUCTO    #
    ############################
    self.frmProducto = ctk.CTkFrame(root)
    self.frm_Prducto(self.frmProducto)
    ############################
    #     GESTIONAR TABLA      #
    ############################
    self.frmTabla = ctk.CTkFrame(root,fg_color="red")
    self.frm_Tabla(self.frmTabla)
    ############################
    #    GESTIONAR USUARIOS    #
    ############################
    self.frmUsuarios = ctk.CTkFrame(root,fg_color="black")
    self.frm_Usuario(self.frmUsuarios)
    ############################
    #    GESTIONAR CLIENTES    #
    ############################
    self.frmCliente = ctk.CTkFrame(root,fg_color="yellow")
    self.frm_Cliente(self.frmCliente)
    
    self.grupoMenu = {self.frmProducto,self.frmTabla,self.frmUsuarios,self.frmCliente}
  
  
  def menu(self):
    ############################
    #                          #
    #       MENU GESTION       #
    #                          #
    ############################ 
    f_Pestañas = ctk.CTkFrame(self.root, height=45, border_width=3)
    f_Pestañas.pack(side="top",fill="x")
    
    lblTitulo = ctk.CTkLabel(f_Pestañas,text="GESTIONAR")
    
    btnProducto = ctk.CTkButton(f_Pestañas, text="PRODUCTO", command=lambda:self.show_frame(self.frmProducto , self.grupoMenu))
    btnUsuario = ctk.CTkButton(f_Pestañas, text="USUARIO", command=lambda:self.show_frame(self.frmTabla, self.grupoMenu))
    btnTabla = ctk.CTkButton(f_Pestañas, text="TABLA", command=lambda:self.show_frame(self.frmUsuarios,self.grupoMenu))
    btnCliente = ctk.CTkButton(f_Pestañas, text="CLIENTE", command=lambda:self.show_frame(self.frmCliente, self.grupoMenu))
    
    lblTitulo.pack(side="left",expand=True)
    
    btnProducto.pack(side="left", padx=4, pady=5)
    btnUsuario.pack(side="left", padx=4)
    btnTabla.pack(side="left", padx=4)
    btnCliente.pack(side="left", padx=4)
    ###################################################
  
          
  def frameCRUD(self,framP,botones):
    frameCrud = ctk.CTkFrame(framP,border_width=5,fg_color="#0A2229")
    frameCrud.pack(side="right",fill="y")
    for i in botones:
      ctk.CTkButton(frameCrud,text=i.texto,fg_color=i.color,command=i.comando).pack(padx=i.padx,pady=i.pady)
        
  
  def show_frame(self,pestana:ctk.CTkFrame,grouPes):
    for pest in grouPes:
        if pest != pestana:
          pest.pack_forget()
        else:
          pestana.pack(fill="both",expand=True)
  
          
  def frm_Prducto(self,frame):
    createProd = ctk.CTkFrame(frame, fg_color="#3B0B0B", border_width=3)
    readProd = ctk.CTkFrame(frame, fg_color="#3B0B0B", border_width=3)
    updateProd = ctk.CTkFrame(frame, fg_color="#3B0B0B", border_width=3)
    deleteProd = ctk.CTkFrame(frame, fg_color="#3B0B0B", border_width=3)
    
    grupoSeccion = {createProd, readProd, updateProd, deleteProd}
    
    self.frameCRUD(frame,
                   [m.Boton("agregar","green",lambda:self.show_frame(createProd,grupoSeccion),10,10),
                    m.Boton("ver","green",lambda:self.show_frame(readProd,grupoSeccion),10,10),
                    m.Boton("actualizar","green",lambda:self.show_frame(updateProd,grupoSeccion),10,10),
                    m.Boton("eliminar","green",lambda:self.show_frame(deleteProd,grupoSeccion),10,10)])
    
    ctk.CTkLabel(createProd, text="ID ASIGNADO", width=100, height=30, anchor="e").grid(row=0,column=0,padx=10,pady=10)
    ctk.CTkLabel(createProd, text="NOMBRE", width=100, height=30, anchor="e").grid(row=1,column=0,padx=10,pady=10)    
    ctk.CTkLabel(createProd, text="DESCRIPCION", width=100, height=30, anchor="e").grid(row=2,column=0,padx=10,pady=10)
    ctk.CTkLabel(createProd, text="CANTIDAD", width=100, height=30, anchor="e").grid(row=3,column=0,padx=10,pady=10)
    ctk.CTkLabel(createProd, text="PRECIO", width=100, height=30, anchor="e").grid(row=4,column=0,padx=10,pady=10)
    
    fc_entryId = ctk.CTkEntry(createProd,width=300).grid(row=0,column=1,padx=10,pady=10)
    fc_entryNom = ctk.CTkEntry(createProd, width=300).grid(row=1,column=1,padx=10,pady=10)
    fc_entryDesc = ctk.CTkEntry(createProd, width=300).grid(row=2,column=1,padx=10,pady=10)
    fc_entryCant = ctk.CTkEntry(createProd, width=300).grid(row=3,column=1,padx=10,pady=10)
    fc_entryPrecio = ctk.CTkEntry(createProd, width=300).grid(row=4,column=1,padx=10,pady=10)
    
    ctk.CTkButton(createProd,text="GUARDAR").grid(column=1,sticky="e",padx=10,pady=10)
     
  def frm_Tabla(self,frame):
    pass
  
  def frm_Usuario(self,frame):
    pass
  
  def frm_Cliente(self,frame):
    pass