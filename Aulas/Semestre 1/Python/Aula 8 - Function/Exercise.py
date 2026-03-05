# 1 Faça uma função que necessite de 3 argumentos e que forneça a soma
def tres(a, b, c):
    return a + b + c

# print(tres(1, 1, 1))

# 2 Escreva uma função que retorne o maior de dois números

def bigger(x, y):
    if x > y:
        return x
    elif y > x:
        return y
    else:
        return x, y

# print(bigger(2, 1))

# Função que receba dois números e retorne True se o primeiro número for múltiplo do segundo
def maiorQ(d, e):
    if d % e == 0:
        return True
    elif e % d == 0:
        return True
    else:
        return False

# print(maiorQ(2, 4))

# Função para calcular fatorial, usando while e outra função com for
def fatorial():
    numero =  int(input('Digite um número: '))
    count = 1
    resultado = 1
    while count <= numero:
        resultado = resultado * count # resultado *= count
        count = count + 1 # count += 1
    print(f'O fatorial de {numero} é {resultado}')

# fatorial()

def novoFatorial():
    number = int(input('digite o número: '))
    counter = 1
    result = 1
    while counter <= number:
        result *= counter
        counter += 1
    print(f'o Fatorial de {number} é {result}')

#novoFatorial()

# Uma das formas mais simples de obter uma aproximação do valor de Pi é utilizando a fórmula de leibniz para a série infinita
# Pi/4 = 1 - 1/3 + 1/5 - 1/7 + 1/9 - 1/11 + 1/13
# Quanto mais termos adicionarmos, mais precisa

def pi(c):
    soma = 0
    for i in range(c):
        soma += (1/(2 * i + 1)*(-1) **i)
    return 4 * soma

#print(f'O valor de pi para {c} termos é: {soma * 4}')

# Um número múltoiplo do outro
def multiplo(a, b):
    if a % b == 0:
        return True
    else:
        return False

#print(multiplo(2, 2))

#retorna a hipotenusa dos catetos raiz quadrada c1^2 + c2^2 = h

def hipo(c1, c2):
    hipot = (c1**2 + c2**2) ** 0.5
    return hipot

print(hipo(3, 4))