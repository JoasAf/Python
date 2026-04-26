nome = input('Qual é seu nome completo?: ')
print('Seu nome maiúsculo: {}\n'
      'Seu nome minúsculo: {}\n'
      'Quantidade de letras em seu nome: {} letras\n'
      'Quantidade de letras em seu 1º nome: {} letras'.format(nome.upper(),nome.lower(),
                                                              len(nome)-nome.count(' '), len(nome.split()[0])))
