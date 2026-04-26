ptermo = int(input('Digite o 1º termo da PA: '))
razao = int(input('Digite a razão da PA: '))
for c in range(0, 10):
    print('{}'.format(ptermo+(razao*c)), end=' → ')
print('Fim')