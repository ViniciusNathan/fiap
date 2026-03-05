# %d inteiro
# %f float
# %s string

x = 18
a = '%d' %x
b = '%03d' %x
print(b)

y = 18.89768763
c = 'Eu tenho R$%.2f reais' %y # 2 casas decimais
d = 'Eu tenho R$%10.2f reais' %y #10 espaços
print(c)
print(d)

# Forma 1
nome = 'Vinicius'
idade = 35
frase = 'Eu me chamo %s e tenho %d anos' % (nome, idade)
print(frase)

# Forma 2
frase2 = 'Eu me chamo {} e tenho {} anos e tenho R${:.2f}' .format(nome, idade, y)
print(frase2)

# Forma 3 mais atual f string
frase3 = f'Eu me {nome} tenho {idade} e R${y:.2f}'
print(frase3)
