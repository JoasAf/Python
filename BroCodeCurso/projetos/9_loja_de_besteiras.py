# Loja de besteiras

cardapio = {'pipoca':1, 'hot-dog':2,
             'pretzel':2, 'bala': 0.5,
             'refri':3, 'água':1.5,
            'salgadinho':5, 'pizza':12}

carrinho = []
total_compra = 0


print(f'{"LOJINHA":=^32}')

for k, v in cardapio.items():
    print(f'{k.upper():-<24}R${v:.2f}')

print('-'*30)

while True:

    compra = input('Comprar ["S" para sair]: ').strip().lower()

    if compra == 's':
        break

    elif not cardapio.get(compra):
        print(f'Desculpe, {compra} não está no cardápio..')
        continue

    carrinho.append(compra)
    total_compra += cardapio.get(compra)
    print('Adicionado ao carrinho!')


print(f'{"TOTAL":=^32}')

for compra in carrinho:
    print(f'{compra:-<24}R${cardapio.get(compra):.2f}')

print(f'Total da compra: R${total_compra:.2f}')