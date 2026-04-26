# Decorator = Uma função que se estende a outra função
#             Sem modificar a função base
#             Passa a função base como um argumento para o decorator

#             @adicionar_granulado
#             pegar_sorvete("chocolate")

def adicionar_granulado(func):
    def wrapper(*a):
        print('Adicionando granulado 🫘')
        func(*a)
    return wrapper

def adicionar_cobertura(func):
    def wrapper(*a):
        print('Adicionando cobertura🍫')
        func(*a)
    return wrapper

@adicionar_cobertura
@adicionar_granulado
def pegar_sorvete(sabor):
    print(f'Aqui está seu sorvete de {sabor} 🍦')

pegar_sorvete('chocolate')