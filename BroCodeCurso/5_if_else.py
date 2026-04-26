# if = faz alguma coisa apenas se (if) alguma coisa for verdadeira
#      senão (else) faz outra coisa

idade = int(input('Digite sua idade: '))

if 100 > idade >= 18:
    print('Você foi inscrito!')
elif idade < 0:
    print('Você nem nasceu ainda!')
elif idade >=100:
    print('Você está muito velho para se inscrever!')
else:
    print('Você precisa ter 18 anos para se inscrever!')

print('-'*40)

resposta = input('Você quer comer? [S/N]: ')

if resposta == 'S':
    print('Toma comida!')
else:
    print('Sem comida pra você!')

print('-'*40)

nome = input('Digite seu nome: ')

if nome == '':
    print('Você não digitou nada!')
else:
    print(f'Olá {nome}')

print('-'*40)

a_venda = True

if a_venda:
    print('Esse item está à venda!')
else:
    print('Esse item não está à venda!')

print('-'*40)

online = False

if online:
    print('O usuário está online!')
else:
    print('O usuário está offline!')