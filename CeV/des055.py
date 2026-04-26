maior = 0
menor = 0
for pessoas in range(0, 5):
    peso = float(input('Qual é o peso da {} pessoa?: Kg'.format(pessoas+1)))
    if pessoas == 0:
        maior = peso
        menor = peso
    else:
        if peso>maior:
            maior = peso
        if peso<menor:
            menor = peso
print('O maior peso foi {:.1f}Kg e o menor foi {:.1f}Kg'.format(maior, menor))
