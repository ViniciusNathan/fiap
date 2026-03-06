l = []
for i in range(10):
    l.append(0)
print(l)

l = []
for i in range(10):
    if i % 2 ==0:
        l.append(0)
print(l)


l1 = [0 for i in range(10)]
l2 = [i for i in range(10)]

l3 = [i for i in range(10) if i % 2 == 0]

print(l1, l2, l3)

#Crie uma lista com os quadrados dos números de 1 a 10
l4 = [i**2 for i in range(1, 11)]
print(f'Quadrados da lista => {l4}')

#Gere uma lista contendo apenas pares de 1 a 20

l5 = [i for i in range(1, 21) if i % 2 == 0]
print(f'Apenas pares da lista => {l5}')

#Crie uma lista contendo o comprimento de cada palavra na lista ['Python', ' List', 'Comprehension', 'Exercícios']

lista6 = ['Python', ' List', 'Comprehension', 'Exercícios']
l6 = [len(i) for i in lista6]
print(f'Comprimento => {l6}')

#Converta uma lista de temperaturas em Celsius [0, 10, 20, 30, 40] para Fahrenheit usando a fórmula F = C*9/5 +32

lista7 = [0, 10, 20, 30, 40]
l7 = [i*9/5 + 32 for i in lista7]
print(f'Celsius para Fahrenheit => {l7}')

#Gere uma lista com os números de  1 a 20, substituindo os múltiplos de 3 por 'Fizz'

l8 = ['Fizz' if i % 3 == 0 else i for i in range(1, 21)]
print(f'Fizz => {l8}')

#Dada a lista de palavras ['Maçã', 'Banana', 'Uva', 'Morango', 'Abacaxi'] crie uma nova lista contendo apenas as palavras com mais de 5 letras

lista9 = ['Maçã', 'Banana', 'Uva', 'Morango', 'Abacaxi']
l9 = [i for i in lista9 if len(i) > 5]
print(f'palavras com 5 letras => {l9}')

#Gere uma lista de representando as coodernadas [x,y] para um grid 3x3
l10 = [[x,y] for x in range(3) for y in range(3)]

print(f'Grid 3x3 {l10}')