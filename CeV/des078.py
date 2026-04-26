listanum = []
maior = menor = 0
for c in range(0, 5):
    listanum.append(int(input(f'Digite o valor da {c}ª posição: ')))
    if c == 0:
        menor = maior = listanum[0]
    else:
        if listanum[c]>maior:
            maior = listanum[c]
        if listanum[c]<menor:
            menor = listanum[c]
print('-=-'*14)
print(f'O maior valor é o {maior} na posições', end=' ')
for i in range(0, len(listanum)):
    if listanum[i] == maior:
        print(f'{listanum.index(maior, i)}', end='...')

print(f'\nO menor valor é o {menor} nas posições', end=' ')
for i in range(0, len(listanum)):
    if listanum[i] == menor:
        print(f'{listanum.index(menor, i)}', end='...')
