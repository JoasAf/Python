lista = list()
dicio = dict()
media = 0

while True:

    dicio['nome'] = str(input('Nome: ')).strip()
    dicio['sexo'] = ' '

    while dicio['sexo'] not in 'MF':
        dicio['sexo'] = str(input('Sexo: [M/F] ')).upper().strip()

    dicio['idade'] = int(input('Idade: '))
    sn = ' '

    while sn not in 'SN':
        sn = str(input('Quer continuar? [S/N]: ')).upper().strip()

    media += dicio['idade']
    lista.append(dicio.copy())

    if sn == 'N':
        break

media /= len(lista)

print('_'*35)

print(f'O número de pessoas cadastradas foi {len(lista)}.')
print(f'A média de idade das pessoas cadastradas foi {media}.')
print(f'As mulheres cadastradas foram:',end=' ')

for mulher in range(0, len(lista)):
    if lista[mulher]['sexo'] == 'F':
        print(lista[mulher]['nome'], end='. ')

print('\nAs pessoas acima da média foram:')

for acima in range(0, len(lista)):
    if lista[acima]['idade'] > media:
        print(f'Nome: {lista[acima]['nome']}; Sexo: {lista[acima]['sexo']}'
              f' ; Idade: {lista[acima]['idade']}')
