from flask import Flask, jsonify, request
import json

app = Flask(__name__)

tarefas = [
    {
        'id'           : 0,
        'responsável'  : 'Claudio',
        'tarefa'       : ['Pintar a casa', 'Varrer o quintal'],
        'status'       : 'pendente'
    },

    {
        'id'           : 1,
        'responsável'  : 'Rafael',
        'tarefa'       : ['Lavar o carro', 'Realizar as compras do mês', 'Realizar pagamentos das contas do mês'],
        'status'       : 'concluído'
    }
]

# Mostra, altera e deleta as tarefas existentes
@app.route('/dev/<int:id>/', methods=['GET', 'PUT', 'DELETE'])
def afazer(id):
    if request.method == 'GET':
        try:
            response = tarefas[id]
        except IndexError:
            mensagem = f'Responsável pela tarefa com o ID {id} não existe.'
            response = {'Status': 'Erro', 'Mensagem' : mensagem}
        except Exception:
            mensagem = 'Erro desconhecido. Procure o Administrador da API.'
            response = {'Status': 'Erro', 'Mensagem': mensagem}
        # print(response)
        return  jsonify(response)
    elif request.method == 'PUT':
        dados = json.loads(request.data)
        tarefas[id] = dados
        return  jsonify(dados)
    elif request.method == 'DELETE':
        tarefas.pop(id)
        return jsonify({'Status':'Sucesso', 'Mensagem':'Registro Excluído!'})

# Lista todos os desenvolvedores e permite a inclusão de um novo também.
@app.route('/dev/', methods=['POST', 'GET'])
def lista_afazeres():
    if request.method == 'POST':
        dados = json.loads(request.data)
        posicao = len(tarefas)
        dados['id'] = posicao
        tarefas.append(dados)
        # mensagem = 'Registro Inserido.'
        # response = {'Status': 'Sucesso', 'Mensagem': mensagem}
        # return jsonify(response)
        return jsonify(tarefas[posicao])
    elif request.method == 'GET':
        return jsonify(tarefas)


if __name__ == '__main__':
    app.run(debug=True)