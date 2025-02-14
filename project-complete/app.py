from flask import Flask

app = Flask(__name__)

@app.route('/') # Define a rota
def hello_world(): # Define uma rota raíz (página inicial) e a função que será executada
    return 'Hello, World!'

if __name__ == "__main__": # Verifica se o script está sendo executado diretamente
    app.run(debug=True)