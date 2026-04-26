# Pedra, papel, tesoura!
from random import randint
from time import sleep

from Cython.Build.Dependencies import join_path

opções = ('pedra', 'papel', 'tesoura')


while True:
    computador = opções[randint(0, 2)]
    print('-' * 30)
    print('Pedra, papel ou tesoura!?')
    print('-' * 30)

    jogador = input('Sua escolha: ').strip().lower()

    print('-'*30)

    if jogador not in opções:
        print('Inválido! Escolha pedra, papel ou tesoura!')
        continue

    else:
        print(f'Jogador jogou {jogador}')
        sleep(1)
        print(f'Computador jogou {computador}')
        sleep(3)

        if jogador == computador:
            print(f'{"EMPATOU":=^30}')

        elif jogador == 'tesoura' and computador == 'pedra':
            print(f'{"VOCÊ PERDEU":=^30}')

        elif jogador == 'papel' and computador == 'tesoura':
            print(f'{"VOCÊ PERDEU":=^30}')

        elif jogador == 'pedra' and computador == 'papel':
            print(f'{"VOCÊ PERDEU":=^30}')

        else:
            print(f'{"VOCÊ GANHOU":=^30}')
            break
