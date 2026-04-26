cont = repet = 0
parar = 5
menorv = maiorv = 0
media = 0

while repet<parar:
    n = float(input('\33[33mDigite um número: '))
    media += n
    cont += 1
    repet += 1

    if repet == 1:
        maiorv = menorv = n
    if maiorv < n:
        maiorv = n
    if menorv > n:
        menorv = n

    if repet == parar:
        print('\33[33mA média dos valores que você digitou foi {:.2f}'.format(media/cont))
        print('O maior valor digitado foi {}'.format(maiorv))
        print('O menor valor digitado foi {}'.format(menorv))
        escol = ' '
        while escol not in 'SN':
            escol = input('\33[36mVocê deseja continuar? [S/N]: ').upper()
            if escol in 'SN':
                if escol == 'S':
                    parar += 5
                if escol == 'N':
                    parar = 0
print('\33[31mCabou!')