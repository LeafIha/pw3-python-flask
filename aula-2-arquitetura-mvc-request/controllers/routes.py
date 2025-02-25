from flask import render_template, request
jogadores = ['leaf', 'quemario', 'midna', 'aspax', 'VT', 'tr0p']


def init_app(app):
    # Criando a primeira rota do site
    @app.route("/")
    # Criando função no python
    def home():
        return render_template('index.html')
    # Criando rota games

    @app.route("/games", methods=['GET', 'POST'])
    # Criando função no python
    def games():

        # Dicionário em Python: Objeto em python.
        game = {
            'titulo': 'CS-GO',
            'ano': 2012,
            'categoria': 'FPS ONLINE'
        }

        # Tratando se a requisição for do tipo POST
        if request.method == 'POST':
            # Verificar se o campo jogador existe
            if request.form.get('jogador'):
                jogadores.append(request.form.get('jogador'))

        jogos = ['CS2', 'Valorant', 'League Of Legends', 'Minecraft',
                 'Euro Truck Simulator 2', 'Asseto Corsa EVO']
        return render_template('games.html',
                               game=game,
                               jogadores=jogadores,
                               jogos=jogos)
