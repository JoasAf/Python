def ficha(nome='<desconhecido>', gols=0):
    """
    ---> Mostra o nome e quant de gols de uma pessoa.

    :param nome: Nome do jogador
    :param gols: Total de Gols
    :return: Retorna str(n) e str(g)
    """
    n = input('Nome do jogador: ')
    g = input('Gols durante o campeonato: ')

    if n != '':
        nome = n
    if g != '':
        gols = g

    print('-'*25)
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato')

ficha()