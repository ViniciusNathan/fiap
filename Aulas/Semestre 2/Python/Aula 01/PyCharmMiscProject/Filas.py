demandas = ['vini', 'nathan']

user = input(f'aperte a para adicionar o r para executar/remover')

if user == 'a':
    add = input('digite o dado')
    demandas.append(add)
    print(demandas)
elif user == 'r':
    demandas.pop()
    print(demandas)

