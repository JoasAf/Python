from random import randint
from time import sleep
dic = dict()
lista = list()
print('Valores sorteados:')
for c in range(0, 4):
    dic['Jogador'] = c+1
    dic['tirou'] = randint(0, 6)
    if c == 0:
        lista.append(dic.copy())
    else:
        if  dic['tirou'] > lista[0]['tirou']:
            lista.insert(0, dic.copy())
        elif dic['tirou']<= lista[-1]['tirou']:
            lista.append(dic.copy())
        else:
            cont = 0
            while True:
                if dic['tirou'] > lista[cont]['tirou']:
                        lista.insert(cont, dic.copy())
                        break
                else:
                    cont+=1
    sleep(0.7)
    print(f'Jogador {dic['Jogador']} tirou {dic['tirou']}')
sleep(1)
for l in range(0, 4):
    sleep(0.5)
    print(f'{l+1}º lugar: Jogador {lista[l]['Jogador']} com {lista[l]['tirou']}')