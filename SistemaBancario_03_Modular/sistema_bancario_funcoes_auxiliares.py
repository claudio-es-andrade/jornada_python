from abc import ABC, abstractclassmethod, abstractproperty
from datetime import date, datetime
import textwrap
from sistema_bancario_classes import Cliente, Conta, ContaCorrente, ContaPoupanca, PessoaFisica, Historico, Transacao, Saque, Deposito


def filtrar_usuario_por_cpf(cpf, clientes):
    clientes_filtrados             = [cliente for cliente in clientes if cliente.cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None

def recuperar_conta_cliente(cliente):
    if not cliente.contas:
        print("\n    Cliente não possui conta!    ")
        return

    # FIXME: não permite cliente escolher a conta
    return cliente.contas[0]

def depositar( clientes):
    cpf                            = input("Informe o CPF do cliente: ")
    cliente                        = filtrar_usuario_por_cpf(cpf, clientes)

    if not cliente:
        print("\n    Cliente não encontrado!    ")
        return

    valor                          = float(input("Informe o valor do depósito: "))
    transacao                      = Deposito(valor)

    conta                          = recuperar_conta_cliente(cliente)
    if not conta:
        return

    cliente.realizar_transacao(conta, transacao)


def sacar( clientes ):
    cpf                            = input("Informe o CPF do cliente: ")
    cliente                        = filtrar_usuario_por_cpf(cpf, clientes)

    if not cliente:
        print("\n    Cliente não encontrado!    ")
        return

    valor                          = float(input("Informe o valor do saque: "))
    transacao                      = Saque(valor)

    conta                          = recuperar_conta_cliente(cliente)
    if not conta:
        return

    cliente.realizar_transacao(conta, transacao)

def imprimir_extrato( clientes ):
    cpf                            = input("Informe o CPF do cliente: ")
    cliente                        = filtrar_usuario_por_cpf(cpf, clientes)

    if not cliente:
        print("\n    Cliente não encontrado!    ")
        return

    conta                          = recuperar_conta_cliente(cliente)
    if not conta:
        return

    print("\n================ EXTRATO ================")
    transacoes                     = conta.historico.transacoes

    extrato                        = ""
    if not transacoes:
        extrato                    = "Não foram realizadas movimentações."
    else:
        for transacao in transacoes:
            extrato                += f"\n{transacao['tipo']}:\n\tR$ {transacao['valor']:.2f}  -->  {transacao['data']}"

    print(extrato)
    print(f"\nSaldo:\n\tR$ {conta.saldo:.2f}")
    print(f"\n {transacao['data']} ")
    print("==========================================")


def criar_cliente( clientes ):
    cpf                            = input("Informe o CPF (somente número): ")
    cliente                        = filtrar_usuario_por_cpf(cpf, clientes)

    if cliente:
        print("\n    Já existe cliente com esse CPF!    ")
        return

    nome                           = input("Informe o nome completo: ")
    data_nascimento                = input("Informe a data de nascimento (dd-Mmm-aaaa/01-Mar-1980): ")
    endereco                       = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    cliente                        = PessoaFisica(nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco)

    clientes.append(cliente)

    print("\n    Cliente criado com sucesso!    ")


def criar_conta_corrente(numero_conta, clientes, contas):
    cpf                            = input("Informe o CPF do cliente: ")
    cliente                        = filtrar_usuario_por_cpf(cpf, clientes)

    if not cliente:
        print("\n    Cliente não encontrado, fluxo de criação de conta encerrado!    ")
        return

    conta                          = ContaCorrente.nova_conta(cliente=cliente, numero=numero_conta)
    contas.append(conta)
    cliente.contas.append(conta)

    print("\n    Conta criada com sucesso!    ")

def criar_conta_poupanca(numero_conta, clientes, contas):
    cpf                            = input("Informe o CPF do cliente: ")
    cliente                        = filtrar_usuario_por_cpf(cpf, clientes)

    if not cliente:
        print("\n    Cliente não encontrado, fluxo de criação de conta encerrado!    ")
        return

    conta                          = ContaPoupanca.nova_conta(cliente=cliente, numero=numero_conta)
    contas.append(conta)
    cliente.contas.append(conta)

    print("\n    Conta criada com sucesso!    ")


def listar_contas( contas):
    
    if contas:
        for conta in contas:
            print("=" * 100)
            print(textwrap.dedent(str(conta)))
    else:
        print("Por Favor, crie uma nova Conta")

def listar_usuarios( clientes):
    if clientes:
        for cliente in clientes:
            if isinstance(cliente, PessoaFisica):
                print("=" * 100)
                print(textwrap.dedent(str(cliente)))
    else:
        print("Por Favor, crie um novo CLIENTE")

def excluir_contas( contas):
    
    print("Informe o número da Conta que deseja encerrar: \n")
    valor                          = int( input() )
    
    for index, conta in enumerate(contas[:]):
        if conta.numero == valor:
            del contas[index]
            print(f"\n=== Conta {valor} excluída com sucesso! ===")
            return
        
    print(f"\n=== Conta {valor} não encontrada! ===")

def excluir_usuarios( clientes):
    cpf                            = input("Informe o CPF do usuário: ")
    cliente                        = filtrar_usuario_por_cpf(cpf, clientes)

    if cliente:
        clientes.remove(cliente)
        print(f"\n    Correntista {cliente} excluído com sucesso!    ")

    else: 
        print("\n Usuário não encontrado, fluxo de exclusão de usuário encerrado!")


def menu():
    menu                           = """\n 
    ================ MENU ================
    [d]  \t DEPOSITAR
    [e]  \t EXTRATO
    [s]  \t SACAR
    [lc] \t LISTAR CONTAS
    [lu] \t LISTAR USUARIOS
    [nc] \t NOVA CONTA
    [nu] \t NOVO USUÁRIO
    [ec] \t EXCLUIR CONTA
    [eu] \t EXCLUIR USUÁRIO
    [q]  \t SAIR
    => """
    return input(textwrap.dedent(menu))

def sub_menu_conta():
    submenu                           = """\n 
    ================ MENU ================
    [cc]  \t CONTA CORRENTE
    [cp]  \t CONTA POUPANÇA
    [v]   \t VOLTAR
    => """
    return input(textwrap.dedent(submenu))

def principal( ):

    clientes                       = []
    contas                         = []

    while True:
        opcao                      = menu()

        if (opcao == "d") or (opcao == "D"):
            depositar(clientes)

        elif (opcao == "s") or (opcao == "S"):
            sacar(clientes)

        elif (opcao == "e") or (opcao == "E"):
            imprimir_extrato(clientes)

        elif (opcao == "nu") or (opcao == "NU"):
            criar_cliente(clientes)

        elif (opcao == "nc") or (opcao == "NC"):
            
            while True:
                sub_opcao          = sub_menu_conta()
                
                if (sub_opcao == "cc") or (sub_opcao == "CC"):
                    numero_conta = len(contas) + 1    
                    criar_conta_corrente(numero_conta, clientes, contas)
                    break
                elif (sub_opcao == "cp") or (sub_opcao == "CP"):
                    numero_conta = len(contas) + 1    
                    criar_conta_poupanca(numero_conta, clientes, contas)
                    break
                elif (sub_opcao == "v") or (sub_opcao == "V"):
                    break

        elif (opcao == "lc") or (opcao == "LC"):
            listar_contas(contas)
        
        elif (opcao == "lu") or (opcao == "LU"):
            listar_usuarios(clientes)

        elif (opcao == "ec") or (opcao == "EC"):
            excluir_contas(contas)
        
        elif (opcao == "eu") or (opcao == "EU"):
            excluir_usuarios( clientes)

        elif (opcao == "q") or (opcao == "Q"):
            break

        else:
            print("\n   Operação inválida, por favor selecione novamente a operação desejada.    ")
        
