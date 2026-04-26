from time import sleep

jogadoratual = dict()
dadosjogadores = list()

while True:
    partidas = list()

    jogadoratual['nome'] = str(input('Nome do jogador: ')).strip()
    jogos = int(input(f'Quantos jogos \33[33m{jogadoratual['nome']}\33[0m jogou?: '))

    while jogos <= 0:
        jogos = int(input(f'\33[31mDigite o núm de jogos que \33[33m{jogadoratual['nome']}\33[31m jogou: \33[0m'))

    for gols in range(0, jogos):
        partidas.append(int(input(f'Gols na {gols+1}ª partida: ')))

    jogadoratual['golsP'] = partidas.copy()
    jogadoratual['golsT'] = sum(partidas)
    dadosjogadores.append(jogadoratual.copy())

    while True:
        sn = str(input('Quer continuar? [S/N]: ')).upper().strip()
        if sn in 'SN':
            break
        print('Responda com S ou N!')
    if sn == 'N':
        break

while True:
    print('_'*42)
    sleep(1)

    print(f'\33[32m{'Cód.':<5} Nome {'Partidas':>18} {'Total':>10}')
    sleep(0.5)

    for cod, jogador in enumerate(dadosjogadores):
        print(f'{cod:<6}', end='')
        sleep(0.3)
        for dado in jogador.values():
            print(f'{str(dado):<15}', end='')
            sleep(0.3)
        print()

    sleep(1)
    print('\33[0m_'*42)

    achou = 0

    det = str(input('\33[37mCód. do jogador para ver detalhes. '
                    '("N" para cancelar): \33[0m')).strip()

    if det.isnumeric():
        for verif in range(0, len(dadosjogadores)):

            if int(det) == verif:
                achou = 1
                print(f'\33[33m{'LEVANTAMENTO JOGADOR:':->35} '
                      f'{dadosjogadores[int(det)]['nome'].upper():-<20}\33[0m')

                for jogo, gols in enumerate(dadosjogadores[int(det)]['golsP']):
                    print(f'{'->':>5} No {jogo+1}º jogo fez \33[34m{gols}\33[0m gols.')

        if achou != 1:
            print('\33[31mJogador não encontrado\33[0m')

    else:
        if det.upper() == 'N':
            break

print(f'\n\33[31m{'Finalizando':-^55}')