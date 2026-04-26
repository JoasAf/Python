def moeda(v, moe = 'R$'):
    return f'{moe}{v:.2f}'


def aumentar(v = 0, p = 0, f = False):
    res =  v * (1+p/100)
    return res if f == False else moeda(res)


def reduzir(v = 0, p = 0, f = False):
    res =  v * (1-p/100)
    return res if f == False else moeda(res)


def dobro(v = 0, f = False):
    res =  v*2
    return res if f == False else moeda(res)


def metade(v = 0, f = False):
    res =  v/2
    return res if f == False else moeda(res)
