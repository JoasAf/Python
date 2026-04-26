print('\33[34m='*15, '\n| \33[35mBANCO JOJO\'s \33[34m|\n', '='*15)

valor = int(input('\33[33mQuantidade a ser sacada: R$'))

saque = valor
ced = 200
tced = 0

while True:
    if saque>=ced:
        tced += 1
        saque-=ced
    else:
        if tced > 0:
            print(f'\33[32mTotal de {tced} cédulas de R${ced}')
        if ced == 200:
            ced = 100
        elif ced == 100:
            ced = 50
        elif ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 5
        elif ced == 5:
            ced = 1
        tced = 0
        if saque == 0:
            break