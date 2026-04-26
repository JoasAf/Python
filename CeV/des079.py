valores = [ ]
while True:
    valor = int(input('Digite um valor: '))
    if valor not in valores:
        valores.append(valor)
        print('Valor adicionado')
    else:
        print('Valor já adicionado na lista!')
    sn = ' '
    while sn not in 'SN':
        sn = input('Quer continuar [S/N]: ').upper().strip()
    if sn == 'N':
        break
print(f'Você digitou os números {sorted(valores)}')