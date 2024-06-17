from model import Pessoas


def insere_pessoas():
    pessoa = Pessoas(nome='Joana', idade=25)
    print(pessoa)
    pessoa.save()

def consulta_pessoas():
    pessoas = Pessoas.query.all() #Pessoas.query.filter_by(nome='Claudio')
    print(pessoas)

    # pessoa = Pessoas.query.filter_by(nome='Claudio').first()
    # print(pessoa.idade)
    # for alguem in pessoa:
    #     print(alguem)
    #print(pessoa)
def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome='João').first()
    pessoa.idade = 40
    pessoa.save()

def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Marcio').first()
    pessoa.delete()

if __name__ == '__main__':
    #insere_pessoas()
    #consulta_pessoas()
    #altera_pessoa()
    #print("exclui Pessoa : Claudio")
    #exclui_pessoa()
    print(" Consulta Pessoas")
    consulta_pessoas()