velho = 0
nomemaisvelho = 'Nenhum homem'
mul20 = 0
soma = 0
media = 0
for pessoas in range(0, 4):
    print('\33[33m='*10,'{}ª pessoa'.format(pessoas+1),'='*10)
    nome = str(input('\33[0mNome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: ')).lower()
    soma += idade
    if sexo == 'homem' and idade>velho:
        velho = idade
        nomemaisvelho = nome
    if sexo == 'mulher' and idade<20:
        mul20 +=1
    media += 1
if nomemaisvelho == 'Nenhum homem':
    print('\33[33m{}'.format(nomemaisvelho))
else:
    print('\33[33mO homem mais velho é o {} com {} anos'.format(nomemaisvelho, velho))
print('Na lista há {} mulheres com menos de 20 anos'.format(mul20))
print('A média de idade das pessoas listadas é de {} anos'.format(soma/media))
