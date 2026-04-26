def fatorial(num=0, mostra = True):
    """
    --->Calcula o fatorial de um número, mostrando ou não o cálculo.

    :param num: O número a ser calculado o fatorial
    :param mostra: (OPCIONAL) Mostrar ou não o cálculo
    :return: Valor do fatorial do número num
    """
    f = 1

    print('-'*25)

    if num < 0:
        print('Números negativos não tem fatoriais!')

    else:
        if mostra:
            for n in range(num, 0, -1):
                f *= n
                print(f'{n}', end=' X ' if n > 1 else ' = ')


        else:
            for n in range(num, 0, -1):
                f *= n
    return f


nu = int(input('Digite um número: '))
print('Ver processo de cálculo do fatorial?')
ver = bool(input('Deixe em branco para NÃO: '))
print(fatorial(nu, ver))
