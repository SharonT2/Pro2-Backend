class Solicitud:

    def __init__(self, idv, nombrev, artistav, albumv, imagenv, fechav, linkspotiv, linkyoutuv):#3l init es nuestro constructor
        self.idv = idv
        self.nombrev = nombrev
        self.artistav = artistav
        self.albumv = albumv
        self.imagenv = imagenv 
        self.fechav = fechav
        self.linkspotiv = linkspotiv
        self.linkyoutuv = linkyoutuv


#get
    
    def getIdv(self):
        return self.idv
     
    def getNombrev(self):
        return self.nombrev
      
    def getArtistav(self):
        return self.artistav

    def getAlbumv(self):
        return self.albumv

    def getImagenv(self):
        return self.imagenv

    def getFechav(self):
        return self.fechav
    
    def getLinkspotiv(self):
        return self.linkspotiv

    def getLinkyoutuv(self):
        return self.linkyoutuv
#set
    def setIdv(self, idv):
        self.idv = idv

    def setNombrev(self, nombrev):
        self.nombrev = nombrev
    
    def setArtistav(self, artistav):
        self.artistav = artistav
    
    def setAlbumv(self, albumv):
        self.albumv = albumv
    
    def setImagenv(self, imagenv):
        self.imagenv = imagenv
    
    def setFechav(self, fechav):
        self.fechav = fechav
    
    def setLinkspotiv(self, linkspotiv):
        self.linkspotiv = linkspotiv
    
    def setLinkyoutuv(self, linkyoutuv):
        self.linkyoutuv = linkyoutuv
    

    