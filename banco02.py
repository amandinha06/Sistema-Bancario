"""Com os novos conhecimentos adquiridos sobre data e hora, você foi encarregado de implementar as seguintes funcionalidades no sisetma:
- Estabelecer um limite de 10 transações diárias para uma conta
- Se o usuário tentar fazer uma transação após atingir o limite, deve ser informado que ele excedeu o número de transações permitidas para aquele dia.
- Mostre no extrato, a data e hora de todas as transações.
"""

from datetime import datetime

menu = '''
    [1] Depósito 
    [2] Saque
    [3] Extrato
    [4] Sair 
'''

saldo = 0
limite_saque = 500
extrato = []  
cont = 0  
limite_transacoes = 10  

while True:
    opcao = input(menu)

    if opcao == "1": 
        if cont < limite_transacoes:
            valor = float(input("Qual valor deseja depositar? "))
            if valor > 0:
                saldo += valor
                cont += 1  
                time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                extrato.append(f"{time} - Depósito: R$ {valor:.2f}")
                print("Depósito realizado com sucesso!")
            else:
                print("Operação falhou! Valor inválido.")
        else:
            print("Número máximo de transações do dia excedido!")

    elif opcao == "2":  
        if cont < limite_transacoes:
            valor = float(input("Informe o valor do saque: "))
            if valor > limite_saque:
                print("Limite de saque excedido!")
            elif valor > saldo:
                print("Saldo insuficiente!")
            elif valor > 0:
                saldo -= valor
                cont += 1 
                time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                extrato.append(f"{time} - Saque: R$ {valor:.2f}")
                print("Saque realizado com sucesso!")
            else:
                print("Operação falhou! O valor informado é inválido.")
        else:
            print("Número máximo de transações do dia excedido!")

    elif opcao == "3":  
        print("\n================ EXTRATO ================")
        if not extrato:
            print("Não foram realizadas movimentações.")
        else:
            for transacao in extrato:
                print(transacao)  
        print(f"Saldo atual: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "4": 
        print("Obrigada por usar Dinjz bancos!")
        break

    else:
        print("Opção inválida. Tente novamente.")

                