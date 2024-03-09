import json

from flask import request
from flask_restful import Resource


lista_de_habilidades = ['Python', 'Flask', 'Django', 'PHP', 'Java', 'Spring']
class Habilidades(Resource):
    def get(self):
        return  lista_de_habilidades

    def post(self):
        dados = json.loads(request.data)
        posicao = len(lista_de_habilidades)
        lista_de_habilidades.extend(dados)
        return lista_de_habilidades[posicao]


class Habilidade(Resource):

    def put(self, id):
        dados = json.loads(request.data)
        lista_de_habilidades[id] = dados
        return dados

    def delete(self, id):
        lista_de_habilidades.pop(id)
        return {'Status': 'Sucesso', 'Mensagem': 'Registro Excluído!'}



