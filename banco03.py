import textwrap

def menu():
    
    menu = """\n
    ===== MENU =====
    [d] Depósito
    [s] Sacar
    [e] Extrato
    [nc] Nova Conta
    [lc] Listar Contas
    [nu] Novo Usuário
    [q] Sair
    => """
    return input(textwrap.dedent(menu))
    
def depositar(saldo, valor, extrato, /):
    
    if valor > 0:
          saldo += valor
          extrato += f"Depósito: \tR$ {valor:.2f}\n"
          print("Depósito realizado com sucesso!")
    else:
          print("Operação falhou!")
          
    return saldo, extrato
    
def sacar(*, saldo, valor, extrato, limete, numero_saques, limete_saques):
    
    excedeu_saldo = valor > saldo
    excedeu_limete = valor > limete
    excedeu_saques = numero_saques > limete_saques
    
    if excedeu_saldo:
        print("Operação falhou! Saldo insuficiente.")
        
    elif excedeu_limete:
        print("Operação falhou! Limete insuficiente.")
        
    elif excedeu_saques:
        print("Operação falhou! Limete excedido de saques.")
        
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print("Saque realizado!")
        
    else:
        print("Operação falhou!")
        
    return saldo, extrato
    
def exibir_extrato(saldo, /, *, extrato):
    
   print("\n=========== EXTRATO ===========") 
   print("Não foram realizadas movimentações" if not extrato else extrato)
   print(f"\nSaldo:\t\tR$ {saldo:.2f}")
   print("=================================")
    
def criar_usuario(usuarios):
   
   cpf = (input("Informe seu CPF(somente números): "))
   usuario = filtrar_usuario(cpf, usuarios)
   
   if usuario:
       print("\n Esse usuário já existe.")
       return
   
   nome = input("Informe o nome completo: ")
   data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
   endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")
   
   usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
   
   print("Usuário criado com sucesso!")
   
def filtrar_usuario(cpf, usuarios): 
    
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None 
 
def criar_conta(agencia, numero_conta, usuarios):
    
    cpf = input ("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario:
        print("\n Conta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("\n Usuário não encontrado!")
    
def listar_contas(contas):
    
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        
        print("=" * 100)
        print(textwrap.dedent(linha))
    
def main():
    
    LIMETE_SAQUES = 3
    AGENCIA = "0001"
    
    saldo = 0
    limete = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []
    
    while True:
        opcao = menu()
        
        if opcao == "d":
            valor = float(input("Infrome o valor do depósito: "))
            
            saldo , extrato = depositar(saldo, valor, extrato)
            
        elif opcao == "s":
            valor = float(input("Infrome o valor do saque"))  
            
            saldo , extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limete=limete,
                numero_saques=numero_saques,
                limete_saques=LIMETE_SAQUES,
            ) 
            
        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)
            
        elif opcao == "nu":
            criar_usuario(usuarios)
            
        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta) 
                           
        elif opcao == "lc":
            listar_contas(contas)
            
        elif opcao == "q":
            print("Obrigada por usar o Dinjz Bancos!")
            break
        
        else:
            print("Operação inválida.")
main()