from flask import Flask, jsonify, request
from flask_cors import CORS
from Administradores import Administrador
from Clientes import Cliente
from Canciones import Cancion
from Comentarios import Comentario
from Playlist import Play
from Solicitudes import Solicitud

app = Flask(__name__)
CORS(app)

Admis = []
prueba = []
Clies = []
Cans = []
Coms = []
Plays = []
Sols = []


ContCan = 0 #identificador unico de canciones, incrementara cada vez que se vaya ingresando
ContSol = 0

Admis.append(Administrador('Sharon', 'Tagual','ed','12'))

#Cans.append(Cancion('1','Cancion1', 'Artista1','Album1','Imagen1','Fecha1', 'Links1', 'Linky1'))
#Cans.append(Cancion('2','Cancion2', 'Artista2','Album2','Imagen2','Fecha2', 'Links2', 'Linky2'))
#Cans.append(Cancion('3','Cancion3', 'Artista3','Album3','Imagen3','Fecha3', 'Links3', 'Linky3'))
#=====================================Rutas para Administradores=======================================

#@app.route('/', methods=['GET'])
#def rutaInicial():
#    print("Hola k ase")
#    return("Hola alumnos")

#Obtener todos los elemento
@app.route('/Administradores', methods=['GET'])
def rutaAdmi():
    global Admis
    Datos = []
  
    for Admi in Admis:
       
        Dato = {
            'nombre': Admi.getNombre(),
            'apellido': Admi.getApellido(), 
            'usuario': Admi.getNombreusuario(),
            'contrasena': Admi.getContraseña()
            }
        Datos.append(Dato)
    respuesta = jsonify(Datos)
    return(respuesta)



#Agregar elemento
@app.route('/Administradoresa/', methods=['POST']) 
def agregarAdmia():
    global Admis

    nombreP = request.json['nombre']
    apellidoP = request.json['apellido']
    usuarioP = request.json['usuario']
    contrasenaP = request.json['password']
    encontrado = False
    for Admi in Admis:
        if Admi.getNombreusuario() == usuarioP:
             encontrado = True
             break
    if encontrado: #si encontro uno igual, encontrado es verdadero
             return jsonify({
                'usuario': Admi.getNombreusuario(),
                'menssage':'Failed',
                'reason':'El usuario ya esta registrado'
             })
    else: #si no encontro uno igual, encontrado falso
             nuevoa = Administrador(request.json['nombre'],request.json['apellido'],request.json['usuario'],request.json['password'])
             Admis.append(nuevoa)
             return jsonify({
                   'message':'Sucess',
                   'reason':'successfully registered'
             })


#Mostrar un elemento 
@app.route('/Administradores1/<string:nombre>', methods=['GET']) 
def obteneradmi(nombre):
    global Admis
    Datos = []
    for Admi in Admis:  #En admi, vas a recorrer admi   
        if Admi.getNombreusuario() == nombre: #si el los admis registrados son igual al admi mandado 
            Dato = {#vas a crear un dato
                'nombre': Admi.getNombre(),
                'apellido': Admi.getApellido(), 
                'usuario': Admi.getNombreusuario(),
                'contrasena': Admi.getContraseña()
                }
           # Datos.append(Dato)#lo vas a agregar
            break  #se rompe
    respuesta = jsonify(Dato)
    return(respuesta)

#Modificar un elemento 
@app.route('/Administradores2/<string:nombre>', methods=['PUT']) 
def Actualizaradmi(nombre):
    global Admis
    for i in range(len(Admis)): 
        if nombre==Admis[i].getNombreusuario(): #si el los admis registrados son igual al admi mandado 
            Admis[i].setNombre(request.json['nombre'])
            Admis[i].setApellido(request.json['apellido'])
            Admis[i].setNombreusuario(request.json['usuario'])
            Admis[i].setContraseña(request.json['password'])
            break  #se rompe
    return jsonify({'message':'Se actualizo con exito'})

