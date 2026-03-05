#número perfeito
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