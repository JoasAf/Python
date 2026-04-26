# Escrevendo arquivos (.txt, .json, .csv)

#.txt
caminho_arq = '43_saida.txt'

try:
    with open(caminho_arq, 'r') as arq:
        conteudo = arq.read()

        print(conteudo)

except FileNotFoundError:
    print('Arquivo não encontrado')

#.json
import json

caminho_arq = '43_saida.json'

try:
    with open(caminho_arq, 'r') as arq:
        conteudo = json.load(arq)

        print(conteudo['cidade'])

except FileNotFoundError:
    print('Arquivo não encontrado')

#.csv
import csv

caminho_arq = '43_saida.csv'

try:
    with open(caminho_arq, 'r') as arq:
        conteudo = csv.reader(arq)

        for linha in conteudo:
            print(linha[0])
        
except FileNotFoundError:
    print('Arquivo não encontrado')