#Eliminar un elemento 
@app.route('/Administradores3/<string:nombre>', methods=['DELETE']) 
def Eliminaradmi(nombre):
    global Admis
    for i in range(len(Admis)): 
        if nombre==Admis[i].getNombreusuario(): #si el los admis registrados son igual al admi mandado 
            del Admis[i]
            break  #se rompe
    return jsonify({'message':'Se elimino el dato con exito'})

#=====================================Rutas para Clientes=======================================

#Obtener todos los elemento
@app.route('/Clientes', methods=['GET'])
def rutaClie():
    global Clies
    Datos2 = []
    # el objeto admi va a recorrer cada posicion de mi lista(Admis)
    for Clie in Clies:
        #construyendo un objeto de tipo dato que tiene la estructura de un Json
        Dato2 = {
            'nombre': Clie.getNombre(),
            'apellido': Clie.getApellido(), 
            'usuario': Clie.getNombreusuario(),
            'contrasena': Clie.getContraseña()
            }
        Datos2.append(Dato2)#añade cada dato a los datos
    respuesta2 = jsonify(Datos2)#va a darle una estructura json a mi arreglo de datos 
    return(respuesta2)

#Agregar elemento
@app.route('/Clientes/', methods=['POST']) 
def agregarClie():
    global Clies

    nombreP = request.json['nombre']
    apellidoP = request.json['apellido']
    usuarioP = request.json['usuario']
    contrasenaP = request.json['contrasena']
    encontrado = False
    for Clie in Clies:
        if Clie.getNombreusuario() == usuarioP:
             encontrado = True
             break
    if encontrado: #si encontro uno igual, encontrado es verdadero
             return jsonify({
                'usuario': Clie.getNombreusuario(),
                'menssage':'Failed',
                'reason':'El usuario ya esta registrado'
             })
    else: #si no encontro uno igual, encontrado falso
             nuevo2 = Cliente(request.json['nombre'],request.json['apellido'],request.json['usuario'],request.json['contrasena'])
             Clies.append(nuevo2)
             return jsonify({
                   'message':'Sucess',
                   'reason':'successfully registered'
             })

#Mostrar un elemento 
@app.route('/Clientes1/<string:nombre>', methods=['GET']) 
def obtenerClie(nombre):
    global Clies
    Datos2 = []
    for Clie in Clies:  #En admi, vas a recorrer admi   
        if Clie.getNombreusuario() == nombre: #si el los admis registrados son igual al admi mandado 
            Dato2 = {#vas a crear un dato
                'nombre': Clie.getNombre(),
                'apellido': Clie.getApellido(), 
                'usuario': Clie.getNombreusuario(),
                'contrasena': Clie.getContraseña()
                }
           # Datos.append(Dato)#lo vas a agregar
            break  #se rompe
    respuesta2 = jsonify(Dato2)
    return(respuesta2)

#Modificar un elemento 
@app.route('/Clientes2/<string:nombre>', methods=['PUT']) 
def ActualizarClien(nombre):
    global Clies
    for i in range(len(Clies)): 
        if nombre==Clies[i].getNombreusuario(): #si el los admis registrados son igual al admi mandado 
            Clies[i].setNombre(request.json['nombre'])
            Clies[i].setApellido(request.json['apellido'])
            Clies[i].setNombreusuario(request.json['usuario'])
            Clies[i].setContraseña(request.json['password'])
            break  #se rompe
    return jsonify({'message':'Se actualizo con exito'})

#Eliminar un elemento 
@app.route('/Clientes3/<string:nombre>', methods=['DELETE']) 
def EliminarClie(nombre):
    global Clies
    for i in range(len(Clies)): 
        if nombre==Clies[i].getNombreusuario(): #si el los admis registrados son igual al admi mandado 
            del Clies[i]
            break  #se rompe
    return jsonify({'message':'Se elimino el dato con exito'})



#=====================================Rutas para Canciones=======================================

