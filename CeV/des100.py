from random import randint
from time import sleep
lista = list()

def sorteia():
    print('Sorteando 5 valores da lista: ', end=' ')

    for n in range(0, 5):
        sleep(0.3)
        lista.append(randint(1, 10))
        print(lista[n], end=', ')
    print('PRONTO!')

def somapar():
    soma = 0
    print('Somando os valores pares da lista:==', end= ' ')

    for n in lista:
        if n%2==0:
            soma += n
            print(n, end=' ')
    print(f'temos {soma}')


sorteia()
somapar()
