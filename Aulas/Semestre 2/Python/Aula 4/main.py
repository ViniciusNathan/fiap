import soma_sub
import multi_div

op = input('Digite o que deseja(+, -, *, /)')
if op in ['+','-','*','/']:
    x = float(input('Digite o primeiro valor: '))
    y = float(input('Digite o segundo valor: '))
res = 0
flag = True

if op == '+':
    res = soma_sub.soma(x, y)
elif op == '-':
    res = soma_sub.sub(x, y)
elif op == '*':
    res = multi_div.mult(x, y)
elif op == '/':
    res == multi_div.div(x, y)
else:
    print('Operação inválida')
    flag = False

if flag:
    print(f'resultado de {x}{op}{y} = {res}')
