n = (int(input('Digite um valor: ')),
     int(input('Digite um valor: ')),
     int(input('Digite um valor: ')),
     int(input('Digite um valor: ')))
print(f'O número 9 apareceu {n.count(9)} vezes')
if 3 in n:
    print(f'O número 3 apareceu na {n.index(3)+1}º posição')
else:
    print('O número 3 não foi digitado nenhuma vez.')
print(f'Os números pares foram', end= ' ')
for c in n:
    if c%2==0:
        print(c, end=' ')