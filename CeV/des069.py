cont = maior18 = homens = mulheresmenor20 = 0
while True:
    sn = ' '
    sexo = ' '
    cont += 1
    print('-'*5,f'{cont}º CADASTRO','-'*5)
    idade = int(input('Idade: '))
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).upper()
        if idade > 18:
            maior18 += 1
        if sexo in 'M':
            homens += 1
        if sexo in 'F' and idade < 20:
            mulheresmenor20 += 1
    while sn not in 'SN':
        sn = input('Quer continuar? [S/N]: ').upper()
    if sn in 'N':
            break
print(f'''
    Você cadastrou {cont} pessoas.
    Sendo {maior18} delas maior de 18 anos.
    {homens} homens.
    E {mulheresmenor20} mulheres com menos de 20 anos.''')
