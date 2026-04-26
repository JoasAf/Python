#                            ┌──────────────────────────────────────────────────────────────────────────┐
#                            │ usados para testar se um valor ou variável é encontrado em uma sequência │
# Operadores de associação = │ (string, lista, tupla, conjunto ou dicionário)                           │
#                            │ 1. in                                                                    │
#                            │ 2. not in                                                                │
#                            └──────────────────────────────────────────────────────────────────────────┘


palavra = 'BANANA'

# letra = input('Fale uma letra da palavra secreta: ')
letra = 'Q'

if letra in palavra:
    print(f'Aqui está {letra}')
else:
    print(f'{letra} não foi encontrada')

print('─'*30)


# Conjuntos
periféricos = {'mouse', 'teclado', 'fone'}

# periférico = input('Digite um periférico: ')
periférico = 'fone'

if periférico in periféricos:
    print(f'Nós temos {periférico}')
else:
    print(f'Nós não achamos {periférico}')

print('─'*30)


# Dicionários

datas = {'Natal':'dez/25', 'Páscoa':'abr/20', 'Aniversário':'nov/6'}

# data = input('Digite uma data especial: ').capitalize()
data = 'Aniversário'

if data in datas:
    print(f'{data} é {datas.get(data)}')
else:
    print(f'{data} não encontrado')

print('─'*30)

email = 'joasantoniofranco425'

if '@' in email and '.' in email:
    print('Email válido!')
else:
    print('Email inválido!')
