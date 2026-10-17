from werkzeug.security import generate_password_hash, check_password_hash
from flask import Flask,render_template,redirect, session, url_for,request,flash
from consultas import consulta, insertar
from decoradores import login_requerido





app = Flask(__name__)


app.secret_key = generate_password_hash("12345")



@app.route("/inicio",)
def inicio():
    return render_template("index.html")
    
@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        usuario = request.form.get("user")
        contraseña_usuario = request.form.get("password")
        query = "SELECT user, contraseña FROM usuarios WHERE user = %s"
        parametros = (usuario,)
        respuesta = consulta(query, parametros)
        if respuesta:
            contraseña_segura = respuesta[0]['contraseña']
            print("mi contraseña segura: ", contraseña_segura)
            if check_password_hash(contraseña_segura, contraseña_usuario):
                flash("contraseña correcta", "exitoso")
                return redirect(url_for('inicio'))
            else:
                flash("contraseña incorrecta", "error")
                return redirect(url_for('login'))
        else:
            flash("usuario no se encuentra registrado", "error")
            session['user'] = usuario
            return redirect(url_for('login'))
    else:
        return render_template("login.html")

app.run(debug=True)