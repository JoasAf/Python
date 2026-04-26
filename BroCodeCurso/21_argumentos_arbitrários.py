#                           ┌─────────────────────────────────────────────────────────┐
#                           │ *args = permite que passe múltiplos argumentos          │
# Argumentos arbitrários =  │ **kwargs = permite que passe múltiplos argumentos chave │
#                           │ * = operador de desempacotamento                        │
#                           └─────────────────────────────────────────────────────────┘

def mostrar_nome(*args):
    for nome in args:
        print(nome, end=' ')

mostrar_nome('Joás', 'Antônio')

print()

def mostrar_endereço(**kwargs):
    for arg in kwargs.values():
        print(arg, end=', ')

mostrar_endereço(cidade='Blumenau',
                 bairro='Itoupava Norte',
                 rua='Rua São Vicente',
                 num=152)