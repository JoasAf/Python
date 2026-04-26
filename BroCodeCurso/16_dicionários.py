# dicionário = é uma coleção de {key:valor}
#              ordenado e mútavel. Sem valores duplos

capitais = {'Brasil':'Brasília',
            'Rússia':'Moscou',
            'Japão':'Tóquio',
            'França':'Paris'}

# print(dir(capitais))
# print(help(capitais))

# print(capitais.get('Brasil'))

# if capitais.get('Argentina'):
#     print('Essa capital existe')
# else:
#     print('Essa capital não existe')

# capitais['Brasil'] = 'Berlim'
# capitais.update({'Brasil': 'Venezuela'}) dá também

# capitais.pop('Japão')
# capitais.popitem()

# keys = capitais.keys()
# valores = capitais.values()
# print(keys, valores)

for k, v in capitais.items():
    print(f'{k}: {v}')