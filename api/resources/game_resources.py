#importando a classe Resource do flask_restful
from flask_restful import Resource

#importando a classe API
from api import api

#Logo abaixo irá as respostas da api
class Gamelist(Resource):
    def get(self):
        return "Bem vindo a API de games"


#Criando endpoint
api.add_resource(Gamelist, "/games")