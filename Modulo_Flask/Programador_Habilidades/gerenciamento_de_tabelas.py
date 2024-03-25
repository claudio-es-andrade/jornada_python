from programador import Programadores
from habilidade import Habilidades
from programador_habilidade import Programadores_Habilidades


def insere_programadores():
    print("Insere o nome do Programador \n")
    programador_Alberto = Programadores(nome='Alberto', idade=50, email='alberto@super_programador.com.br')
    programador_Claudio = Programadores(nome='Claudio', idade=80, email='claudio@super_programador.com.br')
    programador_Ricardo = Programadores(nome='Ricardo', idade=40, email='ricardo@super_programador.com.br')
    programador = Programadores(nome='João', idade=30, email='joao@super_programador.com.br')
    print(programador)
    programador_Claudio.save()
    programador_Ricardo.save()
    programador_Alberto.save()
    programador.save()


def insere_habilidades():
    print("Insere o nome da Habilidade \n")
    habilidade_Alberto = Habilidades(nome='Ruby')
    habilidade_Claudio = Habilidades(nome='PHP')
    habilidade_Ricardo = Habilidades(nome='Javascript')
    habilidade = Habilidades(nome='Python')
    print(habilidade)
    habilidade_Claudio.save()
    habilidade_Ricardo.save()
    habilidade_Alberto.save()
    habilidade.save()


def consulta_programadores():
    print("Consulta Programadores e Informa seus Nomes \n")
    programadores = Programadores.query.all()  # Pessoas.query.filter_by(nome='Claudio')
    print(programadores)

    # pessoa = Pessoas.query.filter_by(nome='Claudio').first()
    # print(pessoa.idade)
    # for alguem in pessoa:
    #     print(alguem)
    # print(pessoa)


def consulta_habilidades():
    print("Consulta Habilidades e Informa seus Nomes \n")
    habilidades = Habilidades.query.all()  # Pessoas.query.filter_by(nome='Claudio')
    print(habilidades)

    # pessoa = Pessoas.query.filter_by(nome='Claudio').first()
    # print(pessoa.idade)
    # for alguem in pessoa:
    #     print(alguem)
    # print(pessoa)


def altera_programadores():
    print("Altera a tabela Programadores modificando Nomes, Idade e E-Mail. \n")
    programador = Programadores.query.filter_by(nome='João').first()
    programador.nome = 'Luís Silva'
    programador.idade = 40
    programador.email = 'Luíss@super_programador.com.br'
    programador.save()


def altera_habilidades():
    print("Altera a tabela Habilidade modificando seu Nome. \n")
    habilidade = Habilidades.query.filter_by(nome='Python').first()
    habilidade.nome = 'Java'
    habilidade.save()


def exclui_programador():
    print("Exclui dados da tabela Programadores. \n")
    programador = Programadores.query.filter_by(nome='Luís Silva').first()
    programador.delete()
    print(f"\n Programador  excluído do sistema com sucesso")


def exclui_habilidade():
    print("Exclui dados da tabela Habilidade. \n")
    habilidade = Habilidades.query.filter_by(nome='Java').first()
    habilidade.delete()
    print(f"\n Habilidade excluída do sistema com sucesso")


if __name__ == '__main__':
    # insere_programadores()
    # insere_habilidades()
    #
    # consulta_programadores()
    # consulta_habilidades()
    #
    # altera_programadores()
    # altera_habilidades()

    #consulta_programadores()
    #consulta_habilidades()

    #exclui_programador()
    #exclui_habilidade()

    consulta_programadores()
    consulta_habilidades()
