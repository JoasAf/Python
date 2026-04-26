from datetime import date
dados = dict()
dados['Nome'] = str(input('Nome: '))
dados['Idade'] = date.today().year - int(input('Ano de nascimento: '))
dados['CTPS'] = int(input('Carteira de Trabalho: '))
if dados['CTPS'] != 0:
    dados['Contratação'] = int(input('Ano de contratação: '))
    dados['Salário'] = float(input('Salário: R$'))
    dados['Aposentadoria'] = dados['Contratação']+35  + dados['Idade'] - date.today().year
for k, v in dados.items():
    print(f'{k}: {v:}')