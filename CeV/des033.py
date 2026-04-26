n1 = float(input('Digite qualquer número: '))
n2 = float(input('Digite outro número: '))
n3 = float(input('Digite o último número: '))

maior = n1
menor = n1

if n2>n3 and n2>n1:
    maior = n2
if n3>n1 and n3>n2:
    maior = n3
print('O número {} é o maior'.format(maior))

if n2<n3 and n2<n1:
    menor = n2
if n3<n2 and n3<n1:
    menor = n3
print('O número {} é o menor'.format(menor))