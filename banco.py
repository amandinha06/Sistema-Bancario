menu = '''
    [1] Depósito 
    [2] Saque
    [3] Extrato
    [4] Sair 
'''

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3


while True:
    
    opcao = input(menu)
    
    if opcao == "1":
        valor = int(input("Qual valor deseja depositar? "))
        if valor > 0:
           saldo += valor
           extrato += f"Deposito: R$ {valor:.2f}\n"
           
        else:
            print("Operção falhou! Tente novamente.")
    
    elif opcao == "2":
        
        excedeu_saques = numero_saques >= LIMITE_SAQUES
        
        valor = int(input("Informe o valor do saque: "))
        
        if valor > limite:
            print("Limete exedido!")
        elif valor > saldo:
            print("Saldo exedido!")
        elif excedeu_saques:
            print("Número máximo de saques excedido!")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido.")
    
    elif opcao == "3":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")    
        
    elif opcao == "4":
        break