menu = """
        Bem-Vindo(a) ao Atendimento Bancário
           Escolha a operação que deseja:
            [1] Saque
            [2] Depósito
            [3] Extrato
            [0] Sair
          >>> """

saldo = 0
saque = 0
limite = 500
numero_saques = 0
deposito = 0
extrato = ""
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":

        if numero_saques != LIMITE_SAQUES:
            saque = float(input("Valor do Saque: R$ "))
           
            if saque <= saldo and saque <= limite:

                    print("Saque realizado!")
                    saldo -= saque
                    numero_saques += 1
                    extrato += f"Saque: R$-{saque:.2f}\n"
            
            else:
                print("Operação falhou! O valor informado é inválido.")
        
        else:
            print("Você excedeu o limite de saques diários!")
   
    elif opcao == "2":
        deposito = float(input("Valor do depósito: R$ "))
        if deposito > 0:
            print("Depósito realizado!")
            saldo += deposito
            extrato += f"Depósito: R$+{deposito:.2f}\n"
        else: 
            print("Não é permitido valores abaixo de R$ 0,00 (Zero)")
    
    elif opcao == "3":
        if extrato == "":
            print("""
                 --------------------------
                | Não houve movimentação   |
                |      na conta!           |
                 -------------------------- 
                """)
        else:
            print(f"---------------------\n\nExtrato:\n{extrato}Saldo: R${saldo:.2f}\n---------------------")
    
    elif opcao == "0":
        print("Saindo...")
        break
 
    else:
        print("Opção inválida! Tente novamente.")
