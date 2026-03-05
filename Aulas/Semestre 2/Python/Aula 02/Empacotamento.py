def soma(a, b):
    return a + b

l = [1, 2]
y = soma(*l) # soma (l[0], i[1])
x = soma(1, 2)
print(x)
print(y)

def soma2(*args):
    print(args)
    print(args[0])

soma2(1,2,4,5)

# somar um número de argumentos
def soma3(*args):
    somador = 0
    for i in args:
        somador = somador + i
    return somador / len(args) #caso queira a média

print(soma3(1, 2 , 3, 3))

# criar um lista, guardar e somar os itens
l = []
qtde = int(input('Digite a qtde de notas: '))
for i in range(qtde):
    l.append(float(input(f'Digite as notas{i+1}: ')))
print(l)
print(soma(*l))

def conca(*a):
    juntar = ''
    for i in a:
        juntar += i + ' '
    return juntar[:-1]

print(conca('oi', 'tudo', 'bem'))