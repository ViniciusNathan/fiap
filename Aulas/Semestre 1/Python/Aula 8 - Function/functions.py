def quad(x): #pode não ter parâmentro. Se não tiver aqui, lá embaixo tb não
    aux = x * x
    print('Estou dentro da função')
    return x**2 #x * x
    # abaixo do return não é lido pela função

a = quad(2)

print(a)

def quad2(y):
    print(y*'-')
    # Não precisa ter return em alguns casos

quad(10)

def conta(l):
    return len(l) #pode retornar uma função

a = [1, 2, 3, 4, 5, 6]
tam = conta(a)
print(tam)