# Uma das formas mais simples de obter uma aproximação do valor de Pi é utilizando a fórmula de leibniz para a série infinita
# Pi/4 = 1 - 1/3 + 1/5 - 1/7 + 1/9 - 1/11 + 1/13
# Quanto mais termos adicionarmos, mais precisa

def pi(qtde):
    soma = 0
    for i in range(qtde):
        x = (-1)** i * (2*i+1)
        soma = soma + 1/x
    return 4*soma

print(pi(100000))
