n = int(input('Escolha qualquer número inteiro: '))
e = int(input('Digite o correspondente número para escolher uma conversão:\n'
          'Binário [1]\n'
          'Octal [2]\n'
          'Hexadecimal [3]\n'))
if e == 1:
    print('{} convertido para binário é \33[33m{}'.format(n, bin(n)[2:]))
elif e == 2:
    print('\33[0m{} convertido para octal é \33[33m{}'.format(n, oct(n)[2:]))
elif e == 3:
    print('\33[0m{} convertido para hexadecimal é \33[33m{}'.format(n, hex(n)[2:]))
else:
    print('\33[31mVocê digitou um número que não corresponde com as opções anteriores!')