def titulos(texto, tam = 30, cor='\33[m', simb='-', negrito='n', end='\n'):
    match cor, negrito:
        case 'verm', 'n':
            cor = '\33[31m'
        case 'verd', 'n':
            cor = '\33[32m'
        case 'amar', 'n':
            cor = '\33[33m'
        case 'azul', 'n':
            cor = '\33[34m'
        case 'mage', 'n':
            cor = '\33[35m'
        case 'cian', 'n':
            cor = '\33[36m'
        case 'cinz', 'n':
            cor = '\33[37m'

        case 'verm', 's':
            cor = '\33[1:31m'
        case 'verd', 's':
            cor = '\33[1:32m'
        case 'amar', 's':
            cor = '\33[1:33m'
        case 'azul', 's':
            cor = '\33[1:34m'
        case 'mage', 's':
            cor = '\33[1:35m'
        case 'cian', 's':
            cor = '\33[1:36m'
        case 'cinz', 's':
            cor = '\33[1:37m'

    print(cor, end='')
    print(simb * ((tam//2)-(len(texto)//2)),end='')
    print(texto, end='')
    print(simb * ((tam//2)-(len(texto)//2)),end='')
    print('\33[m', end=end)

def tcor(texto, cor='\33[m'):
    match cor:
        case 'verm':
            cor = '\33[31m'
        case 'verd':
            cor = '\33[32m'
        case 'amar':
            cor = '\33[33m'
        case 'azul':
            cor = '\33[34m'
        case 'mage':
            cor = '\33[35m'
        case 'cian':
            cor = '\33[36m'
        case 'cinz':
            cor = '\33[37m'
    print(f'{cor}{texto}\33[m')