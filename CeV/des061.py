ptermo = int(input('Digite o 1º termo da PA: '))
razao = int(input('Digite a razão da PA: '))
termo = 0
while termo < 10:
    print('{}'.format(ptermo+(termo*razao)), end=' → ')
    termo+=1
print('Fim')