class Cancion:

    def __init__(self, id, nombre, artista, album, imagen, fecha, linkspoti, linkyoutu):#3l init es nuestro constructor
        self.id = id
        self.nombre = nombre
        self.artista = artista
        self.album = album
        self.imagen = imagen 
        self.fecha = fecha
        self.linkspoti = linkspoti
        self.linkyoutu = linkyoutu


#get
    
    def getId(self):
        return self.id
     
    def getNombre(self):
        return self.nombre
      
    def getArtista(self):
        return self.artista

    def getAlbum(self):
        return self.album

    def getImagen(self):
        return self.imagen

    def getFecha(self):
        return self.fecha
    
    def getLinkspoti(self):
        return self.linkspoti

    def getLinkyoutu(self):
        return self.linkyoutu
#set
    def setId(self, id):
        self.id = id

    def setNombre(self, nombre):
        self.nombre = nombre
    
    def setArtista(self, artista):
        self.artista = artista
    
    def setAlbum(self, album):
        self.album = album
    
    def setImagen(self, imagen):
        self.imagen = imagen
    
    def setFecha(self, fecha):
        self.fecha = fecha
    
    def setLinkspoti(self, linkspoti):
        self.linkspoti = linkspoti
    
    def setLinkyoutu(self, linkyoutu):
        self.linkyoutu = linkyoutu
    

    