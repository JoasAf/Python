jogador = dict()
partida = list()

jogador['nome'] = str(input('Nome do jogador: '))
QuantPart = int(input(f'Quantas partidas {jogador['nome']} jogou?: '))

for gols in range(0, QuantPart):
    partida.append(int(input(f'Gols na {gols+1}ª partida: ')))

jogador['gols'] = partida.copy()
jogador['total'] = sum(partida.copy())

print('_'*35)

print(jogador)

print('_'*35)

for k, v in jogador.items():
    print(f'O campo {k} tem valor {v}')

print('_'*35)

print(f'O jogador {jogador['nome']} jogou {len(partida)} partidas.')
for jogo, gols in enumerate(jogador['gols']):
    print(f'{'-> ':>5}Na {jogo+1}ª partida fez {gols} gols.')
print(f'Totalizando {jogador['total']} gols.')
