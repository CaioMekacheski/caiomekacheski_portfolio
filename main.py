#Criado 23/03/2023

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/contato")
def contatos():
    return render_template("contato.html")


@app.route("/formação")
def usuario():
    return render_template("formacao.html")

@app.route("/experiência")
def experiencia():
    return render_template("experiencia.html")

@app.route("/habilidades")
def habilidades():
    return render_template("habilidades.html")

@app.route("/objetivo")
def objetivo():
    return render_template("objetivo.html")

@app.route("/game")
def game():
    return render_template("game.html")

if __name__ == "__main__":
    app.run(debug=True)
