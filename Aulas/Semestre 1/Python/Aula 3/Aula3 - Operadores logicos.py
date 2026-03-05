# not aplicado no True da False e not no False da True

# and -> para duas expressões (True ou False)
# True and True -> True
# False and True -> False
# True and False -> False
# False and False -> False

# or retorna verdadeiro se uma das expressões é verdadeiro
# T or T -> T
# T or F -> T
# F or T -> T
# F or F -> F

# ordem dos operadores not -> and -> or

a = 5 * 4 < 4 + 3 #false
b = 6 * 2 - 1 > 3 * 1 #True
c = 9 - 4 / 2 <= 7 + 1 or 5 * 2 - 3 != 6 #True
d = 9 / 3 == 3 * 3 and 2 * 3 - 1 >= 8 #False
print(a, b, c, d)

# Escreva um programa que retorne se o cliente pode ou não contratar um empréstimo (com base em duas condições, idade E salário). O programa deve escrever na tela True ou False
idade = 35
salario = 1200
idadeM = 18
salarioM = 1000
regiao = 'SP'
emprestimo = (idade >= idadeM and salario >= salarioM) or regiao == 'SP'
print('Aprovado?', emprestimo)

# Escreva um expressão que ser
notaC = 7
Mat1 = 8
Mat2 = 6
Mat3 = 5
passou = Mat1 >= notaC and Mat2 >= notaC and Mat3 >= notaC
print('Passou?', passou)