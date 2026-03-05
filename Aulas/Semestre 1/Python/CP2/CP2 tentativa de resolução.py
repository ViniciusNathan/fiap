#Verifique o palíndromo de "socorram-me, subi no ônibus em Marrocos" e remova espaço, vírgula, e traço

frase = 'arara'
i = 0 # para percorrer pela frase
inverso = '' # onde vou guardar o oposto

while i < len(frase):
    if frase[i] != ' ' and frase[i] != ',' and frase[i] != '-':
        inverso += frase[i]
    i += 1
if frase == frase[::-1]:
    print('É um palíndromo')

# identifique as vogais de uma palavra
palavra = 'presidente'
vogais = 'aeiou'
extract = ''
x = 0


while x < len(palavra):
    y = 0
    while y < len(vogais):
        if palavra[x] == vogais[y]:
            extract += palavra[x]
            break
        y += 1
    x += 1

print(extract)






word = 'amor'
result = ''
z = 0
soma = 0

while z < len(word):
    if word[z] == 'a' or word[z] == 'e' or word[z] == 'i' or word[z] == 'o' or word[z] == 'u':
        result += word[z]
        soma += 1
    z += 1

print(result, soma)