from flask import Flask, request
from flask_restful import Resource, Api, abort
from model import Pessoas, Atividades, Usuarios
from flask_httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()
app = Flask(__name__)
api = Api(app)


@auth.verify_password
def verificacao(login, senha):
    if not (login and senha):
        print("Nome ou senha não fornecida")
        return False

    
    usuario = Usuarios.query.filter_by(login=login).first()
    if not usuario:
        print("Usuário não encontrado")
        return False

    if usuario.senha != senha:
        print("Senha incorreta")
        return False

    if usuario.ativo != 'ativo':
        
        abort(403, description=f"Usuário {login} não está ativo. Status atual: {usuario.ativo}")

    return True


class Pessoa(Resource):
    @auth.login_required
    def get(self, nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        try:
            response = {
                'nome': pessoa.nome,
                'idade': pessoa.idade,
                'id': pessoa.id
            }
        except AttributeError:
            response = {
                'Status' : 'Error',
                'Mensagem ': 'Pessoa não encontrada'
            }
        return response

    @auth.login_required
    def put(self, nome):
        pessoa = Pessoas.query.filter_by(nome = nome).first()
        dados  = request.json
        if 'nome' in dados:
            pessoa.nome = dados['nome']
        if 'idade' in dados:
            pessoa.idade = dados['idade']
        pessoa.save()

        response = {
            'id': pessoa.id,
            'nome': pessoa.nome,
            'idade': pessoa.idade
        }

        return response

    @auth.login_required
    def delete(self, nome):
        pessoa = Pessoas.query.filter_by(nome = nome).first
        mensagem = 'Pessoa {} excluída com sucesso! '.format(pessoa.nome)
        pessoa.delete()

        return {'Status':'Sucesso', 'Mensagem': mensagem }

class ListaPessoas(Resource):

    @auth.login_required
    def get(self):
        pessoas = Pessoas.query.all()
        response = [{'id': i.id, 'nome': i.nome, 'idade': i.idade} for i in pessoas]
        return response

    @auth.login_required
    def post(self):
        dados = request.json
        pessoa = Pessoas(nome=dados['nome'], idade=dados['idade'])
        pessoa.save()

        response = {
            'id': pessoa.id,
            'nome': pessoa.nome,
            'idade': pessoa.idade
        }
        return response

class ListaAtividades(Resource):

    @auth.login_required
    def get(self):
        atividades = Atividades.query.all()
        response  = [ {'id': i.id, 'nome':i.nome, 'pessoa': i.pessoa.nome} for i in atividades]
        return response

    @auth.login_required
    def post(self):
        dados = request.json
        pessoa = Pessoas.query.filter_by(nome = dados['pessoa']).first()
        atividade = Atividades(nome = dados['nome'], pessoa = pessoa)
        atividade.save()

        response = {
            'pessoa' : atividade.pessoa.nome,
            'nome'   : atividade.nome,
            'id'     : atividade.id
        }

        return response

api.add_resource(Pessoa, '/pessoa/<string:nome>/')
api.add_resource(ListaPessoas, '/pessoa/')
api.add_resource(ListaAtividades, '/atividades/')

if __name__ == '__main__':
    app.run(debug=True)
