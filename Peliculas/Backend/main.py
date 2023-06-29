from flask import Flask, request
from flask_cors import CORS

from Clases.Usuario import Usuario
from Clases.Comentario import Comentario
from Metodos.Inicial import *
from Metodos.Usuario import *
from Metodos.Administrador import *

usuarios = []
usuarioEnSesion = -1
peliculas = []
comentarios = [] 

# tipo 1 para administrador
usuarios.append(Usuario('Usuario', 'Administrador', 'admin', 'admin1', 1).toDict())

# tipo 2 para clientes
usuarios.append(Usuario('moi   ', 'vasquez', 'moi', '1234a', 2).toDict())

# comentarios ejemplo
comentarios.append(Comentario('Super Mario Bros', 'juanito', 'bonitos recuerdos').toDict())
comentarios.append(Comentario('Super Mario Bros', 'mario', 'me recuerda a mi infancia').toDict())
comentarios.append(Comentario('Los Vengadores', 'elmer', 'Muy buena').toDict())
comentarios.append(Comentario('Los Vengadores', 'estefani', 'esta fea').toDict())

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def rutaInicial():
    return("Si funciona")

# ------------------------------------------------------------- INICIAL
@app.route('/registrarUsuario', methods=['POST'])
def registrarUsuario():
    respuesta = RegistrarUsuario(request.json, usuarios)
    return respuesta

@app.route('/recuperarContrasenia', methods=['POST'])
def recuperarContrasenia():
    respuesta = RecuperarContrasenia(request.json, usuarios)
    return respuesta

@app.route('/iniciarSesion', methods=['POST'])
def iniciarSesion():
    respuesta = IniciarSesion(request.json, usuarios)
    global usuarioEnSesion
    
    usuarioEnSesion = respuesta['usuarioEnSesion']
    print(usuarioEnSesion)
    return respuesta
    
# ------------------------------------------------------------- USUARIOS
@app.route('/getUsuarioEnSesion', methods=['GET'])
def getUsuarioEnSesion():
    respuesta = GetUsuarioEnSesion(usuarios, usuarioEnSesion)
    return respuesta

@app.route('/modificarPerfil', methods=['POST'])
def modificarPerfil():
    global usuarios
    respuesta = ModificarPerfil(request.json, usuarios, usuarioEnSesion)
    usuarios = respuesta['data']
    return {'data':'OK', 'status': respuesta['status']}

@app.route('/modificarCliente', methods=['POST'])
def modificarCliente():
    global usuarios
    respuesta = ModificarCliente(request.json, usuarios, usuarioEnSesion)
    usuarios = respuesta['data']
    return {'data':'OK', 'status': respuesta['status']}
# ------------------------------------------------------------- ADMINISTRADOR
@app.route('/cargarPeliculas', methods=['POST'])
def cargarPeliculas():
    respuesta = CargarPeliculas(request.json)
    global peliculas
    peliculas = respuesta['data']
    return respuesta

@app.route('/getPeliculas', methods=['GET'])
def getPeliculas():
    respuesta = {'data': peliculas, 'status': 200}
    return respuesta

@app.route('/getPelicula', methods=['POST'])
def getPelicula():
    respuesta = GetPelicula(request.json, peliculas)
    return respuesta

@app.route('/editarPelicula', methods=['POST'])
def editarPelicula():
    global peliculas
    respuesta = EditarPelicula(request.json, peliculas)
    peliculas = respuesta['data']
    return {'data':'OK', 'status': respuesta['status']}

@app.route('/eliminarPelicula', methods=['POST'])
def eliminarPelicula():
    global peliculas
    respuesta = EliminarPelicula(request.json, peliculas)
    peliculas = respuesta['data']
    return {'data':'OK', 'status': respuesta['status']}

@app.route('/getComentarios', methods=['POST'])
def getComentarios():
    respuesta = GetComentarios(request.json, comentarios)
    return respuesta

@app.route('/getUsuarios', methods=['GET'])
def getUsuarios():
    respuesta = {'data': usuarios, 'status': 200}
    return respuesta

@app.route('/eliminarUsuario', methods=['POST'])
def eliminarUsuario():
    global usuarios
    respuesta = EliminarUsuario(request.json, usuarios)
    usuarios = respuesta['data']
    return {'data':'OK', 'status': respuesta['status']}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)
