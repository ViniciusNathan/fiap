valor = float(input("digite o valor inicial"))
op = input('Digite 1 para desconto ou 2 para aumento')
tx = float(input('Para a opção escolhida, digite a taxa'))

if op == '1':
    vf = valor - valor * tx
if op == '2':
    vf = valor + valor * tx