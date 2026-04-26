p = str(input('Digite qualquer coisa: ')).lower().strip().replace(' ', '')
q = p[::-1]
if p == q:
    print('É um palíndromo! {} invertido é {}'.format(p, q))
