listamae = []
listapar = []
listaimpar = []
while True:
    valor = int(input('Digite um valor: '))
    listamae.append(valor)
    if valor % 2 == 0:
        listapar.append(valor)
    else:
        listaimpar.append(valor)
    sn = ' '
    while sn not in 'SN':
        sn = input('Quer continuar?[S/N]: ').upper().strip()
    if sn == 'N':
        break
print(f'Lista: {listamae}')
print(f'Lista par: {listapar}')
print(f'Lista ímpar: {listaimpar}')
