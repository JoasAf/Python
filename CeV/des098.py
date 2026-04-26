from time import sleep

def contador(i, f, p):

    if p == 0:
        p = 1

    print('-='*20)

    print(f'Contagem de {i} até {f} de {abs(p)} em {abs(p)}.')

    print('-='*20)

    if i > f:

        while True:

            sleep(0.3)
            print(i, end=' ')
            i -= abs(p)

            if i < f:
                break
    else:

        while True:

            sleep(0.3)
            print(i, end=' ')
            i += abs(p)

            if i > f:
                break

    print('FIM!')


contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é sua vez de personalizar a contagem!')
contador(int(input('Início: ')),
         int(input('Fim: ')),
         int(input('Passo: ')))