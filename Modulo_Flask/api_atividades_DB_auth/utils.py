from flaskext.auth import login
from model import Pessoas, Usuarios

def insere_pessoa():
    pessoa = Pessoas(nome='Maria', idade=35)
    print(pessoa)
    pessoa.save()

def insere_usuario():
    usuario = Usuarios(login='Raul', senha='123', ativo="ativo")
    print(f"Usuario {usuario.login} conectando no sistema!")
    usuario.save()

def consulta_pessoas():
    pessoas = Pessoas.query.all()  # Pessoas.query.filter_by(nome='Claudio')
    print(pessoas)

def consulta_usuarios():
    usuarios = Usuarios.query.all()  # Usuarios.query.filter_by(login='Caio')
    print(usuarios)

def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome='João').first()
    pessoa.idade = 30
    pessoa.save()

def altera_usuario():
    usuario = Usuarios.query.filter_by(login='Maria').first()
    usuario.senha = '321'
    usuario.ativado = 'desativado'
    usuario.save()

def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Maria').first()
    pessoa.delete()

def exclui_usuario():
    usuario = Usuarios.query.filter_by(login='Caio').first()
    usuario.delete()

if __name__ == '__main__':
    #insere_pessoa()
    #insere_usuario()
    print("Usuaria Maria será desativada")
    altera_usuario()
    print("Consulta Pessoas")
    consulta_pessoas()
    print("Todos os usuários cadastrados")
    consulta_usuarios()


    #insere_usuario()
    #consulta_pessoas()
    #altera_pessoa()
    #print("Consulta e informa primeiro")
    #consulta_pessoas()
    #print("exclui Pessoa : Caio")
    #exclui_pessoa()
    #print(" Consulta Pessoas")
    #consulta_pessoas()
    #print(" Todos os usuários cadastrados")
    #consulta_usuarios()