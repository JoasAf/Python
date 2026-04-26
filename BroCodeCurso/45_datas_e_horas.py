import datetime as dt

data = dt.date(2025, 10, 22)
hoje = dt.date.today()

hora = dt.time(12, 30, 0)
agora = dt.datetime.now()

agora = agora.strftime('%H:%M - %d/%b')

tempo_alvo = dt.datetime(2025, 1, 22, 14, 28, 10)
tempo_atual = dt.datetime.now()

if tempo_alvo < tempo_atual:
    print('A data já passou')
else:
    print('A data ainda Não passou')