from des109 import moeda

v = int(input('Digite um valor: '))
print(f'O dobro de {v} é {moeda.dobro(v)}')
print(f'A metade de {v} é {moeda.metade(v)}')
print(f'{v} mais 10% é {moeda.aumentar(v, 10, True)}')
print(f'{v} menos 20% é {moeda.reduzir(v, 20, True)}')