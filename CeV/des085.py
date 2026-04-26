paim = [[], []]
for c in range(0, 7):
    num = int(input(f'Digite o {c+1}º valor: '))
    if num%2==0:
        paim[0].append(num)
    else:
        paim[1].append(num)
paim[0].sort()
paim[1].sort()
print(f'Os números pares digitados em ordem são {paim[0]}')
print(f'Os números ímpares digitados em ordem são {paim[1]}')
