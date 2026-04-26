# Detecção de Arquivo

import os

caminho_arq = '42_teste'

print('\n')

if os.path.exists(caminho_arq):
    print(f'O caminho {caminho_arq} existe') 

    if os.path.isfile(caminho_arq):
        print('É um arquivo')

    elif os.path.isdir(caminho_arq):
        print('É um diretório')
    
else:
    print('O caminho não existe')

print('\n')