#Usando apenas operadores relacionais e aritméticos, vamos escrever um programa que lê um número e verifica em qual dos seguintes casos o número se enquadra
# par e menor que 100
# par e maior ou igual a 100
# impar e menor que 100
# impar e maior ou igual a 100

a = 27

if a % 2 == 0:
    if a < 100:
        print("A é par e menor 100")
    else:
        print("A é par e maior 100")
else:
    if a < 100:
        print("A é impar e menor 100")
    if a >= 100:
        print("A é impar e menor 100")


#Agora usando também operadores lógicos, vamos escrever um programa que lê um número e verifica em qual dos seguintes casos o número se enquadra
# par e menor que 100
# par e maior ou igual a 100
# impar e menor que 100
# impar e maior ou igual a 100

b = 120
if b % 2 == 0 and b < 100:
    print("B é par e menor 100")
if b % 2 == 1 and b < 100:
    print("B é impar e menor 100")



# else:
#     print("B é par e maior 100")

# else:
#     print("B é impar e maior 100")