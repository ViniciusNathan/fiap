x = input('Digite uma frase: ')

i = 0
frase = ''
while i < len(x):
    if x[i] != ' ' and x[i] != ',':
        frase += x[i]
    i = i + 1

print(f'Frase modificada: {frase}')

valor = 34.903940394
print(f'R${valor:.2f}') #printar duas casas decimais

#Faça um programa que dado um número digitado pelo usuário, calcule o fatorial deste número
user = int(input('Digite um número: '))
y = 1

while user > 0:
    y = y * user
    user = user - 1

print(y)

#Faça um programa para verificar se um número é primo ou não
x = 13 #O que quero saber se é primo ou não
i = 1 #Pra percorrer pelos números menores que x
qtd = 0 #Contar contos restos de 2

while i <= x:
    if x % i == 0:
        qtd = qtd + 1
    i += 1
if qtd == 2:
    print(f'{x} é primo')
else:
    print(f'{x} não é primo')