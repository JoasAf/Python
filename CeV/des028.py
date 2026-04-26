from random import randint

n = randint(1,3)
print('Estou pensando em um número de 1 a 3...')
e = int(input('Tente acertar o número: '))
if e == n:
    print('\nO número era {}'.format(n))
    print('Você me venceu.. Desta vez!')
else:
    print('\nO número era {}'.format(n))
    print('Você errou!')
