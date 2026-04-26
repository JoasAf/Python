def leiaDinheiro(txt):
    while True:
        resp = input(txt).replace(',','.').strip()
        if resp.replace('.', '').isnumeric():
            return float(resp)
        print(f'\33[31mERRO, "{resp}" não é um preço válido!\33[0m')


def leiaInt(txt):
    while True:
        try:
            num = input(txt).strip()
            int(num)
        except (TypeError, ValueError):
            print('\33[31mERRO, digite um número inteiro\33[m')
            continue
        except KeyboardInterrupt:
            print('\n\33[31mO usuário decediu não digitar esse número.\33[m')
            return 0
        else:
            print(f'O valor digitado foi {num}')
            return num

def leiaFloat(txt):
    while True:
        try:
            num = input(txt).strip()
            float(num)
        except (TypeError, ValueError):
            print('\33[31mERRO, digite um número real\33[m')
            continue
        except KeyboardInterrupt:
            print('\n\33[31mO usuário decediu não digitar esse número.\33[m')
            return 0
        else:
            print(f'O valor digitado foi {num}')
            return num
