from datetime import date
g = input('Você é mulher ou homem?: ').lower()
if 'r' in g:
    print('Certo, pode ir passando')
else:
    ano = int(input('Qual ano você nasceu garoto?: '))
    if date.today().year-ano > 18:
        print('Já passou {} anos do prazo de alistamento para você. Seu alistamento foi em {}'.format(date.today().year-ano-18, ano+18))
    elif date.today().year-ano == 18:
        print('Ha! Está na hora do seu alistamento! Venha cá garoto!')
    elif date.today().year-ano <18:
        print('Você ainda não está maduro o suficiente.. Nos vemos daqui {} ano(s) em {}.'.format(ano-date.today().year+18, ano+18))
