from time import sleep
ptermo = int(input('\33[33mDigite o 1º termo da PA: '))
razao = int(input('Digite a razão da PA: '))
pausa = 10
cont = 0
while cont < pausa:
    print('\33[34m{}'.format(ptermo+(cont*razao)), end=' > ')
    cont += 1
    if cont == pausa:
        print('\33[33m[PAUSA]')
        sleep(0.5)
        print('\33[36mVocê quer mais termos? [S/N]')
        resp = str(input('')).upper()
        while resp not in 'SN':
                print('\33[36mDigite [S] ou [N]: ')
                resp = str(input('')).upper()
        if resp in 'S':
            pausa += int(input('\33[36mQuantos?: '))
        elif resp in 'N':
            print('Termos mostrados: {}'.format(pausa))
            pausa = 0

print('\33[1:31m-'*6,'Terminado', '-'*6)