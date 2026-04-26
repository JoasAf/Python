# Programa de banco
def programa(funcionando = True):
    import cores as cores

    def opções(*opcs):
        for item in opcs:
            cores.tcor(f'{opcs.index(item) + 1}. \33[33m{item}', 'cian')

    def mostrar_saldo():
        cores.titulos('SALDO ATUAL', cor='verd')
        cores.titulos(f'R${saldo:.2f}', simb=' ')

    def depositar():
        while True:
            valor = float(input('Digite o tanto a depositar: '))

            if valor <= 0:
                cores.tcor('Valor inválido!', 'verm')
                continue

            cores.titulos('DEPOSITANDO', cor='verd', simb='.')
            return valor

    def sacar():
        while True:
            valor = float(input('Digite o tanto a sacar: '))

            if valor <= 0:
                cores.tcor('Valor inválido!', 'verm')
                continue
            elif valor > saldo:
                cores.tcor('Saldo insuficiente!', 'verm')
                continue

            cores.titulos('SACANDO',cor= 'verd', simb='.')
            return valor

    saldo = 0

    while funcionando:
        cores.titulos(' Programa de Banco ', cor='azul')
        opções('Saldo', 'Depositar', 'Sacar', 'Sair')
        escolha = input('Sua escolha: ')

        match escolha:
            case '1' | 'saldo':
                mostrar_saldo()

            case '2' | 'depositar':
                saldo += depositar()
                cores.tcor(f'Saldo atual R${saldo:.2f}', 'verd')

            case '3' | 'sacar':
                saldo -= sacar()
                cores.tcor(f'Saldo atual R${saldo:.2f}', 'verd')

            case '4' | 'sair':
                cores.titulos('SAINDO', 20, 'mage')
                funcionando = False

            case _:
                cores.titulos('OPÇÃO INVÁLIDA', cor='verm')

if __name__ == '__main__':
    programa()