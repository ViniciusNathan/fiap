preco = 0
# Ex 1

preco = 0
while True:
    cod = int(input('Digite o código da fruta ou 0 para sair: '))
    if cod == 1:
        qtde = float(input('Digite quantos kg deseja: '))
        preco += 12.90 * qtde
    elif cod == 2:
        qtde = float(input('Digite quantos kg deseja: '))
        preco += 9.30 * qtde
    elif cod == 3:
        qtde = float(input('Digite quantos kg deseja: '))
        preco += 3.50 * qtde
    elif cod == 4:
        qtde = float(input('Digite quantos kg deseja: '))
        preco += 7 * qtde
    elif cod == 5:
        qtde = float(input('Digite quantos kg deseja: '))
        preco += 37.50 * qtde
    elif cod == 0:
        break
    else:
        print('Código inválido')


print(f'O valor da sua compra é R${preco:.2f}')

# Ex 2
n = int(input('Digite um valor para o fatorial: '))
fat = n
mult = 1
#while n >= 1:
#    mult = mult*n
#    n = n - 1
#print(f'O fatorial de {fat}! = {mult}')
i = 1
while i <= n:
    mult = mult*i
    i = i + 1
print(f'O fatorial de {fat}! = {mult}')



# Ex 3
while True:
    n = int(input('Digite um número:'))
    if n == 0:
        break
    i = 1
    soma = 0
    while i < n:
        if n%i == 0:
            soma = soma + i
        i += 1
    if soma == n:
        print(f'{n} é um número perfeito')
    else:
        print(f'{n} não é um número perfeito pois a soma é {soma}')


# Ex 4
txt = input('Digite uma frase:')
i = 0
soma = 0
while i < len(txt):
    if txt[i] == 'a' or txt[i] == 'e' or txt[i] == 'i' or txt[i] == 'o' or txt[i] == 'u':
        soma += 1
    i += 1
print(f'A qtde de vogais de {txt} = {soma}')


# Ex 5
txt = input('Digite uma frase:')
i = 0
frase = ''
while i < len(txt):
    if txt[i] != ' ' and txt[i] != ',' and txt[i] != '.' and txt[i] != '-':
        frase += txt[i]
    i += 1
if frase == frase[::-1]:
    print('É um palindromo!')



