from datetime import date
anoatual = date.today().year
maior = 0
menor = 0
for pessoa in range(1, 8):
    nascimento = int(input('Qual ano a {}ª pessoa nasceu?: '.format(pessoa)))
    idade = anoatual-nascimento
    if idade>=21:
        maior += 1
    else:
        menor += 1
print('O total de maioridades é {} e de menoridades é {}'.format(maior, menor))