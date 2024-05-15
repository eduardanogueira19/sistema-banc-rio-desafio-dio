def sacar(*,saldo, extrato, limite, numero_saques, limite_saques):
    if numero_saques != limite_saques:
        valor = float(input("Valor do Saque: R$ "))
           
        if valor <= saldo and valor <= limite:

            print("Saque realizado!")
            saldo -= valor
            numero_saques += 1
            extrato += f"Saque: R$-{valor:.2f}\n"
            
        else:
            print("Operação falhou! O valor informado é inválido.")
        
    else:
        print("Você excedeu o limite de saques diários!")
    return saldo, extrato
   
def depositar(saldo, extrato,/):
    valor = float(input("Valor do depósito: R$ "))
    if valor > 0:
        print("Depósito realizado!")
        saldo += valor
        extrato += f"Depósito: R$+{valor:.2f}\n"
    else: 
        print("Não é permitido valores abaixo de R$ 0,00 (Zero)")
    return saldo, extrato

def visualizar_extrato(saldo,/,*, extrato):
    if extrato == "":
        print("""
             --------------------------
            | Não houve movimentação   |
            |      na conta!           |
             -------------------------- 
            """)
    else:
        print("---------------------")
        print("       Extrato       ")                   
        print(extrato)
        print(f"\nSaldo: R${saldo:.2f}")
        print("---------------------")
    return(extrato, saldo)

def criar_usuario(usuarios):
    nome = str(input("Nome: ")).strip()
    data_nascimento = str(input("Data de nascimento(dd/mm/aaaa): ")).strip()
    cpf = str(input("CPF(apenas números): ")).strip()
    endereco = str(input("Endereço (logradouro, numero - bairro - cidade/sigla estado): "))

    cpf_existente = False
    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            cpf_existente = True
    
            break
    if cpf_existente:
        print("Erro: CPF já cadastrado.")
    else:
        cpf = ''.join(filter(str.isdigit, cpf))
        usuarios.append({'nome': nome, 'data_nascimento': data_nascimento, 'cpf': cpf, 'endereco': endereco})
        print("Usuário criado com sucesso.")

def criar_conta(agencia, contas, usuarios):
    cpf = str(input("Insira o CPF do usuário: "))
    usuario_encontrado = None

    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            usuario_encontrado = usuario
            break

    if usuario_encontrado:
        numero_conta = len(contas) + 1
        contas.append({'agencia': agencia, 'numero_conta': numero_conta, 'usuario': usuario_encontrado})
        print("Conta criada com sucesso!")

    else:
        print("Usuário não encontrado.")   

def listar_contas(contas):
    if not contas:
        print("Não há contas cadastradas.")
    else:
        print("--------------------------------")
        print("\lista de Contas")
        print("--------------------------------")
        for conta in contas:
            agencia = conta['agencia']
            numero_conta = conta['numero_conta']
            usuario = conta['usuario']['nome']
            cpf = conta['usuario']['cpf']
            print(f"Agência : {agencia}")
            print(f"Número da Conta: {numero_conta}")
            print(f"Titular: {usuario}")
            print(f"CPF: {cpf}")
            print(f"------------------------------")

    pass

menu ="""
    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Criar usuário
    [5] Criar conta corrente
    [6] Listar contas
    [s] Sair
>>> """

LIMITE_SAQUES = 3
AGENCIA = "0001"

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
usuarios = []
contas = []

while True:

    opcao = input(menu)

    if opcao == "1":
       saldo, extrato = depositar(saldo, extrato)

    elif opcao == "2":
        saldo, extrato = sacar(saldo=saldo, extrato=extrato, limite=limite, numero_saques=numero_saques, limite_saques=LIMITE_SAQUES)

    elif opcao == "3":
        visualizar_extrato(saldo, extrato=extrato)        

    elif opcao == "4":
        criar_usuario(usuarios)

    elif opcao == "5":
        criar_conta(AGENCIA, contas, usuarios)

    elif opcao == '6':
        listar_contas(contas)

    elif opcao == "s":
        print("Saindo...")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
