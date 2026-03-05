notas = [10, 9, 8]

#Repetição com While
i = 0
while i < len(notas):
    print(notas)
    i += 1

#repetição com for
for i in notas:
    print(i)
    if i == 1:
        break

for x in range(10):# de 0 a 9
    print(x)

for y in range(1,11):# de 1 a 10
    print(y)

for y in range(3,12,2): #de 3 a 12 pulando de 2 em 2
    print(y)

for y in range(10,-1,-1): #conta de 10 a 0
    print(y)

# Faça um programa que imprime os números inteiros no intervalo a e b passado pelo usuário

inicial = int(input('Digite número inicial: '))
final = int(input('Digite número inicial: '))
soma = 0

# while inicial <= final:
#     print(inicial)
#     inicial += 1

for x in range(inicial, final + 1):
    print(x)
    soma += x

print(soma, soma / len(range(inicial, final + 1)))

