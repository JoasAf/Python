dados = dict()
dados['nome'] = str(input('Nome: '))
dados['média'] = float(input(f'Média de {dados['nome']}: '))
if dados['média'] >= 7:
    dados['situação'] = 'aprovado'
elif 5 < dados['média'] < 7:
    dados['situação'] = 'recuperação'
else:
    dados['situação'] = 'reprovado'
for k, v in dados.items():
    print(f'{k}: {v}')