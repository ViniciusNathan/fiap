dado = input('Digite algo: ')

print(dado)

usuario = input('Nome do usuário ')
idade = input('Qual sua iddade? ')
print('Olá, meu nome é',usuario, 'e tenho', idade, 'anos')

primeiroNumero = int(input('Primeiro número ')) #int para converter inteiro
segundoNumero = int(input('Segundo número '))

somaNumero = primeiroNumero + segundoNumero

print('Soma', somaNumero)

# Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário, assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0,15 por km rodado

kmRodado = float(input('Quantos Km rodados? '))
diasRodados = int(input('Quantos dias rodados? '))

taxaKmRodado = 0.15
taxaDiasRodados = 60

gastoTotal = (kmRodado * taxaKmRodado) + (diasRodados * taxaDiasRodados)

print(gastoTotal)