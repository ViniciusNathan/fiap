#1
print('Seja muito bem-vindo a Vinheria Agnello')
nome = input('Qual seu nome?')
end = input('Qual seu endereço?')
ano = int(input('Qual ano do se nascimento?'))
idade = 2025 - ano

#2
if idade < 18:
    print('Não é permitido a venda de bebidas alcoólicas para menores de 18 anos')
# else e identar todos as linhas abaixo para bloquear a continuidade do código
#3
msg = '''Os vinhos da casa são:
Opção | Vinho   | R$
  1   | Vinho 1 | 47.70
  2   | Vinho 2 | 123.70
  3   | Vinho 3 | 17.30
  4   | Vinho 4 | 64.00
  5   | Vinho 5 | 450.70
'''

# vinho1 = 47.70
# vinho2 = 123.70
# vinho3 = 17.30
# vinho4 = 64.00
# vinho5 = 450.70

#4
print(msg)
op = input('Digite a opção do vinho desejado')
qtd = int(input('Digite a quantidade de garrafas'))
if op == '1':
    vinho = 47.70
if op == '2':
    vinho = 123.70
if op == '3':
    vinho = 17.30
if op == '4':
    vinho = 64.00
if op == '5':
    vinho = 450.70

valor = vinho * qtd

#5
if valor <= 150:
    frete = 10
    valor = valor + frete

#6
if idade >= 60:
    print('Parabéns você tem um desconto de 5%')
    valor = valor * 0.95

#7
print('Obrigado', nome)
print('Sua entrega será feita em', end)
print('O valor total da compra é de', valor)