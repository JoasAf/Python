# Conversor de temperatura em python

unidade = input('Celsius ou Fahrenheit? [C/F]: ')
temp = float(input(f'Digite uma temperatura em {unidade}: '))

if unidade == 'C':
    conversao = temp * 1.8 + 32
    print(f'{temp}Cº são {conversao}Fº')
elif unidade == 'F':
    conversao = (temp - 32) * 5 / 9
    print(f'{temp}Fº são {conversao}Cº')
else:
    print(f'{unidade} não é uma unidade válida!')