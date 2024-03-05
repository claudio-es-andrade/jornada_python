############################################### INICIO FUNCOES ###############################################
def deposito(valor, extrato, saldo):
            
    if valor > 0:
        saldo += valor
        extrato += valor #f"Depósito: R$ {valor:.2f}\n"
    else:
        print("Operação falhou! O valor informado é inválido.")
    return valor, extrato, saldo

def saque(valor, saldo, extrato, limite, LIMITE_SAQUES, numero_saques):
            

    excedeu_saldo = valor > saldo

    excedeu_limite = valor > limite

    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")

    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")

    elif valor > 0:
        saldo -= valor
        extrato -= valor  # f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1

    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo,extrato,numero_saques

def imprime_extrato(extrato, numero_saques):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else f"Numero de Saques até o momento: {numero_saques}")
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")
    
############################################### FIM DAS FUNCOES ###############################################

############################################### INICIO PROGRAMA PRINCIPAL ###############################################

menu = """
\n 
================ MENU ================
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = 0 # " "
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        
        valor = float(input("Informe o valor do depósito: "))
        valor, extrato, saldo = deposito(valor, extrato, saldo)
        
    elif opcao == "s":

        valor = float(input("Informe o valor do saque: "))
        saldo, extrato, numero_saques = saque(valor, saldo, extrato, limite, LIMITE_SAQUES, numero_saques)
        
    elif opcao == "e":
        imprime_extrato(extrato, numero_saques)
        
    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
        
############################################### FIM PROGRAMA PRINCIPAL ###############################################