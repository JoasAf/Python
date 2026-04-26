# Escrevendo arquivos (.txt, .json, .csv)

#.txt
alunos = ['Joas', 'Anna', 'Cintia', 'Thomas', 'Thalyta']

caminho_arq = '43_saida.txt'

try:
    with open(caminho_arq, 'w') as arq:
        for aluno in alunos:
            arq.write(aluno + '\n')

        print(f'Sucesso')
except FileExistsError:
    print('O arquivo já existe!')


#.json
import json

aluno = {
    'nome': 'Joas',
    'idade': 17,
    'rua': 'Sao Vicente',
    'cidade': 'Blumenau',
    'estado': 'SC'
}

caminho_arq = '43_saida.json'

try:
    with open(caminho_arq, 'w') as arq:
        json.dump(aluno, arq, indent=4)

        print(f'Sucesso')
except FileExistsError:
    print('O arquivo já existe!')

#.csv
import csv

alunos = [['nome', 'idade', 'media'],
          ['Joas', 17, 8.6],
          ['Anna', 16, 9.2],
          ['Cintia', 16, 8.1],
          ['Thomas', 15, 6.7],
          ['Thalyta', 16, 7.7]]

caminho_arq = '43_saida.csv'

try:
    with open(caminho_arq, 'w', newline='') as arq:
        escreve = csv.writer(arq)

        for linha in alunos:
            escreve.writerow(linha)

        print(f'Sucesso')
except FileExistsError:
    print('O arquivo já existe!')