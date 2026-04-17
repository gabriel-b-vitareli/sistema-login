# Importando o Flask
from flask import Flask, render_template, request

app = Flask(__name__)


# Página Inicial
@app.route('/')
def home():
    return render_template('index.html')


# Sistema de Login
@app.route('/login', methods=['POST'])
def login():
    
    user = request.form.get('user')
    password = request.form.get('password')
    
    if user == "GabrielBragaVitareli" and password == "BVitareli09":
        return "Acesso Liberado."
    else:
        return "Acesso Negado."


# Inicializando o site na porta 8000 com o IP local (Localhost)
if __name__ == '__main__':
    app.run('0.0.0.0', port=8000)