from time import sleep

def escreva(txt, cor):
    print(cor, end='')
    print('~'*(len(txt)+2))
    print(f' {txt}')
    print('~'*(len(txt)+2))


while True:
    escreva('SISTEMA DE AJUDA INTELIGENTE PYJOJO', '\33[0:30:42m')
    f = input('\33[0mDigite uma função ou biblioteca: ').lower().strip()
    if f == 'fim':
        escreva('ATÉ LOGO!!', '\33[7:31:40m')
        break
    sleep(0.7)
    escreva(f'PESQUISANDO O MANUAL DE "{f}"', '\33[30:44m')
    print('\33[7:37:40m', end='')
    sleep(1)
    help(f)
    sleep(1)