# Desafio do Sistema Bancário DIO

##Sistema conta com 3 principais funções:
### - Saque:
      - Máximo de 3 saques diários com limite de R$ 500,00 por saque.
      - Caso não tenha dinheiro em Saldo, exibir mensagem de erro.
      - Todos os saques devem ser armazenados em uma variável e exibidos na operação de extrato.
### - Depósito:
      - Somente valores positivos.
      - Todos os depósitos devem ser armazenados em uma variável e exibidos na operação de extrato.
### - Extrato:
      - Listar todoa os depósitos e saques realizados na conta.
      - No fim da listagem exibir o saldo atual.
      - Modelo: R$ xxx.xx
## Atualização do sistema
- Possui 3 novas funções: Criar usuário, Criar conta e Listar todas as contas

### - Criar usuário:
      - Pedir os dados pessoais do usuário (nome, cpf, data de nascimento e endereço.
      - Não deixar criar um usuário com um CPF já existente no sistema.
### - Criar conta: 
      - Pedir o CPF do usuário, se já estiver cadastrado no sistema criar conta. Caso negativo mostrar uma mensagem da impossibilidade de criar a conta.
      - Um usuário pode ter várias contas.
