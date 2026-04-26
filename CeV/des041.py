from datetime import date
ano = int(input('Digite seu ano de nascimento: '))
if date.today().year-ano<=9:
    print('Categoria Mirim')
elif date.today().year-ano<=14:
    print('Categoria Infantil')
elif date.today().year-ano<=19:
    print('Categoria Junior')
elif date.today().year-ano<=25:
    print('Categoria Sênior')
else:
    print('Categoria Master')
