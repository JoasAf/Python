valores = []
while True:
    valores.append(int(input('Digite um valor: ')))
    valores.sort(reverse=True)
    sn = ' '
    while sn not in 'SN':
        sn = input('Quer continuar?[S/N]: ').upper().strip()
    if sn == 'N':
        break
print(f'Você digitou {len(valores)} valores')
print('O número 5 está na lista' if 5 in valores else 'O número 5 não está na lista')
print(f'A ordem decrescente da lista é {valores}')