from flask import Flask
from flask import request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///ecommerce.db" # Configura a URI do banco de dados
db = SQLAlchemy(app) # Inicializa o banco de dados

class Product(db.Model): # Define uma classe que representa uma tabela do banco de dados
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text, nullable=True)

@app.route('/api/products/add', methods=["POST"]) # Define uma rota para adicionar um produto via método POST
def add_product():
    data = request.json
    return data

@app.route('/') # Define a rota
def hello_world(): # Define uma rota raíz (página inicial) e a função que será executada
    return 'Hello, World!'

if __name__ == "__main__": # Verifica se o script está sendo executado diretamente
    app.run(debug=True) # Inicia o servidor web do Flask em modo de depuração (debug)

# CONTINUA EM 35 MINUTOS
