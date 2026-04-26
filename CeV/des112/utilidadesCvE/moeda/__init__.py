def moeda(v, moe = 'R$'):
    return f'{moe}{v:.2f}'.replace('.', ',')


def aumentar(v = 0, p = 0, f = True ):
    res =  v * (1+p/100)
    return res if f == False else moeda(res)


def reduzir(v = 0, p = 0, f = True ):
    res =  v * (1-p/100)
    return res if f == False else moeda(res)


def dobro(v = 0, f = True ):
    res =  v*2
    return res if f == False else moeda(res)


def metade(v = 0, f = True ):
    res =  v/2
    return res if f == False else moeda(res)


def resumo(v, p1, p2):
    print('-'*30)
    print(f'{'RESUMO DO VALOR':^30}')
    print('-'*30)
    print(f'Preço digitado: {moeda(v)}')
    print(f'Preço dobrado: {dobro(v)}')
    print(f'Metade do preço: {metade(v)}')
    print(f'Aumento de {p1}%: {aumentar(v, p1)}')
    print(f'Redução de {p2}%: {reduzir(v, p2)}')
    print('-'*30)
