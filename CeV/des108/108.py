from des108 import moeda

v = int(input('Digite um valor: '))
print(f'O dobro de {moeda.moeda(v)} é {moeda.moeda(moeda.dobro(v))}')
print(f'A metade de {moeda.moeda(v)} é {moeda.moeda(moeda.metade(v))}')
print(f'{moeda.moeda(v)} mais 10% é {moeda.moeda(moeda.aumentar(v, 10))}')
print(f'{moeda.moeda(v)} menos 20% é {moeda.moeda(moeda.reduzir(v, 20))}')