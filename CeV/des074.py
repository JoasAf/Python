from random import randint
n = (randint(0, 9), randint(0, 9), randint(0, 9),
     randint(0, 9), randint(0, 9))
print(f'Números sorteados: {n}')
print(f'Menor número sorteado: {sorted(n)[0]}')
print(f'Maior número sorteado: {sorted(n)[-1]}')
