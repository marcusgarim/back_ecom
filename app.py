from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash

# Configuração inicial da aplicação Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = "minha_chave_123"  # Chave secreta para segurança
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db'  # Banco de dados SQLite

# Configuração do gerenciador de login e banco de dados
login_manager = LoginManager()
db = SQLAlchemy(app)
login_manager.init_app(app)
login_manager.login_view = 'login'
CORS(app)  # Habilita CORS para permitir requisições entre domínios

# Modelagem do banco de dados
class User(db.Model, UserMixin):  # Modelo de usuário
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False, unique=True)
    password_hash = db.Column(db.String(128), nullable=False)
    cart = db.relationship('CartItem', backref='user', lazy=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Product(db.Model):  # Modelo de produto
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text, nullable=True)

class CartItem(db.Model):  # Modelo de item no carrinho
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)

# Criação das tabelas no banco de dados
with app.app_context():
    db.create_all()

# Função para carregar usuário na sessão
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Rota para registro de usuários
@app.route('/register', methods=["POST"])
def register():
    data = request.json
    if not data.get("username") or not data.get("password"):
        return jsonify({"message": "Username and password are required"}), 400
    
    if User.query.filter_by(username=data.get("username")).first():
        return jsonify({"message": "Username already exists"}), 400
    
    user = User(username=data["username"])
    user.set_password(data["password"])
    db.session.add(user)
    db.session.commit()
    return jsonify({"message": "User registered successfully"})

# Rota para login
@app.route('/login', methods=["POST"])
def login():
    data = request.json
    user = User.query.filter_by(username=data.get("username")).first()
    
    if user and user.check_password(data.get("password")):
        login_user(user)
        response = jsonify({"message": "Logged in successfully"})
        response.headers['Set-Cookie'] = 'session=active'  # Simulando o Set-Cookie
        return response
    
    return jsonify({"message": "Unauthorized. Invalid credentials"}), 401

# Adiciona um item ao carrinho
@app.route('/api/cart/add/<int:product_id>', methods=['POST'])
@login_required
def add_to_cart(product_id):
    product = Product.query.get(product_id)
    if not product:
        return jsonify({'message': 'Product not found'}), 404
    
    existing_item = CartItem.query.filter_by(user_id=current_user.id, product_id=product_id).first()
    if existing_item:
        return jsonify({'message': 'Item already in cart'}), 400
    
    cart_item = CartItem(user_id=current_user.id, product_id=product_id)
    db.session.add(cart_item)
    db.session.commit()
    return jsonify({'message': 'Item added to the cart successfully'})

# Remove um item do carrinho
@app.route('/api/cart/remove/<int:item_id>', methods=['DELETE'])
@login_required
def remove_from_cart(item_id):
    cart_item = CartItem.query.filter_by(id=item_id, user_id=current_user.id).first()
    if not cart_item:
        return jsonify({'message': 'Item not found in cart'}), 400
    
    db.session.delete(cart_item)
    db.session.commit()
    return jsonify({'message': 'Item removed from the cart successfully'})

# Busca por produtos
@app.route('/api/products/search', methods=['GET'])
def search_products():
    query = request.args.get('q', '')
    if not query:
        return jsonify({'message': 'Query parameter is required'}), 400
    
    products = Product.query.filter(Product.name.ilike(f'%{query}%')).all()
    if not products:
        return jsonify({'message': 'No products found'}), 404
    
    product_list = [{"id": p.id, "name": p.name, "price": p.price} for p in products]
    return jsonify(product_list)

# Adiciona um novo produto
@app.route('/api/products/add', methods=["POST"])
@login_required
def add_product():
    data = request.json
    if 'name' in data and 'price' in data:
        product = Product(name=data["name"], price=data["price"], description=data.get("description", ""))
        db.session.add(product)
        db.session.commit()
        return jsonify({"message": "Product added successfully"}), 201
    return jsonify({"message": "Invalid product data"}), 400

# Rota raiz apenas para teste
if __name__ == "__main__":
    app.run(debug=True)