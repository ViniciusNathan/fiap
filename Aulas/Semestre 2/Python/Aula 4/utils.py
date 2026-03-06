def vogal(t): #verificar se tem vogal
    c = 0
    for i in t:
        if i == 'a' or i == 'e' or i == 'i' or i == '0' or i == 'u':
            c += 1
    return c

def inv(t): #inverter palavra
    return t[::-1]

def contarPalavras(t): #contar palavras - Contar espaços + 1
    if len(t) == 0:
        return 0
    c = 1
    for i in t:
        if t == ' ':
            c += 1
    return c

#len(t.split(' '))