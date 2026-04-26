def leiaOpc(txt, tamLista):
    while True:
        try:
            n = input(txt)
            n = int(n)
        except (ValueError, TypeError):
            print('\33[31mERRO, digite um número inteiro!\33[m')
            continue
        except KeyboardInterrupt:
            print('\33[33mO usuário saiu do programa\33[m')
            return 3
        else:
            if tamLista >= n > 0:
                return n
            else:
                print('\33[31mERRO, escolha uma opção válida!\33[m')


def leiaInt(txt):
    while True:
        try:
            num = input(txt).strip()
            int(num)
        except (TypeError, ValueError):
            print('\33[31mERRO, digite um número inteiro!\33[m')
            continue
        except KeyboardInterrupt:
            print('\33[33mO usuário não digitou a idade.\33[m')
            return 0
        else:
            return num


def arqExis(txt):
    try:
        arq = open(txt, 'rt')
        arq.close()
    except FileNotFoundError:
        arq = open(txt, 'w')
        arq.close()
        print(f'arquivo {txt} criado com sucesso')
