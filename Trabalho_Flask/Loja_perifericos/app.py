from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
produtos_mouse = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cadastro_dict1', methods=['GET', 'POST'])
def cadastro_dict1():
    if request.method == 'POST':
        novo_produto = {
            'nome': request.form.get('nome'),
            'preco': request.form.get('preco'),
            'categoria': request.form.get('categoria'),
            'fabricante': request.form.get('fabricante'),
             'imagem':'https://i.pinimg.com/736x/d4/cc/f9/d4ccf9695b9fae52de2d4405c25647be.jpg '
        }
        produtos_mouse.append(novo_produto)
        return redirect(url_for('produtos'))
    return render_template('cadastro_dict1.html')

@app.route('/produtos')
def produtos():
    return render_template('produtos.html', produtos=produtos_mouse)

# Rotas para outras páginas
@app.route('/teclado')
def teclado():
    return render_template('teclado.html')

@app.route('/headsets')
def headsets():
    return render_template('head.html')

@app.route('/mousepads')
def mousepads():
    return render_template('pad.html')

@app.route('/mouse')
def mouse():
    return render_template('mouse.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)