#                       ┌────────────────────────────────────────────────────────┐
#                       │ É um jeito conciso de criar listas em python           │
#  Lista compreensiva = │ Mais compacto e fácil de ler doq os tradicionais loops │
#                       │ [expressão for (valor) in (iterável) if (condição)]     │
#                       └────────────────────────────────────────────────────────┘

dobros = [x * 2 for x in range(1, 6)]
# for x in range(1, 6):
#     dobros.append(x*2)

print(f'Dobros: {dobros}')


print('─'*30)

triplos = [y * 3 for y in range(1, 6)]

print(f'Triplos: {triplos}')


print('─'*30)

compras = ['arroz', 'feijão', 'banana', 'leite']
compras = [compra.upper() for compra in compras]

print(f'Compras maiúsculas: {compras}')


print('─'*30)

números = [-1, -2, 3, -4, 5, 6]

números_positivos = [núm for núm in números if núm >= 0]
números_negativos = [núm for núm in números if núm < 0]
números_pares = [núm for núm in números if núm%2==0]
números_ímpares = [núm for núm in números if núm%2==1]

print(f'Números positivos: {números_positivos}')
print(f'Números negativos: {números_negativos}')
print(f'Números pares: {números_pares}')
print(f'Números ímpares: {números_ímpares}')


print('─'*30)

notas = [99, 45, 65, 76, 13, 89]

aprovados = [nota for nota in notas if nota >=70]
reprovados = [nota for nota in notas if nota <70]

print(f'Aprovados: {aprovados}')
print(f'Reprovados: {reprovados}')