#Obtener todos los elemento
@app.route('/Cancionesm', methods=['GET'])
def rutaCan():
    global Cans
    Datos3 = []
    # el objeto Can va a recorrer cada posicion de mi lista(Cans)
    for Can in Cans:
        #construyendo un objeto de tipo dato que tiene la estructura de un Json
        Dato3 = {
            'Identificador': Can.getId(),
            'Nombre': Can.getNombre(),
            'Artista': Can.getArtista(),
            'Album': Can.getAlbum(),
            'Imagen': Can.getImagen(),
            'Fecha': Can.getFecha(),
            'LinkS': Can.getLinkspoti(),
            'LinkY': Can.getLinkyoutu()
            }
        Datos3.append(Dato3)#añade cada dato a los datos
    respuesta3 = jsonify(Datos3)#va a darle una estructura json a mi arreglo de datos 
    return(respuesta3)

#Agregar elemento
@app.route('/Cancionesa/', methods=['POST']) 
def agregarCan():
    global Cans, ContCan
    id = ContCan#variable que lleva el identificador de las cancionesp
    nombreC = request.json['nombre']
    artistaC = request.json['artista']
    albumC = request.json['album']
    fechaC = request.json['fecha']
    imagenC = request.json['imagen']
    linksC = request.json['spotify']
    linkyC = request.json['youtube']

    nuevo3 = Cancion(ContCan, nombreC, artistaC, albumC, imagenC, fechaC, linksC, linkyC)
    Cans.append(nuevo3)
    ContCan += 1
    return jsonify({
            'messagge':'Success',
            'reason':'Se agregó la cancion'
            })

#Mostrar un elemento 
@app.route('/Canciones1/<string:nombre>', methods=['GET']) 
def obteneCan(nombre):
    f = int(nombre)#pase la cadena de texto a tipo entero para poder ocmpararlo con el identificador
    global Cans
    Datos3 = []
    for Can in Cans:  
        if Can.getId() == f: #si el los cans registrados son igual al can mandado 
            Dato3 = {#vas a crear un dato
                 'Identificador': Can.getId(),
                 'Nombre': Can.getNombre(),
                 'Artista': Can.getArtista(),
                 'Album': Can.getAlbum(),
                 'Imagen': Can.getImagen(),
                 'Fecha': Can.getFecha(),
                 'LinkS': Can.getLinkspoti(),
                 'LinkY': Can.getLinkyoutu()
                 }
           # Datos.append(Dato)#lo vas a agregar
            break  #se rompe
    respuesta3 = jsonify(Dato3)
    return(respuesta3)

#Modificar un elemento 
@app.route('/Canciones/<string:nombre>', methods=['PUT']) 
def ActualizarCan(nombre):
    f2 = int(nombre)
    global Cans
    for i in range(len(Cans)): 
        if f2==Cans[i].getId(): #si una cancion registrada es igual a la cancion que se pide
            Cans[i].setNombre(request.json['identificador'])
            Cans[i].setNombre(request.json['nombre'])
            Cans[i].setArtista(request.json['artista'])
            Cans[i].setAlbum(request.json['album'])
            Cans[i].setImagen(request.json['imagen'])
            Cans[i].setFecha(request.json['fecha'])
            Cans[i].setLinkspoti(request.json['links'])
            Cans[i].setLinkyoutu(request.json['linky'])
            break  #se rompe
    return jsonify({'message':'Se actualizo con exito'})

#Eliminar un elemento 
@app.route('/Canciones/<string:nombre>', methods=['DELETE']) 
def EliminarCan(nombre):
    f3 = int(nombre)
    global Cans
    for i in range(len(Cans)): 
        if f3==Cans[i].getId(): #si el los admis registrados son igual al admi mandado 
            del Cans[i]
            break  #se rompe
    return jsonify({'message':'Se elimino el dato con exito'})


#=====================================LOGIN=======================================
    
