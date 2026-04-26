total = contT = cont1000 = menorP = 0
nomeB = ''
print('\33[33m*'*3, 'COMPRAS JOJA\'s', '*'*3)
while True:
    contT += 1
    sn = ''
    print('\33[36m>'*5,f'PRODUTO {contT}', '<'*5)
    nome = input('\33[34mDigite o nome do produto: ')
    preco = float(input('\33[33mDigite o preço do produto: R$'))
    total += preco
    if contT == 1 or preco < menorP:
        nomeB = nome
        menorP = preco
    if preco > 1000:
        cont1000 +=1
    while sn != 'S' and sn != 'N':
        sn = input('\33[37mQuer continuar? [S/N]:').upper()
    if sn == 'N':
        break
print(f'''\33[32mVocê comprou {contT} produtos.
Sendo {cont1000} mais caros do que R$1000,00.
O mais barato sendo {nomeB}, custando R${menorP:.2f}.
A compra saiu no total R${total:.2f}''')