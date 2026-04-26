from operator import itemgetter
from time import sleep
from random import randint
jogo = dict()
for valores in range(0, 4):
    jogo['Jogador '+str(valores+1)] = randint(1, 6)
rank = sorted(jogo.items(), key=itemgetter(1), reverse=True)
for k, v in jogo.items():
    sleep(0.7)
    print(f'{k} tirou {v}')
sleep(1)
for c in range(0, len(rank)):
    sleep(0.7)
    print(f'{c+1}ºlugar: {rank[c][0]} com {rank[c][1]}')