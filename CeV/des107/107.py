from des107 import moeda

v = int(input('Digite um valor: '))
print(f'O dobro de R${v:.2f} é R${moeda.dobro(v):.2f}')
print(f'A metade de R${v:.2f} é R${moeda.metade(v):.2f}')
print(f'R${v:.2f} mais 10% é R${moeda.aumentar(v, 10):.2f}')
print(f'R${v:.2f} menos 20% é R${moeda.reduzir(v, 20):.2f}')