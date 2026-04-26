matriz = [[], [], [],
          [], [], [],
          [], [], []]
q = 3
for c in range(0, 9):
    if c<3:
        matriz[c].append(int(input(f'Digite o valor pra posição {c-c}:{c} -> ')))
    elif c<6:
        matriz[c].append(int(input(f'Digite o valor pra posição {c-(c-1)}:{c-3} -> ')))
    else:
        matriz[c].append(int(input(f'Digite o valor pra posição {c-(c-2)}:{c-6} -> ')))
for c in range(0, 9):
    if c == q:
        print()
        q+=3
    print(f'[{matriz[c][0]:^5}]', end='')