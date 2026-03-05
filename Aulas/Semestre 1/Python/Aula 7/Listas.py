l = [10, 20, 30, 40, 3.45, 'oi', True, [1, 2]]
i = 0
print(l[0])
print(l[-1][0])
print(type(l))
print(10 in l)

while i < len(l):
    print(l[i])
    i += 1

#Dado uma lista de notas, faça um programa a calcular a soma e a média de todas notas
lista = [10, 10, 10, 10, 10]
x = 0
soma = 0
media = 0
media2 = 0

while x < len(lista):
    soma += lista[x]
    media = media + lista[x] / len(lista) #opção 1
    # print(media)
    x += 1

media2 = soma / len(lista) #opção 2

print(soma)
print(media)
print(media2)