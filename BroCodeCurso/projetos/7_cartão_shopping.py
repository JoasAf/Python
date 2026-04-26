# Programa de cartão de shopping

comidas = []
preços = []

while True:
    preço = 0

    comida = input('Comida [Q para sair]: ').strip()

    if comida.upper() == 'Q':
        break
    elif comida == '':
        continue

    while preço <= 0:
        preço = float(input('Preço: '))

    comidas.append(comida)
    preços.append(preço)

total = sum(preços)

for compra in range(0, len(comidas)):
    print(f'{comidas[compra]:_<20}', end='')
    print(f'R${preços[compra]:>076.2f}')

print('-'*29)
print(f'{"Total":_<20}R${total:>07.2f}')
