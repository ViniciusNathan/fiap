# printe em tela todos os segundos do dia no formato
# hh:mm:ss

import time #lib externa

for h in range(24):
    for m in range(60):
        for s in range(60):
            time.sleep(1) # imprime um por segundo
            print(f'{h:02d}:{m:02d}:{s:02d}') #d de número inteiro

