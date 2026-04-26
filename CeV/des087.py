matriz = [[], [], [],
          [], [], [],
          [], [], []]
q = 3
somapar = 0
maior = 0
for c in range(0, 9):
    if c<3:
        matriz[c].append(int(input(f'Digite o valor pra posição {c-c}:{c}: ')))
    elif c<6:
        matriz[c].append(int(input(f'Digite o valor pra posição {c-(c-1)}:{c-3}: ')))
    else:
        matriz[c].append(int(input(f'Digite o valor pra posição {c-(c-2)}:{c-6}: ')))
print('-=-'*10)
for c in range(0, 9):
    if c == q:
        q+=3
        print()
    print(f'[{matriz[c][0]:^5}]', end='')
    if matriz[c][0]%2==0:
        somapar += matriz[c][0]
print('\n','-=-'*10)
if matriz[3][0]>matriz[4][0] and matriz[3][0]>matriz[5][0]:
    maior = matriz[3][0]
elif matriz[4][0]>matriz[3][0] and matriz[4][0]>matriz[5][0]:
    maior = matriz[4][0]
else:
    maior = matriz[5][0]
somaterc = matriz[2][0]+matriz[5][0]+matriz[8][0]
print(f'A soma dos números pares é {somapar}')
print(f'A soma dos números da terceira coluna é {somaterc}')
print(f'O maior número da segunda linha é {maior}')