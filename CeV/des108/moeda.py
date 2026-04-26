def moeda(v, moe = 'R$'):
    return f'{moe}{v:.2f}'

def aumentar(v = 0, p = 0):
    return v * (1+p/100)

def reduzir(v = 0, p = 0):
    return v * (1-p/100)

def dobro(v = 0):
    return v*2

def metade(v = 0):
    return v/2
