# Faça um programa usando f-string para printar a tabela de vinhos de uma forma um pouco mais bonita. Coloque 3 vinhos

v1 = 'Vinho Branco'
v2 = 'Vinho tinto'
v3 = 'Vinho Rose'
valor = 200
x = 20

print(f'|{'id'}|{v1:-^{x}s}|R${valor:.2f}|')
print('-' * 31)
print(f'|{'id'}|{v2:-^20s}|R${valor:.2f}|')
print('-' * 31)
print(f'|{'id'}|{v3:-^20s}|R${valor:.2f}|')

