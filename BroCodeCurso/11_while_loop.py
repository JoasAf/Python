# while loop = Executa um código enquanto uma condição é verdadeira

nome = input('Seu nome: ')

while nome == '':
    print('Você esqueceu de digitar!!')
    nome = input('Seu nome: ')

print(f'Olá {nome}')

comida = input('Comida favorita [Q para sair]: ')

while comida.upper() != 'Q':
    print(comida)
    comida = input('Comida favorita [Q para sair]: ')