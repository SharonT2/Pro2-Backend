class Comentario:

    def __init__(self, nombre, id, persona):
        self.nombre = nombre
        self.id = id
        self.persona = persona


        
#get
    def getNombre(self):
        return self.nombre

    def getId(self):
        return self.id

    def getPersona(self):
        return self.persona
     
#set
    def setNombre(self, nombre):
        self.nombre = nombre

    def setId(self, id):
        self.id = id
    
    def setPersona(self, persona):
        self.persona = persona
    
