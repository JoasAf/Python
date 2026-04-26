# Calculadora em python

operador = input('Escohla um operador [+-*/]: ')
n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))

if operador == '+':
    t = n1+n2
    print(f'O total é {t:.2f}')
elif operador == '-':
    t = n1-n2
    print(f'O total é {t:.2f}')
elif operador == '*':
    t = n1*n2
    print(f'O total é {t:.2f}')
elif operador == '/':
    t = n1/n2
    print(f'O total é {t:.2f}')
else:
    print(f'{operador} não é um operador válido!')