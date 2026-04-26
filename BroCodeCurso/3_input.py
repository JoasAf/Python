# input() = É uma função que deixa o usuario colocar dados.
#           Retorna os dados como uma string

nome = input('Qual é seu nome?: ')
idade = int(input('Quantos anos você tem?: '))

idade += 1

print(f'Olá {nome}!')
print('FELIZ ANIVERSÁRIO')
print(f'Você tem {idade} anos')