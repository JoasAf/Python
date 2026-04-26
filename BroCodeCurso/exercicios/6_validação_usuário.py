# Exercício 6 validação de nome de usuário
# 1 - Não pode passar de 12 caracteres
# 2 - Não pode ter espaços
# 3 - Não pdoe ter números

nome = input('Nome de usuário: ')

if len(nome) > 12:
    print('Não pode passar de 12 caracteres!')

elif nome.count(' ') != 0:
    print('Não pode ter espaços!')

elif not nome.isalpha():
    print('Não pode ter números!')

else:
    print(f'Olá {nome}')