brasileirao = ('Botafogo', 'Palmeiras', 'Flamengo', 'Fortaleza', 'Internacional',
               'São Paulo', 'Corinthians', 'Bahia', 'Cruzeiro', 'Vasco Gama',
               'EC Vitória', 'Atletico Mineiro', 'Fluminense', 'Gremio', 'Juventude',
               'Chapecoense', 'Paranaense', 'Criciúma', 'Goianiense', 'Cuiabá')
print(f'Os 5 primeiros colocados do Brasileirão são {brasileirao[0: 5]}')
print(f'Os 4 últimos colocados do Brasileirão são {brasileirao[-4:]}')
print(f'Os times do Brasileirão em ordem alfabética é : {sorted(brasileirao)}')
print(f'O time Chapecoense está na {brasileirao.index('Chapecoense')+1}ª posição')