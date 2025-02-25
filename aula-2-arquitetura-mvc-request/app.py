# importando o flask para a aplicação
from flask import Flask, render_template

#importando as rotas que estão no controller
from controllers import routes

# Carregando o flask na variável app
app = Flask(__name__, template_folder='views')

#chamando as rotas
routes.init_app(app)

# Iniciando o servidor no localhost, porta 5000, o debug ativado para checagem de erros.
if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
