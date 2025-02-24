from flask import Flask, request, jsonify 
from flask_sqlalchemy import SQLAlchemy  

app = Flask(__name__)  
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///ecommerce.db"  
db = SQLAlchemy(app)  

# Definição do modelo de produto
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)  
    name = db.Column(db.String(120), nullable=False)  
    price = db.Column(db.Float, nullable=False)  
    description = db.Column(db.Text, nullable=True)  

# Cria as tabelas no banco de dados se ainda não existirem
with app.app_context():
    db.create_all()

@app.route('/api/products/add', methods=["POST"])
def add_product():
    data = request.json  # Obtém os dados do JSON enviado na requisição
    
    # Verifica se os campos necessários foram fornecidos
    if 'name' in data and 'price' in data:
        try:
            price = float(data["price"])  # Converte o preço para número (float)
        except ValueError:
            return jsonify({"message": "Preço inválido"}), 400

        product = Product(name=data["name"], price=price, description=data.get("description", ""))
        db.session.add(product)  # Adiciona o produto ao banco de dados
        db.session.commit()  # Confirma a transação no banco
        
        return jsonify({"message": "Produto adicionado com sucesso"})  # Retorna mensagem de sucesso
    
    return jsonify({"message": "Dados do produto inválidos"}), 400  # Retorna erro caso os dados sejam inválidos

# Teste
@app.route('/')
def hello_world():
    return 'Hello, World!'

# Executa a aplicação no modo debug
if __name__ == "__main__":
    app.run(debug=True) 
