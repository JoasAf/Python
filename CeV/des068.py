from random import randint
cont = 0
while True:
    computador = randint(0, 10)
    player = int(input('Digite um valor: '))
    total = player+computador
    tipo = str(input('Par ou Ímpar?: ')).upper().strip()[0]
    print(f'Computador: {computador}')
    print(f'Jogador: {player}')
    print('DEU PAR!' if total%2==0 else 'DEU ÍMPAR!')

    if tipo == 'P':
        if total%2==0:
            print('Você ganhou!')
            cont += 1
        else:
            print('Você perdeu!')
            break
    elif tipo == 'I' or tipo == 'Í':
        if total%2==1:
            print('Você ganhou!')
            cont += 1
        else:
            print('Você perdeu!')
            break
print('Você não ganhou nenhuma vez' if cont == 0 else 'Você ganhou 1 vez'
    if cont == 1 else f'Você ganhou {cont} vezes seguidas')
