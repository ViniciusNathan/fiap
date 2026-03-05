a = 'Fiap'
b = '_Paulista'
tam = len(a)
print(a)
print(a + b)
print(a * 5)
print(tam)

c = 'Hoje_tem_aula!'
print('Tamanho', len(c))

print(c[2])
print(c[13])
print(c[len(c)-1]) #Acessar último caracter

#Fatiar
print(c[5:8]) #colocar um número a mais do index, o último não printa
print(c[9:]) # do index escolhido "9" até o fim
print(c[:6]) # do começo até o index escolhido "6"
print(c[1:8:2]) # o 2 é para o passo

# Faça um programa que dado o nome de uma pessoa, escreva na tela o número de letras do nome e a primeira letra do nome da pessoa
nome = 'Vinicius'
print('Seu nome tem', len(nome), 'carateres')
print('Primeira letra: ', nome[0])

# Faça um programa que dado uma palavra, retorne os caracteres nas posições pares
print('Letras pares', nome[0::2])

# Faça um programa que dado uma palavra, retorne os caracteres nas posições ímpares
print('Letras ímpares', nome[1::2])

# Faça um programa que dado duas strings escreva na tela a concatenação delas com exceção do primeiro caractere de cada uma
nome1 = 'Vinicius'
nome2 = 'Nathan'

print('Concatenar sem a primeira letra de cada palavra fica: ', nome1[1:] + nome2[1:])

# Faça um programa que dado uma palavra, retorne a palavra invertida e verifique se é palíndromo
nome3 = 'natan'
nome4 = nome3[::-1]

if nome3 == nome4:
    print('É um palíndromo')
else:
    print('Não é um palíndrimo')

##########################

x = 6

if x >= 1 and x < 2:
    y = x
elif x >= 2 and x < 3.5:
    y = 2
elif x >= 3.5 and x < 5:
    y = 3
else:
    y = x ** 2 - 10 * x + 28

print(y)