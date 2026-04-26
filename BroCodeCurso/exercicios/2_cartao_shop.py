# Exercício 2 Programa de cartão de shopping

item = input('Item que você vai comprar: ')
preco = float(input(f'Preço de {item}: R$'))
quant = int(input(f'Quantos {item} você vai comprar?: '))

total = preco * quant

print(f'Você comprou {quant} {item} por R${total:.2f}')