itens = ('Pão', 6.90, 'Leite', 3.8,
         'Açucar', 3.50, 'Dúzia de Ovos', 13.90,
         'Lápis', 1.40, 'Borracha', 0.80,
         'Caderno', 6.20, 'Mochila', 34.90,
         'Apontador', 2.50, 'Mouse Gamer', 99.90)
print('_'*40)
print(f'{'TABELA DE PREÇOS':^40}')
print('-'*40)
for nomes in range(0, len(itens), 2):
    print('|{:.<30}'.format(itens[nomes]),end='R${:>6.2f}|\n'.format(itens[nomes+1]))
print('_'*40)
