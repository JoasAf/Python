# Calculadora de juros compostos em python

while True:
    valor = float(input('Valor: R$'))

    if valor <0:
        print(f'"{valor}" não é válido!')
        continue
    break

while True:
    taxa = float(input('Taxa (a.a): '))
    if taxa < 0:
        print(f'"{taxa}" não é válido!')
        continue
    break

while True:
    tempo = int(input('Tempo: '))
    if tempo < 0:
        print(f'"{tempo}" não é válido!')
        continue

    total = valor*(1+taxa/100)**tempo
    print(f'Total é R${total:.2f}')
    break