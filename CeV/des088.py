from random import  sample
from time import sleep
nums = []
jogos = int(input('Quantos jogos você quer que eu sorteie?: '))
print(f'{'SORTEANDO':-^30}')
sleep(1)
for c in range(0, jogos):
    nums.append(sorted(sample(range(1, 61), 6)))
    print(f'Jogo {c+1}: {nums[c]}')
    sleep(0.7)
print(f'{'< BOA SORTE >':-^30}')