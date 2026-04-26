matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = maior = ster = 0

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor pra  [{l}, {c}]: '))
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^3}]', end='')
        if matriz[l][c] % 2 == 0:
            spar+=matriz[l][c]
        if c == 2:
            ster += matriz[l][c]
        if l == 1:
            if c == 0:
                maior = matriz[l][c]
            else:
                if matriz[l][c]>maior:
                    maior = matriz[l][c]
    print()
print(f'A soma dos números pares é {spar}')
print(f'A soma dos números da terceira coluna é {ster}')
print(f'O maior número da segunda linha é {maior}')
