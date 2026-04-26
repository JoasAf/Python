#Caça Níqueis em Python
def sorteia():
    simbolos = ['🔔', '🍉', '🍒', '⭐', '🍋']

    from random import randint as rdt

    return [simbolos[rdt(0, 4)] for _ in range(3)]

def print_linha(linha):
    print('*'*32)
    print('    |    '.join(linha).center(30))
    print('*'*32)

def recompensa(linha, aposta):
    if linha[0] == linha[1] and linha[1] == linha[2]:
        match linha[0]:
            case '🍒':
                return aposta*2
            case '🍋':
                return aposta*5
            case '🍉':
                return aposta*10
            case '🔔':
                return aposta*25
            case '⭐':
                return aposta*50
    return 0

def main():

    saldo = 1000

    print('Jogo do Bixo'.center(35))
    print('Símbolos: 🍒 🍋 🍉 🔔 ⭐ '.center(33))

    while saldo > 0:
        print(f'\33[32mSeu saldo: R${saldo:.2f}\33[m')

        aposta = input('Sua aposta: R$')

        if not aposta.isdigit():
            print('\33[31mDigite um valor válido\33[m')
            continue

        aposta = float(aposta)

        if aposta <= 0:
            print('\33[31mDigite um valor maior que zero\33[m')
            continue

        if aposta > saldo:
            print('\33[31mSaldo insuficiente\33[m')
            continue

        linha = sorteia()

        print_linha(linha)

        mult = recompensa(linha, aposta)

        if mult != 0:
            print('\33[36mGanhou!\33[m')
            print(f'R${saldo:.2f} + R${mult:.2f}')
            saldo += mult

        else:
            print('\33[31mPerdeu!\33[m')
            print(f'R${saldo:.2f} - R${aposta:.2f}')
            saldo -= aposta

        sn = input('\33[33mQuer continuar? [S/N]: \33[m')

        if sn.upper() == 'N':
            break

    print(f'\33[35mSaldo final: R${saldo:.2f}')

if __name__ == '__main__':
    main()
