n = 90

# Versão não identada Valida todos os if
if n >= 90:
    print('A')
if n < 90 and n > 70:
    print('B')
if n < 70 and n >= 50:
    print('C')
if n < 50:
    print('D')

# Versão  identada
if n >= 90:
    print('A')
else:
    if n >= 70:
        print('B')
    else:
        if n >= 50:
            print('C')
        else:
            print('D')

# elif => else if mais compacto
if n >= 90:
    print('A')
elif n >= 70:
    print('B')
elif n >= 50:
    print('C')
else:
    print('D')

# Escreva um programa que leia dois números e que pergunte qual operação você deseja realizar. Você deve poder calcular soma (+) subtração (-) multiplicação (*) e divisão (/). Exiba o resultado da operação e retorne operação invalida se preencher valores não aceito

n1 = float(input('Qual primeiro número?'))
n2 = float(input('Qual segundo número?'))
operator = input('Qual operação?( + - * / )')
a = True # variável sinalizadora

if operator == '+':
    value = n1 + n2
elif operator == '-':
    value = n1 - n2
elif operator == '*':
    value = n1 * n2
elif operator == '/':
    value = n1 / n2
else:
    a = False
    print('Valor errado')

if a:
    print('Resultado: ', value)

# Escreva um programa que calcule o preço a pagar pelo fornecimento de energia elétrica. Pergunte a quantidade de kWh consumida e o tipo de instalação: R para residências, I para indústrias e C para comércio. Calcule o preço a pagar de acordo com a tabela a seguir

watts = int(input('Quantos kWh foram consumidos?'))
instalation = input('Qual instalação? R para residências, I para indústrias e C para comércio')
valido = True

if instalation == 'R':
    if watts < 500:
        value = watts * 0.40
    else:
        value = watts * 0.65
elif instalation == 'I':
    if watts < 1000:
        value = watts * 0.55
    else:
        value = watts * 0.60
elif instalation == 'C':
    if watts < 5000:
        value = watts * 0.55
    else:
        value = watts * 0.60
else:
    valido = False
    print('Opção errada')

if valido:
    print('Sua conta ficou em: ', value)