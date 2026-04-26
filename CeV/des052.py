p = 0
n = int(input('Digite um número inteiro: '))
for c in range(1, n+1):
    if n%c==0:
        p += 1
        print('\33[33m', end= '')
    else:
        print('\33[0m', end= '')
    print(c, end=' ')
if p == 2:
    print('\n\33[32m{} é um número primo! Ele foi dívisivel {} vezes'.format(n, p))
else:
    print('\n\33[31m{} não é um número primo! Ele foi dívisivel {} vezes'.format(n, p))