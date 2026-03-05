a = 30
b = 40

if a > b:
    print('A é maior que b')
if b >= a:
    print('B maior que A')
print('Oi') #É impresso porque está fora do bloco

if a > b:
    print('A é maior que b')
else: #espera o oposto
    print('B maior que A')

#Escreva um programa que pergunte a velocidade do carro de um usuário. Caso ultrapasse 80 Km/h, exiba uma mensagem dizendo que o usuário foi multado. Nesse caso, exiba o valor da multa, cobrando R$ 5 por km acima de 80Km/h. Caso esteja abaixo do limite lhe dê os parabéns
qualVelo = float(input('Qual foi a velocidade? '))
limiteVelo = 80
taxaMulta = 5
veloSuperior = qualVelo - limiteVelo

if qualVelo >= limiteVelo:
    print('Você foi multado por trafegar', veloSuperior, 'km acima. O valor da multa é R$', (veloSuperior * taxaMulta))
else:
    print('Parabéns, você está dentro da velocidade')

#Escreva um programa que leia três números e que imprima o maior e o menor
nume1 = 20
nume2 = 30
nume3 = 40
# O maior
if nume1 > nume2 and nume1 > nume3:
    print('Número 1 maior')
if nume2 > nume1 and nume2 > nume3:
    print('Número 2 é o maior')
if nume3 > nume1 and nume3 > nume2:
    print('Número 3 é o maior')
# O menor
if nume1 < nume2 and nume1 < nume3:
    print('Número 1 menor')
if nume2 < nume1 and nume2 < nume3:
    print('Número 2 é o menor')
if nume3 < nume1 and nume3 < nume2:
    print('Número 3 é o menor')
#Igual
if nume1 == nume2 and nume1 == nume3:
    print('Número 1 menor')
if nume2 == nume1 and nume2 == nume3:
    print('Número 2 é o menor')
if nume3 == nume1 and nume3 == nume2:
    print('Número 3 é o menor')

#Escreva um programa que pergunte o salário do funcionçario e calcule o valor do aumento. Para salários superiores a R$ 1.250,00, calcule um aumento de 10%. Para os inferiores ou iguais, de 15%
qualSalario = int(input('Qual o seu salário? '))
tetoSalario = 1250
aumento1 = qualSalario * 1.10
aumento2 = qualSalario * 1.15

if qualSalario >= tetoSalario:
    print('Você recebeu um aumento de R$', aumento1)
if qualSalario < tetoSalario:
    print('Você recebeu um aumento de R$', aumento2)



