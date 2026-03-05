animais = []
print(animais)
animais.append('Gato')
print(animais)


#Adicionar a lista
notas = []
i = 1

while i <= 10:
    a = float(input('Digite'))
    notas.append(a)
    i += 1

print(notas)

#remove da lista
rem = notas.pop()
rem = notas.pop(0)
print(rem)

lista = [1, 2]
lista.extend([3, 4])
print(lista)