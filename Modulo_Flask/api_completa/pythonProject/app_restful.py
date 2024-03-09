from flask import Flask, request
from flask_restful import Resource, Api
import json

from habilidades import Habilidades, Habilidade

desenvolvedores = [
    {
        'id': 0,
        'Nome' : 'Claudio',
        'Habilidades' : ['Python', 'Flask']
    },

    {
        'id' : 1,
        'Nome' : 'Rafael',
        'Habilidades' : ['Python', 'Django']}
]

app = Flask(__name__)
api = Api(app)

class Desenvolvedor(Resource):
    # Mostra (get), altera (put) e deleta (delete) os desenvolvedores existentes
    def get(self, id):
        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagem = f'Desenvolvedor de ID {id} não existe.'
            response = {'Status': 'Erro', 'Mensagem': mensagem}
        except Exception:
            mensagem = 'Erro dessssconhecido. Procure o Administrador da API.'
            response = {'Status': 'Erro', 'Mensagem': mensagem}
        # print(response)
        return response

    def put(self, id):
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return dados

    def delete(self, id):
        desenvolvedores.pop(id)
        return {'Status': 'Sucesso', 'Mensagem': 'Registro Excluído!'}


# Lista todos os desenvolvedores e permite a inclusão de um novo também.
class Lista_Desenvolvedores(Resource):
    def get(self):
        return desenvolvedores
    def post(self):
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.extend(dados)
        return desenvolvedores[posicao]

api.add_resource(Desenvolvedor, '/dev/<int:id>')
api.add_resource(Lista_Desenvolvedores, '/dev/')
api.add_resource(Habilidades, '/habilidades')
api.add_resource(Habilidade, '/habilidades/<int:id>')
if __name__ == '__main__':
    app.run(debug=True)