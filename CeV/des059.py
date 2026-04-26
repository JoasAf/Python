from time import sleep
n1 = int(input('\33[33mDigite o 1º número: '))
n2 = int(input('Digite o 2º número: '))
opcao = 0
opcao2 = ''

while opcao != '5':
    print('\33[0:34m-'*6,'OPÇÕES','-'*6)
    sleep(0.3)
    print('''\33[34m    [1] Somar
    [2] Multiplicar
    [3] O Maior
    [4] Novos números
    [5] Sair do programa''')
    print('\33[32mNúmeros escolhidos: {} e {}'.format(n1, n2))
    sleep(0.3)
    opcao = input('\33[33mOpção: ')

    sleep(0.3)

    if opcao == '1':
        print('\33[35m{} + {} = {}'.format(n1, n2, n1+n2))
        sleep(0.3)
        while opcao2 != 'S' and opcao2 != 'N':
            print('\33[36mDeseja continuar a usar o programa? [S/N]')
            sleep(0.3)
            opcao2 = input('\33[33mOpção: ').upper()
        if opcao2 == 'N':
            sleep(0.3)
            opcao = '5'

    if opcao == '2':
        print('\33[35m{} X {} = {}'.format(n1, n2, n1*n2))
        sleep(0.3)
        while opcao2 != 'S' and opcao2 != 'N':
            print('\33[36mDeseja continuar a usar o programa? [S/N]')
            sleep(0.3)
            opcao2 = input('\33[33mOpção: ').upper()
        if opcao2 == 'N':
            sleep(0.3)
            opcao = '5'

    if opcao == '3':
        if n1 > n2:
            print('\33[35m{} é o maior'.format(n1))
        elif n2 > n1:
            print('\33[35m{} é o maior'.format(n2))
        else:
            print('\33[35m{} e {} são iguais'.format(n1, n2))
        sleep(0.3)
        while opcao2 != 'S' and opcao2 != 'N':
            print('\33[36mDeseja continuar a usar o programa? [S/N]')
            sleep(0.3)
            opcao2 = input('\33[33mOpção: ').upper()
        if opcao2 == 'N':
            opcao = '5'

    if opcao == '4':
        print('\33[35m-'*25)
        n1 = float(input('\33[33mDigite o novo 1º número: '))
        n2 = float(input('Digite o novo 2º númeto: '))

    elif opcao2 not in 'NS' or opcao not in '5':
        print('\33[31mDigite uma opção abaixo')
    opcao2 = ''
print('\33[1:31m-'*8,'Saindo', '-'*8)