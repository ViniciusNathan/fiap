user1 = int(input("Digite um número userA: "))
user2 = int(input("Digite um número userB: "))

def conta():
    calculo = (user1 * 2) * (user2 * 3)
    return print(f'resultado é {calculo}')

print(conta())