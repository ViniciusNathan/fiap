from numba import typeof

obj = [
    [1,2,3],
    [2,4],
    [3,4,5,6]
]
print(obj)

obj2 = [ #É uma matriz porque tem a mesma qtd de elementos em cada item da lista
    [1,2,3],
    [2,4,0],
    [3,4,6]
]

print(obj2[2][1]) #acessar Matriz[Linha 2] e [Coluna 1]
print(len(obj2)) #quantidade de linhas
print(len(obj2[0])) #quantidades de colunas

#crie uma matriz de forma que o usuário passe a quantidade de linhas e a quantidade de colunas e também informe o elemento a ser adicionado

coluna = int(input('Colunas: ')) #qtd de colunas
linhas = int(input('Linhas: ')) #qtd de linhas
m = []
for j in range(linhas):
    linhas = []
    for i in range(coluna):
        linhas.append(int(input('Digite o valor: ')))
    m.append(linhas)

print(m)


