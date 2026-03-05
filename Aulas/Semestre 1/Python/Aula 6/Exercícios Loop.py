#Faça um programa para exibir os números de 1 a 100
a = 1
while a <= 100:
    print(a)
    a = a + 1

print('--------')

#Faça um programa para exibir de 50 a 10
b = 50
while b <= 100:
    print(b)
    b += 1

print('--------')

# Faça um programa para escrever a contagem regressiva do lançamento de um foguete. O programa deve imprimir 10, 9, 8 ... 1, 0 e Fogo! na tela
c = 10
while c >= 0:
    print(c)
    c = c - 1
print('Fogo!')

print('--------')

#Faça um programa para imprimir de 1 até o número digitado pelo usuário, mostrando apenas os números pares
d = 1
user = 10


while d <= user:
    if d % 2 == 0:
        print(f'números pares {d}')
    d += 1

print('--------')

#Faça um programa para imprimir de 1 até o número digitado pelo usuário, mostrando apenas números ímpares
user1 = 10
e = 1

while e <= user1:
    if e % 2 != 0:
        print(f'números ímpares {e}')
    e += 1

print('--------')

#Faça um programa para somar todos os pares dentro de um intervalo numérico passado pelo usuário
inicio = int(input('Digite o início'))
fim = int(input('Digite o fim'))
soma = 0

while inicio <= fim:
    if inicio % 2 == 0:
        soma = soma + inicio
    inicio = inicio + 1
print(f'A soma do intervalor é{soma}')

print('--------')

# Break

f = 2
g = 15
while f <= g:
    print(f)
    if f == 10:
        break
    f += 1

print(f)

#continue

# Faça um programa para interromper a execução do while assim que o 0 for digitado e após imprima a soma de todos os valores que o usuário digitou
somaUser = 0

while True:
    user2 = int(input('Digite um número'))
    if user2 == 0:
        break
    somaUser = somaUser + user2
print(f'Soma do usuário {somaUser}')

'''Escreva um programa para controlar uma pequena máquina registradora. Você deve solicitar ao usuário que digite o código do produto e a quantidade comprada.
Utilize a tabela de códigos a seguir para obter o preço de cada produto:

Código Preço
1      0,50
2      1,00
3      4,00
5      7,00
9      8,00

Seu programa deve exibir o total das compras depois que o usuário digitar 0. Qualquer outro código deve gerar a mensagem de erro "Código inválido
'''