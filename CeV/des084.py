pep = [[], [], [], []]
cont = 0
while True:
    cont += 1
    sn = ' '
    print(f'{'CADASTRO':-^20}')
    nome = input('Nome: ')
    peso = float(input('Peso: '))

    if cont == 1:
        pep[0].append(nome)
        pep[1].append(peso)
        pep[2].append(nome)
        pep[3].append(peso)
    else:
        if peso < pep[1][0]:
            del(pep[1][0:], pep[0][0:])
            pep[0].append(nome)
            pep[1].append(peso)

        elif peso > pep[3][0]:
            del(pep[2][0:], pep[3][0:])
            pep[2].append(nome)
            pep[3].append(peso)

        elif peso == pep[1][0]:
            pep[0].append(nome)
            pep[1].append(peso)

        elif peso == pep[3][0]:
            pep[2].append(nome)
            pep[3].append(peso)
    while sn not in 'SN':
        sn = input('Quer continuar?[S/N]: ').upper().strip()
    if sn == 'N':
        break
print(pep)
print(f'Pessoas cadastradas: {cont}')
print(f'Menor peso foi {pep[1][0]}kg de {pep[0]}')
print(f'Maior peso foi {pep[3][0]}kg de {pep[2]}')
