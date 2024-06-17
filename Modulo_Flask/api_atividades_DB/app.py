from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from model import Pessoas, Atividades

app = Flask(__name__)
api = Api(app)


class Pessoa(Resource):
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
                'Status': 'Error',
                'Mensagem ': 'Pessoa não encontrada'
            }
        return response

    def put(self, nome):
        try:
            pessoa = Pessoas.query.filter_by(nome=nome).first()
            dados = request.json
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
        except AttributeError:
            response = {
                'Status': 'Error',
                'Mensagem ': 'Pessoa não encontrada'
            }
        return response

    def delete(self, nome):
        try:
            pessoa = Pessoas.query.filter_by(nome=nome).first()
            dados = request.json
            if 'nome' in dados:
                pessoa.nome = dados['nome']
            if 'idade' in dados:
                pessoa.idade = dados['idade']
            mensagem = 'Pessoa {} excluída com sucesso! '.format(pessoa.nome)
            pessoa.delete()
            response = {'Status': 'Sucesso', 'Mensagem': mensagem}
        except AttributeError:
            response = {
                'Status': 'Error',
                'Mensagem ': 'Pessoa não encontrada'
            }
        return response


class ListaPessoas(Resource):
    def get(self):
        try:
            pessoas = Pessoas.query.all()
            response = [{'id': i.id, 'nome': i.nome, 'idade': i.idade} for i in pessoas]
        except AttributeError:
            response = {
                'Status': 'Error',
                'Mensagem ': 'Pessoa não encontrada'
            }
        return response

    def post(self):
        try:
            dados = request.json
            pessoa = Pessoas(nome=dados['nome'], idade=dados['idade'])
            pessoa.save()
            response = {
                'id': pessoa.id,
                'nome': pessoa.nome,
                'idade': pessoa.idade
            }
        except AttributeError:
            response = {
                'Status': 'Error',
                'Mensagem ': 'Pessoa não encontrada'
            }

        return response


class ListaAtividades(Resource):
    def get(self):
        atividades = Atividades.query.all()
        response = [{'id': i.id, 'nome': i.nome, 'pessoa': i.pessoa.nome, 'status': i.status} for i in atividades]
        return response

    def post(self):
        try:
            dados = request.json
            pessoa = Pessoas.query.filter_by(nome=dados['pessoa']).first()
            if not pessoa:
                return {'Status': 'Error', 'Mensagem': 'Pessoa não encontrada'}, 404

            if 'status' not in dados or dados['status'] not in ["concluido", "pendente"]:
                return {'Status': 'Error', 'Mensagem': 'Status inválido ou ausente'}, 400

            atividade = Atividades(nome=dados['nome'], pessoa=pessoa, status=dados['status'])
            atividade.save()

            response = {
                'pessoa': atividade.pessoa.nome,
                'nome': atividade.nome,
                'status': atividade.status,
                'id': atividade.id
            }
        except Exception as e:
            response = {
                'Status': 'Error',
                'Mensagem': 'Erro ao inserir atividade',
                'Detalhes': str(e)
            }
        return response


class Status_Atual(Resource):
    def get(self, id):
        atividade = Atividades.query.filter_by(id=id).first()
        try:
            response = {
                'id': atividade.id,
                'status': atividade.status
            }
        except AttributeError:
            response = {
                'Status': 'Error',
                'Mensagem ': 'Atividade não encontrada'
            }
        return response

    def post(self, id):
        try:
            atividade = Atividades.query.filter_by(id=id).first()
            if not atividade:
                return {'Status': 'Error', 'Mensagem': 'Atividade não encontrada'}, 404

            # Get the request data
            dados = request.json
            if 'status' in dados:
                if dados['status'] in ["concluido", "pendente"]:
                    atividade.status = dados['status']
                else:
                    return {'Status': 'Error', 'Mensagem': 'Status inválido'}, 400

            atividade.save()

            response = {
                'id': atividade.id,
                'status': atividade.status
            }
        except Exception as e:
            response = {
                'Status': 'Error',
                'Mensagem': 'Erro ao atualizar atividade',
                'Detalhes': str(e)
            }
        return response


class ListaPessoaAtividades(Resource):
    def get(self, nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        if not pessoa:
            return {
                'Status': 'Error',
                'Mensagem': 'Pessoa não encontrada'
            }, 404

        atividades = Atividades.query.filter_by(pessoa_id=pessoa.id).all()

        response = []
        for atividade in atividades:
            response.append({
                'id': atividade.id,
                'nome': atividade.nome,
                'status': atividade.status
            })

        return response
    


api.add_resource(Pessoa, '/pessoa/<string:nome>/')
api.add_resource(ListaPessoas, '/pessoa/')
api.add_resource(ListaAtividades, '/atividades/')
api.add_resource(Status_Atual, '/status/<int:id>/')
api.add_resource(ListaPessoaAtividades, '/atividades/<string:nome>/')

if __name__ == '__main__':
    app.run(debug=True)
