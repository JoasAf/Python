cont = 0
while True:
    n = int(input('Quer ver a tabuada de qual número?: '))
    if n < 0:
        break
    print('-'*6,f'TABUADA DO {n}','-'*6)
    while True:
        print(f'{n:2} X {cont:2} = {n*cont:3}')
        if cont == 10:
            cont = 0
            break
        cont+=1
