from flask import Flask,render_template,redirect,request
from intentocony import Usuario

app = Flask(__name__)

@app.route('/')
def index():
    usuarios = Usuario.get_all()

    return render_template("usuario_tabla.html", usuarios = usuarios)

@app.route('/usuarios')
def usuarios():
    todos_usuarios = Usuario.get_all()

    return render_template("usuario_tabla.html", usuarios = todos_usuarios)

@app.route('/usuarios/nuevo')
def nuevo():
    return render_template("usuario_nuevo.html")


@app.route('/usuarios/nuevo/procesar',methods=['POST'])
def crear():
    datos = {
        "nombre":request.form['nombre'],
        "apellido": request.form['apellido'],
        "email": request.form['email']
    }
    Usuario.save(datos)
    return redirect('/usuarios')

@app.route('/usuarios/<int:id>')
def perfil(id):
    usuario_id ={"id": id}
    usuario = Usuario.get_one(usuario_id)

    return render_template("perfil_usuario.html", usuario = usuario)

@app.route("/usuarios/borrar/<int:id>")
def borrar(id):
     usuario_id ={"id": id}
     Usuario.delete(usuario_id)
     return redirect('/usuarios')

@app.route("/usuarios/actualizar/<int:id>")
def actualizar(id):
     usuario_id ={"id": id}
     usuario = Usuario.get_one(usuario_id)

     return render_template("usuario_editar.html",usuario = usuario )

@app.route("/usuarios/actualizar/procesar",methods=['POST'])
def procesar_actualizar():
    datos = {
        "id": request.form['id'],
        "nombre":request.form['nombre'],
        "apellido": request.form['apellido'],
        "email": request.form['email']
    }
    Usuario.update(datos)
    return redirect('/usuarios')

if __name__=="__main__":   

   app.run(debug=True)