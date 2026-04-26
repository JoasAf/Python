n = 0
soma = 0
cont = 0
while n != 999:
    n = int(input('Digite um número!: '))
    if n != 999:
        soma += n
        cont += 1
print('Você digitou {} digitos e a soma deles foi {}!'.format(cont, soma))
