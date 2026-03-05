#Crie um programa que usa uma variável global para armazenar um carrinho de compras
# Implemente as funções
# adicionar_produto(produto), remover_produto(produto) e ver_carrinho()

carrinho = []

def adicionar_produto(produto):
    carrinho.append(produto)

def remover_produto(produto):
    for i in range(len(carrinho)):
        if produto == carrinho[i]:
            carrinho.pop
            break

def ver_carrinho():
    for i in carrinho:
        print(i)

while True:
    op = input('(1) add; (2) remove; (3) checkout;(else) exit')
    if op == '1':
        produto = input('Digite o nome do produto')
        adicionar_produto(produto)
        print()
    elif op == '2':
        produto = input('Digite o nome do produto')
        remover_produto(produto)
        print()
    elif op == '2':
        ver_carrinho()
        print()
    else:
        break