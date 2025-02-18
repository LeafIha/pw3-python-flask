# importando o flask para a aplicação
from flask import Flask

# Carregando o flask na variável app
app = Flask(__name__)

# Criando a primeira rota do site
@app.route("/")
# Criando função no python
def home():
    return'<h1>Bem vindo ao meu primeiro site em Flask!</h1>'

# Iniciando o servidor no localhost, porta 5000, o debug ativado para checagem de erros.
if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)