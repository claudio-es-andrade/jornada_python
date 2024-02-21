import textwrap 

def deposito(valor, extrato, saldo):

    if valor > 0:
        saldo         +=  valor
        extrato       +=  valor     
    else:
        print("Operação falhou! O valor informado é inválido.")
    return extrato, saldo

def imprime_extrato( extrato, numero_saques ):

    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else f"Numero de Saques até o momento: {numero_saques}")
    print(f" \n Saldo: R$ {extrato:.2f}")
    print("==========================================")

def saque(valor, saldo, extrato, limite, LIMITE_SAQUES, numero_saques ):

    excedeu_saldo   =  valor > saldo

    excedeu_limite  =  valor > limite

    excedeu_saques  =  numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")

    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")

    elif valor > 0:
        saldo          -= valor
        extrato        -= valor  
        numero_saques  += 1

    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo,extrato,numero_saques

def criar_novo_usuario( usuarios  ):
    
    cpf                =  input("Informe o CPF (somente número): ")
    usuario            =  filtrar_usuario_por_cpf(cpf, usuarios)

    if usuario:
        print("\n Usuário já cadastrado! ")
        return

    nome               = input("Informe o nome completo: ")
    data_nascimento    = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco           = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("=== Usuário criado com sucesso! ===")


def criar_nova_conta(numero_conta, agencia, usuarios):
    
    cpf                 = input("Informe o CPF do usuário: ")
    usuario             = filtrar_usuario_por_cpf(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\n Usuário não encontrado, fluxo de criação de conta encerrado! ")

def filtrar_usuario_por_cpf(cpf, usuarios ):
    
    usuarios_filtrados  = [ usuario for usuario in usuarios if (usuario["cpf"] == cpf) ]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def filtrar_usuario_por_nome(nome, usuarios ):
    
    usuarios_filtrados  = [ usuario for usuario in usuarios if (usuario["nome"] == nome) ]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def listar_contas(contas):
    
    if contas:
        for conta in contas:
            linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
            """
            print("=" * 100)
            print(textwrap.dedent(linha))
    else:
        print("Por Favor, crie uma nova conta")

def listar_usuarios(usuarios):
    if usuarios:
        for usuario in usuarios:
            linha = f"""\
            Nome: \t {usuario['nome']}
            CPF: \t  {usuario['cpf']}
            """
            print("=" * 100)
            print(textwrap.dedent(linha))
    else:
        print("Por Favor, crie um novo usuário")

def excluir_contas(contas):
    
    print("Informe o número da Conta que deseja encerrar: \n")
    valor               = int( input() )
    
    for index, conta in enumerate(contas[:]):
        if conta["numero_conta"] == valor:
            del contas[index]
            print(f"\n=== Conta {valor} excluída com sucesso! ===")
            return
        
    print(f"\n=== Conta {valor} não encontrada! ===")

def excluir_usuarios( usuarios):
    cpf                 = input("Informe o CPF do usuário: ")
    usuario             = filtrar_usuario_por_cpf(cpf, usuarios)

    if usuario:
        usuarios.remove(usuario)
        print(f"\n=== Correntista {usuario} excluído com sucesso! ===")

    else: 
        print("\n Usuário não encontrado, fluxo de exclusão de usuário encerrado!")


def menu():
    menu = """\n 
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

def principal( ):

    saldo                 =  0
    limite                =  500
    extrato               =  0 
    numero_saques         =  0
        
    usuarios              = []
    contas                = []

    AGENCIA               = "0001"
    LIMITE_SAQUES         =  3
    # PRESIDENTE_DO_BANCO   = {"nome": "JOÃO DA SILVA", "data_nascimento": "01/04/1960", "cpf": 12340, "endereco": "Rua X, 30 - Onda Nova - Cidadão Antigo/MG "}

    
    while True:

        opcao = menu()
 
        if (opcao == "d") or (opcao == "D"):        
            valor = float(input("Informe o valor do depósito: "))
            extrato, saldo   =    deposito( valor, extrato, saldo )
        
        elif (opcao == "s") or (opcao == "S"):
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato, numero_saques = saque(valor, saldo, extrato, limite, LIMITE_SAQUES, numero_saques )
        
        elif (opcao == "e") or (opcao == "E"):
            imprime_extrato( extrato, numero_saques )
        
        elif (opcao == "nu") or (opcao == "NU"):
            criar_novo_usuario( usuarios )

        elif (opcao == "nc") or (opcao == "NC"):
            numero_conta = len(contas) + 1
            conta = criar_nova_conta(numero_conta, AGENCIA, usuarios )
            if conta:
                contas.append(conta)

        elif (opcao == "lc") or (opcao == "LC"):
            listar_contas(contas)
        
        elif (opcao == "lu") or (opcao == "LU"):
            listar_usuarios(usuarios)

        elif (opcao == "ec") or (opcao == "EC"):
            excluir_contas(contas)
        
        elif (opcao == "eu") or (opcao == "EU"):
            excluir_usuarios( usuarios)
        
        elif (opcao == "q") or (opcao == "Q"):
            break
        
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")
        
############################################### FIM DAS FUNCOES ###############################################

############################################### INICIO PROGRAMA PRINCIPAL ###############################################

principal( )

############################################### FIM PROGRAMA PRINCIPAL ###############################################