from random import randint
tentativas = 1
computador = randint(0, 10)
print('\33[33m-'*40)
print('\33[34mEstou pensando em um número de 0 a 10...')
print('\33[33m-'*5,'Em qual número estou pensando?','-'*5)
jogador = int(input('\33[34mNúmero: '))
while jogador != computador:
    tentativas += 1
    print('\33[31m-'*5,'Você errou! Tente novamente!!','-'*5)
    jogador = int(input('\33[34mNúmero: '))
print('\33[33mVocê me venceu em {} tentativas! Que tal outra partida?!'.format(tentativas))