@app.route('/Login2/', methods=['POST']) 
def Login2():
    global Clies
    global Admis

    usuarioL = request.json['usuario']
    contasenaL = request.json['password']
    
    confirma=False
    #if confirma==False:
    if confirma==False:
        for Clie in Clies:
            if Clie.getNombreusuario() == usuarioL and Clie.getContraseña() == contasenaL:  
                DatoL = {
                    'message':'Success1',
                    'usuario': Clie.getNombreusuario()
                    }
                confirma=True
                break
            else:
                DatoL = {
                   'message':'Failed',
                   'usuario': ''
                   }
    #elif confirma==False:
    if confirma==False:#no funciona con elif por que si el primero se ejecuta, no lo valua, y entonces se va con qeu las credenciales no son correctas
        for Admi in Admis:
            if Admi.getNombreusuario() == usuarioL and Admi.getContraseña() == contasenaL:       
                DatoL = {
                    'message':'Success2',
                    'usuario': Admi.getNombreusuario()
                    }
                confirma=True
                break
            else:
                DatoL = {
                   'message':'Failed',
                   'usuario': ''
                    }
    respuesta = jsonify(DatoL)
    return(respuesta)        

#Recuperar contraseña
@app.route('/Recuperar/', methods=['POST']) 
def RecuperarContraCliente():
    global Clies

    usuarioP = request.json['usuario']
    
    encontrado = False
    for Clie in Clies:
        if Clie.getNombreusuario() == usuarioP:
             encontrado = True
             break
    if encontrado: #si encontro uno igual, encontrado es verdadero
             return jsonify({
                'usuario': Clie.getNombreusuario(),
                'password': Clie.getContraseña(),
                'pip':'True',
                'reason':'Se encontro el usuario'
             })
    else: #si no encontro uno igual, encontrado falso
             
             return jsonify({
                   'usuario': "",
                   'password': "f",
                   'message':'False',
                   'reason':'No se encontro el usuario'
             })
#=====================================Comentarios======================================


#Obtener todos los elemento
@app.route('/Comentarios', methods=['GET'])
def rutaComen():
    global Coms
    Datos4 = []
    for Com in Coms:
        Dato4 = {
            'nombre': Com.getNombre(),
            'id': Com.getId(),
            'persona': Com.getPersona()
            }
        Datos4.append(Dato4)#añade cada dato a los datos
    respuesta = jsonify(Datos4)#va a darle una estructura json a mi arreglo de datos 
    return(respuesta)


#Agregar elemento
@app.route('/Comentariosa/', methods=['POST']) 
def agregarComen():
    global Coms
    nombreP = request.json['nombre']
    identifi = request.json['id']
    person = request.json['persona']
    nuevoc = Comentario(nombreP, identifi, person)
    Coms.append(nuevoc)
    return jsonify({
                'message':'Sucess',
                'reason':'successfully registered'
                })


#Mostrar elementos restringidos
@app.route('/Comentariosm/<string:iden>', methods=['GET']) 
def obtenerComen(iden):
    global Coms
    Datos4 = []
    for Com in Coms:  
        if Com.getId()  == iden:  
            Dato4 = { 
                'nombre': Com.getNombre(),
                'id': Com.getId(),
                'persona': Com.getPersona()
                }
            Datos4.append(Dato4)
    respuesta4 = jsonify(Datos4)
    return(respuesta4)

#=====================================PlayList======================================


#Obtener todos los elemento
@app.route('/Play', methods=['GET'])
def rutaPlay():
    global Plays
    Datos5 = []
    for Pla in Plays:
        Dato5 = {
            'link': Pla.getLink(),
            'id': Pla.getId(),
            'persona': Pla.getPersona(),
            'imagen': Pla.getImagen()
            }
        Datos5.append(Dato5)#añade cada dato a los datos
    respuesta = jsonify(Datos5)#va a darle una estructura json a mi arreglo de datos 
    return(respuesta)


