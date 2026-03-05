"""
1) dê um oi para o usuário
2) pergunte a velocidade dele
3) Aplique uma multa de 5 reais para cada km/h acima de 110km/h
4) Pergunte como ele deseja pagar
5) Aplique um taxa de 10% para pagamentos no crédito e um desconto de 15% para pagamentos pix
6) informe o valor a pagar
7) Dê um tchau para o usuário
"""

print("Olá, tudo bem?")
qualVelo = int(input("Qual velocidade?"))
limiteVel = 110
taxa = 5
taxaCred = 1.10
descPix = 0.85

if qualVelo > limiteVel:
    valMulta = (qualVelo - limiteVel) * taxa
    print("acima da velocidade com valor de R$", valMulta)
    formaPag = input("como deseja pagar?")
    if formaPag == 'crédito':
        calcMulta = int(valMulta * taxaCred)
        print('Valor total R$', calcMulta)
    if formaPag == 'pix':
        calcMulta = int(valMulta * descPix)
        print('Valor total R$', calcMulta)
else:
    print("abaixo do limite, parabéns!")