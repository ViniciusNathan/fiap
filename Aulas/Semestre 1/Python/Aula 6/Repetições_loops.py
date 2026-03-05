a = 1
while a <= 5:
    print(a)
    a = a + 1

#Faça uma tabela mostrando os valores que i j n assume em cada execução do while
i = 0
j = 10
n = 0
while i < j:
    i = i + 1
    j = j - 1
    n = n + 1
    print(i)

# i = 0 | j = 10 | n = 0
# i = 1 | j = 9 | n = 1
# i = 2 | j = 8 | n = 2
# i = 3 | j = 7 | n = 3
# i = 4 | j = 6 | n = 4
# i = 5 | j = 5 | n = 5 acabou

i = 0
j = 0
n = 0
while i < 10:
    i = i + 1
    n = n + i + j
    j = j + 1
    print(i)

# i = 0 | j = 0 | n = 0
# i = 1 | j = 1 | n = 1
# i = 3 | j = 3 | n = 9
# i = 4 | j = 4 | n = 16
# i = 5 | j = 5 | n = 25
# i = 6 | j = 6 | n = 36
# i = 7 | j = 7 | n = 49
# i = 8 | j = 8 | n = 64
# i = 9 | j = 9 | n = 81
# i = 10 | j = 10 | n = 100