#Agregar elemento
@app.route('/Playa/', methods=['POST']) 
def agregarPlay():
    global Plays
    link = request.json['link']
    identifi = request.json['id']
    person = request.json['persona']
    ima = request.json['imagen']
    nuevop = Play(link, identifi, person, ima)
    Plays.append(nuevop)
    return jsonify({
                'message':'Sucess',
                'reason':'successfully registered'
                })

#Mostrar elementos restringidos
@app.route('/Playm/<string:iden>', methods=['GET']) 
def obtenerPlay(iden):
    global Plays
    Datos5 = []
    for Pla in Plays:  
        if Pla.getPersona()  == iden:  
            Dato5 = { 
                'link':Pla.getLink(),
                'id': Pla.getId(),
                'persona': Pla.getPersona(),
                'imagen': Pla.getImagen()
                }
            Datos5.append(Dato5)
    respuesta5 = jsonify(Datos5)
    return(respuesta5)
#==========================================Solicitues=================================================
#Obtener todos los elemento
@app.route('/Solicitues', methods=['GET'])
def rutaSol():
    global Sols
    Datos6 = []
    # el objeto Can va a recorrer cada posicion de mi lista(Cans)
    for Sol in Sols:
        #construyendo un objeto de tipo dato que tiene la estructura de un Json
        Dato6 = {
            'Identificador': Sol.getIdv(),
            'Nombre': Sol.getNombrev(),
            'Artista': Sol.getArtistav(),
            'Album': Sol.getAlbumv(),
            'Imagen': Sol.getImagenv(),
            'Fecha': Sol.getFechav(),
            'LinkS': Sol.getLinkspotiv(),
            'LinkY': Sol.getLinkyoutuv()
            }
        Datos6.append(Dato6)#añade cada dato a los datos
    respuesta6 = jsonify(Datos6)#va a darle una estructura json a mi arreglo de datos 
    return(respuesta6)

#Agregar elemento
@app.route('/Solicitudesa/', methods=['POST']) 
def agregarSol():
    global Sols, ContSol
    id = ContSol#variable que lleva el identificador de las cancionesp
    nombrev = request.json['nombre']
    artistav = request.json['artista']
    albumv = request.json['album']
    fechav = request.json['fecha']
    imagenv = request.json['imagen']
    linksv = request.json['spotify']
    linkyv = request.json['youtube']

    nuevo6 = Solicitud(ContSol, nombrev, artistav, albumv, imagenv, fechav, linksv, linkyv)
    Sols.append(nuevo6)
    ContSol += 1
    return jsonify({
            'messagge':'Success',
            'reason':'Se agregó la Solicitud'
            })


#Mostrar un elemento 
@app.route('/Solicitues1/<string:nombre>', methods=['GET']) 
def obtenerSol(nombre):
    f = int(nombre)#pase la cadena de texto a tipo entero para poder ocmpararlo con el identificador
    global Sols
    Datos6 = []
    for Sol in Sols:  
        if Sol.getIdv() == f: #si el los cans registrados son igual al can mandado 
            Dato6 = {
                 'Identificador': Sol.getIdv(),
                 'Nombre': Sol.getNombrev(),
                 'Artista': Sol.getArtistav(),
                 'Album': Sol.getAlbumv(),
                 'Imagen': Sol.getImagenv(),
                 'Fecha': Sol.getFechav(),
                 'LinkS': Sol.getLinkspotiv(),
                 'LinkY': Sol.getLinkyoutuv()
                 }
           # Datos.append(Dato)#lo vas a agregar
            break  #se rompe
    respuesta6 = jsonify(Dato6)
    return(respuesta6)


#Eliminar un elemento 
@app.route('/Solicitudese/<string:nombre>', methods=['DELETE']) 
def EliminarSol(nombre):
    f6 = int(nombre)
    global Sols
    for i in range(len(Sols)): 
        if f6==Sols[i].getIdv(): #si el los admis registrados son igual al admi mandado 
            del Sols[i]
            break  #se rompe
    return jsonify({'message':'Se elimino el dato con exito'})


#DE ultimo
if __name__ == "__main__":
    app.run(port=5000, debug=True)




