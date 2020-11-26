#coding: utf-8
from flask import Flask
from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
def login():
    return render_template("login.html"), 200
     
@app.route("/menu/")
def Menu():
    return render_template("Menu.html"), 200
     
@app.route("/CadastroFuncionários/")
def funcionarios():
    return render_template("Formulário Funcionários.html"), 200

@app.route("/Comandas/")
def comandas():
    return render_template("Comandas.html"), 200
    
@app.route("/Produto/")
def Produto():
    return render_template("Form Produto.html"), 200

@app.route("/CriarComandas/")
def CriarComandas():
    return render_template("Criar comandas.html"), 200
    
@app.route("/vizualizaracomanda/")
def VerComandas():
    return render_template("Vizualizar comandas.html"), 200



if __name__ == "__main__":
    app.run()