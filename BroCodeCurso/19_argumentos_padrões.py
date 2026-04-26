# Argumentos padrões: Um argumento padrão para certos parâmetros
#                     Esse argumento é usado sempre que outro não for inserido
#                     Torna as suas funções mais flexíveis, reduzindo o número de argumentos.

from time import sleep


def conta(preço, desconto=0, taxa=5):
    return preço * (1-desconto/100) * (1+taxa/100)

print(f'Conta: R${conta(500):.2f}')


def contagem(fim, começo=0):
    for x in range(começo, fim+1):
        print(x)
        sleep(1)
    print('Acabou!')

contagem(20)