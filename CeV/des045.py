from random import randint
computador = randint(1,3)
player = int(input('''\33[33mPedra, papel ou tesoura?!: 
[1] Pedra
[2] Papel
[3] Tesoura\n'''))
if player == 1 and computador == 1:
    print('Eu escolhi pedra! Empatamos!')
elif player == 2 and computador == 1:
    print('Eu escolhi pedra! Você ganhou!')
elif player == 3 and computador == 1:
    print('Eu escolhi pedra! Você perdeu!')
elif player == 1 and computador == 2:
    print('Eu escolhi papel! Você perdeu!')
elif player == 2 and computador == 2:
    print('Eu escolhi papel! Empatamos!')
elif player == 3 and computador == 2:
    print('Eu escolhi papel! Você ganhou!')
elif player == 1 and computador == 3:
    print('Eu escolhi tesoura! Você ganhou!')
elif player == 2 and computador == 3:
    print('Eu escolhi tesoura! Você perdeu!')
elif player == 3 and computador == 3:
    print('Eu escolhi tesoura! Empatamos!')
else:
    print('\33[31mÉ só pedra, papel, ou tesoura! Você escolheu outra coisa!')