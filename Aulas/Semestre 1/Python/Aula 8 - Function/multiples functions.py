def main():
    op = input('Você deseja fazer o que? (1) quadrado (2) soma')
    if op == '1':
        x = float(input('Digite o valor para o quadrado'))
        a = quadrado(x)
        print(f'O quadrado de {x} é {a}')
    elif op == '2':
        x = float(input('Digite o primeiro valor da soma'))
        y = float(input('Digite o segundo valor da soma'))
        som = soma(x,y)
        print(f'A soma de {x} + {y} é {som}')
    else:
        print('opção inválida')

def conta(l):
    return len(l)

def quadrado(x):
    return x**2

def soma(x,y):
    return x + y

main()
