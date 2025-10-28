#GET (LISTAR) / POST (CADASTRO) / PUT (ATUALIZAR) / DELETE (DELETAR)


#importando o flask
from flask import Flask
#importando o flask restful
from flask_restful import Api
#carregando o flask na varável "app"
app = Flask(__name__)
#carregando o flask restful na varável "api"
api = Api(app)

#adicionando os recursos da api
from .resources import game_resources