class Play:

    def __init__(self, linkspoti, id, persona, imagen):
        self.linkspoti = linkspoti
        self.id = id
        self.persona = persona
        self.imagen = imagen


        
#get
    def getLink(self):
        return self.linkspoti

    def getId(self):
        return self.id

    def getPersona(self):
        return self.persona

    def getImagen(self):
        return self.imagen
     
#set
    def setLink(self, linkspoti):
        self.linkspoti = linkspoti

    def setId(self, id):
        self.id = id
    
    def setPersona(self, persona):
        self.persona = persona
    
    def setImagen(self, imagen):
        self.imagen = imagen
    
