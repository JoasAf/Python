'''from math import factorial
n = int(input('Digite um número inteiro: '))
print('O fatorial de {} é {}'.format(n, factorial(n)))'''
n = int(input('Digite um número inteiro: '))
a = n
f = 1
while n != 1:
    f*= n
    n-=1
print('O fatorial de {} é {}'.format(a, f))