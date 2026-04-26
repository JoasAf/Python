# Conversor de peso em python

peso = float(input('Escolha um peso: '))
unidade = input('Converter pra Kilogramas ou Libras? [K/L]: ')

if unidade == 'K':
    conversao = peso * 0.4536
    print(f'{peso} libras são {conversao:.2f}kg')
elif unidade == 'L':
    conversao = peso / 0.4536
    print(f'{peso}kg são {conversao:.2f} libras')
else:
    print(f'{unidade} não é uma unidade válida!')
