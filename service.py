from flask import Flask, jsonify, request, make_response, render_template
import mysql.connector


import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='impacta',
    database='bdimpacra',
)

cursor = conexao.cursor()





class users:
    def __init__(self, email, nome, curso):
        self.email = email
        self.nome = nome
        self.curso= curso


user1 = users('@gmail', 'Fabricio', 'ads')
lista = [user1]

gmail = ""
nome = ""



app = Flask(__name__)

@app.route('/')
def index():
    return render_template('cadastro.html', titulo='Lista de alunos cadastrados', users=lista)

@app.route('/', methods=['POST',])
def criar():
    email = request.form['email']
    nome = request.form['nome']
    curso = request.form['curso']
    user = users(email, nome, curso)
    lista.append(user)
    comando = f'INSERT INTO projeto (email, usuario, curso) VALUES ("{email}", "{nome}", "{curso}")'

    return render_template('cadastro.html', titulo='Lista de alunos cadastrados', users=lista)





app.run(port=5000,host='localhost', debug = True )


