# Faça um programa que simule uma fila. O usuário deve falar se quer adicionar uma pessoa na fila ou atender alguém (remover da fila)
#Caso adicione, pegue o nome da pessoa para adicionar
action = input('Digite "add" para adicionar ou "rem" para remover: ')
lista = []

if action == 'add':
    lista = input('Digite o que quer adicionar: ')
    print(lista)
elif action == 'rem':
    lista.pop(0)

