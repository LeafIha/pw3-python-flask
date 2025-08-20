from flask import Flask, render_template
from controllers import routes

# Carregando o Flask na variável app
app = Flask(__name__, template_folder='views')

routes.init_app(app)

@app.route('/')
def main():
    return render_template('index.html')

if __name__ == '__main__':
    # Iniciando o servidor no localhost na porta 5000, modo de depuração ativado
    app.run(host='0.0.0.0', port=5000, debug=True)