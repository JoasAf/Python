from time import sleep

def maior(*num):
    cont = mai = 0

    print('=-'*20)
    print('Analisando os valores passados...')
    sleep(0.7)
    for n in num:
        if cont == 0:
            mai = n
        else:
            if n > mai:
                mai = n
        cont += 1
        print(n, end=' ')
        sleep(0.1)
    sleep(0.7)
    print(f'\nForam informados {len(num)} valores.')
    sleep(0.7)
    print(f'O maior valor foi {mai}.')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior(-10, -1)