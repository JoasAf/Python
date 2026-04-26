# loop aninhado = Um loop dentro de outro loop

linhas = int(input('Linhas: '))
colunas = int(input('Colunas: '))
simbolo = input('Simbolo: ')

for linha in range(linhas):
    for coluna in range(colunas):
        print(simbolo, end=' ')
    print()