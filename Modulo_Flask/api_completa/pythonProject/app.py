from flask import Flask, jsonify, request
import json

app = Flask(__name__)

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

# Mostra, altera e deleta os desenvolvedores existentes
@app.route('/dev/<int:id>/', methods=['GET', 'PUT', 'DELETE'])
def desenvolvedor(id):
    if request.method == 'GET':
        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagem = f'Desenvolvedor de ID {id} não existe.'
            response = {'Status': 'Erro', 'Mensagem' : mensagem}
        except Exception:
            mensagem = 'Erro dessssconhecido. Procure o Administrador da API.'
            response = {'Status': 'Erro', 'Mensagem': mensagem}
        # print(response)
        return  jsonify(response)
    elif request.method == 'PUT':
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return  jsonify(dados)
    elif request.method == 'DELETE':
        desenvolvedores.pop(id)
        return jsonify({'Status':'Sucesso', 'Mensagem':'Registro Excluído!'})

# Lista todos os desenvolvedores e permite a inclusão de um novo também.
@app.route('/dev/', methods=['POST', 'GET'])
def lista_desenvolvedores():
    if request.method == 'POST':
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        # mensagem = 'Registro Inserido.'
        # response = {'Status': 'Sucesso', 'Mensagem': mensagem}
        # return jsonify(response)
        return jsonify(desenvolvedores[posicao])
    elif request.method == 'GET':
        return jsonify(desenvolvedores)


if __name__ == '__main__':
    app.run(debug=True)