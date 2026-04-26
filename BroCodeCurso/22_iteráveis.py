#             ┌────────────────────────────────────────────────────────────────┐
# Iteráveis = │ Um objeto/coleção que pode retornar seus elementos um por vez, │
#             │ permitindo que seja iterado em um loop.                        │
#             └────────────────────────────────────────────────────────────────┘

números = ['1', '2', '3', '4', '5']

for item in reversed(números):
    print(item, end= ' │ ')
print('\n')


países = ('Brasil', 'México', 'Japão', 'Alemanha')

for item in reversed(países):
    print(item, end=' │ ')
print('\n')


frutas = {'Banana', 'Maça', 'Pera', 'Abacaxi', 'Laranja'}

for item in frutas:
    print(item, end=' │ ')
print('\n')


capitais = {'Argentina':'Buenos Aires',
            'Brasil':'Brasília',
            'Japão':'Tóquio'}

for key, value in capitais.items():
    print(f'{key}: {value}', end=' │ ')