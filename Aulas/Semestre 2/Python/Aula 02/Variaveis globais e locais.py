#Crie um programa que simule um banco, usando variáveis globais saldo e transações.
# Implemente as funções depositar(valor), sacar(valor) e extrato()

saldo = 0
transacoes = [] # listas são globais por padrão

def sacar(valor):
    global saldo
    saldo =- valor
    # if valor > saldo:
    #     print('Saldo inválido')
    transacoes.append(-valor)
    return None

def depositar(valor):
    global saldo
    saldo += valor
    transacoes.append(+valor)
    return None

def extrato():
    for i in transacoes:
        print(f'R${i:.2f}')
    print(f'R${saldo:.2f}')

while True:
    op = input('Digite o que deseja (1) sacar; (2) depositar; (3) extrato; outro para sair')
    if op == '1':
        valor = float(input('Digite o valor para o saque'))
        sacar(valor)
    elif op == '2':
        valor = float(input('Digite o valor para o saque'))
        depositar(valor)
    elif op == '3':
        extrato()
    else:
        break


