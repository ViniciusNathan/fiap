soma = lambda a, b: a + b
print(soma(1,2,))

total3 = lambda a, b, c: a + b + c
print(total3(1, 1, 1))

inverter = lambda texto: texto[::-1]
print(inverter('python'))

palindromo = lambda texto: texto == texto[::-1]
print(palindromo('arara'))

pali2 = lambda s: 'é palindromo' if s == s[::-1] else 'não é'
print(pali2('arara'))