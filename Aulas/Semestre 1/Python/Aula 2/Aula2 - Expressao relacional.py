# Exercício 1 - Converter 1 dia 3 horas 46 min e 40 segundos
dia = 1
horas = 3
min = 46
sec = 40
# total 100 000 segundos

# segundos por unidade
tempSec = 60
tempMin = tempSec
tempHora = tempSec * tempMin
tempDia = tempHora * 24
'''print(tempMin)
print(tempHora)
print(tempDia)'''

tempTotal = (dia * tempDia) + (horas * tempHora) + (min * tempMin) + sec
print(tempTotal)

# Converter 87426 segundos para dias, horas, minutos e segundos

segf = 5000000

# segundos
segundoFinal = segf % 60
# minutos
minu = segf // 60
minuFinal = minu % 60
# horas
horas = minu // 60
horasFinal = horas % 24
# dias
diasFinal = horas // 24

print(diasFinal, "dias", horasFinal, "horas", minuFinal, "minutos", segundoFinal, "segundos")

# Boolean

v = True
f = False
print(type(v))

# Faça um programa que avalie a sua nota e lhe retorne verdadeiro ou falso sobre sua aprovação na disciplina
nota = 10
notaPassar = 10

resul = nota >= notaPassar
print(resul)

# Escreva uma expressão para determinar se uma pessoa deve ou não pagar imposto. Considere que pagam impostos pessoas cujo salário é maior que R$ 1200

salario1 = 1400
imposto = 1200

a2 = salario1 >= imposto
print(imposto)

# Escreva um programa que retorne se o cliente pode ou não contratar um empréstimo (com base em uma condição: salário)

salario = 10000
emprestimo = salario >= 90000
print(emprestimo)

# Escreva um programa que mostre True ou False se o nome for par; faça o mesmo para impar

number = 24

par = number % 2 == 0
impar = number % 2 != 0 # n % == 1
print('é par:', par)
print('é impar:', impar)

#Escreva um programa que mostre True se dois números tiverem paridade distinta

n1 = 10
n2 = 23

paridade = n1 % 2 != n2 % 2

print('Paridade distinta?', paridade)