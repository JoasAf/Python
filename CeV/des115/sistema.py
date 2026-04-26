from des115.lib.interface import *
from time import sleep

arqExis('pessoas.txt')

while True:

    opc = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do programa'])

    if opc == 1:
        titulo('PESSOAS CADASTRADAS')
        formata('pessoas.txt')

    elif opc == 2:
        titulo('CADASTRO')
        nome = input('\33[33mNome: ')
        idade = leiaInt('\33[33mIdade: \33[m')
        cadastro('pessoas.txt', nome, idade)

    elif opc == 3:
        titulo('SAINDO DO PROGRAMA...ATÉ MAIS!')
        break
    sleep(2)