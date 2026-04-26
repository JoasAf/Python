from des115.lib.dados import *


def linha(tam = 40):
    return '-'*tam


def titulo(txt, tam = 40, cor = '\33[m'):
    print(linha())
    print(f'{cor}{txt.center(tam)}\33[m')
    print(linha())


def menu(opcs):
    print(linha())
    cont = 1
    for opc in opcs:
        print(f'\33[33m{cont} - \33[36m{opc}\33[m')
        cont+=1
    print(linha())
    return leiaOpc('Opção: ', len(opcs))


def cadastro(txt, nome = 'desconhecido', idade = 0):
    with open(txt, 'at', encoding='utf-8') as f:
        f.write(f'{nome};{idade}\n')
    titulo(f'{nome.upper()} CADASTRADO COM SUCESSO!', 40, '\33[32m')


def formata(txt):
    with open(txt, 'rt', encoding='utf-8') as pessoa:
        for linha in pessoa:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30} {dado[1]:>3} anos')
