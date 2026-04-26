nome = input("Digite seu nome completo: ").split()

print('Seu primeiro nome é {} e seu último é {}'.format(nome[0], nome[len(nome)-1-len(nome)]))
