class Cliente:

    def __init__(self, nombre, apellido, nombreusuario, contraseña):#3l init es nuestro constructor
        self.nombre = nombre
        self.apellido = apellido
        self.nombreusuario = nombreusuario
        self.contraseña = contraseña

#get
    def getNombre(self):
        return self.nombre
     
    def getApellido(self):
        return self.apellido
    
    def getNombreusuario(self):
        return self.nombreusuario

    def getContraseña(self):
        return self.contraseña
#set
    def setNombre(self, nombre):
        self.nombre = nombre
    
    def setApellido(self, apellido):
        self.apellido = apellido
    
    def setNombreusuario(self, nombreusuario):
        self.nombreusuario = nombreusuario
    
    def setContraseña(self, contraseña):
        self.contraseña = contraseña