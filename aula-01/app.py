# importando o flask para a aplicação
from flask import Flask, render_template

# Carregando o flask na variável app
app = Flask(__name__, template_folder='views')

# Criando a primeira rota do site


@app.route("/")
# Criando função no python
def home():
    return render_template('index.html')


# Criando rota games
@app.route("/games")
# Criando função no python
def games():

#Dicionário em Python: Objeto em python.
    game = {
        'titulo' : 'CS-GO',
        'ano' : 2012,
        'categoria' : 'FPS ONLINE'
    }
    jogadores = ['leaf', 'quemario', 'midna', 'aspax', 'VT', 'tr0p']
    jogos = ['CS2', 'Valorant', 'League Of Legends', 'Minecraft',
             'Euro Truck Simulator 2', 'Asseto Corsa EVO']
    return render_template('games.html',
                           game=game,
                           jogadores=jogadores,
                           jogos=jogos)


# Iniciando o servidor no localhost, porta 5000, o debug ativado para checagem de erros.
if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
