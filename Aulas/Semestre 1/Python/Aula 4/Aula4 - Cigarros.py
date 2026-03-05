#Escreva um programa para calcular a redução de tempo de vida de um fumante. Pergunte a quantidade de cigarros fumados por dia e quantos anos ele já fumou. Considere que um fumante perde 10 Minutos de vida a cada cigarro, e calcule quantos dias de vida um fumante perderá. Exiba o total em dias.

qtdPorDia = int(input("Cigarros por dia?"))
qtdeAnos = int(input("Quantos anos?"))
minutosPerdidos = 10

totalCigar = qtdPorDia * (qtdeAnos * 365)
diasPerdidos = int((totalCigar * minutosPerdidos) / 144)

print("Você perdeu", diasPerdidos, "dias da sua vida")


