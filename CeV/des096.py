def área(h, w):
    a = h * w
    print(f'A área de um terreno {h:.1f}x{w:.1f} é {a:.1f}m².')


área(float(input('Altura(m): ')),
     float(input('Largura(m): ')))