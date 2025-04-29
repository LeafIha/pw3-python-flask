from flask import render_template, request, redirect, url_for

jogadores = ['leaf', 'quemario', 'midna', 'aspax', 'VT', 'tr0p']

# Arrays de objetos
gamelist = [
    {
        'titulo': 'CS-GO',
        'ano': 2012,
        'categoria': 'FPS ONLINE'
    }
]

consolelist = [
    {
        'nome': 'XBOX 360',
        'fabricante': 'Microsoft',
        'preco': 500
    }
]


def init_app(app):
    # Criando a primeira rota do site
    @app.route("/")
    def home():
        return render_template('index.html')

    # Criando rota games
    @app.route("/games", methods=['GET', 'POST'])
    def games():
        game = gamelist[0] if gamelist else None

        if request.method == 'POST':
            if request.form.get('jogador'):
                jogadores.append(request.form.get('jogador'))
            return redirect(url_for('games'))

        jogos = ['CS2', 'Valorant', 'League Of Legends', 'Minecraft',
                 'Euro Truck Simulator 2', 'Asseto Corsa EVO']
        return render_template('games.html',
                               game=game,
                               jogadores=jogadores,
                               jogos=jogos)

    # Rota de cadastro de jogos (em dicionário)
    @app.route('/cadgames', methods=['GET', 'POST'])
    def cadgames():
        if request.method == 'POST':
            if request.form.get('titulo') and request.form.get('ano') and request.form.get('categoria'):
                gamelist.append({
                    'titulo': request.form.get('titulo'),
                    'ano': int(request.form.get('ano')),
                    'categoria': request.form.get('categoria')
                })
            return redirect(url_for('cadgames'))
        return render_template('cadgames.html', gamelist=gamelist)

    @app.route('/consoles', methods=['GET', 'POST'])
    def consoles():
        if request.method == 'POST':
            if request.form.get('nome') and request.form.get('fabricante') and request.form.get('preco'):
                consolelist.append({
                    'nome': request.form.get('nome'),
                    'fabricante': request.form.get('fabricante'),
                    'preco': request.form.get('preco')
                })
            return redirect(url_for('consoles'))
        return render_template('consoles.html', consolelist=consolelist)
