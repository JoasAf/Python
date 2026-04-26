# Jogo da Forca em Pithon

palavras = ("abacaxi", "elefante", "computador", "biblioteca", "montanha", 
            "escola", "cachorro", "brinquedo", "girassol", "amarelo", 
            "astronauta", "passarinho", "diamante", "helicóptero", "bicicleta", 
            "piano", "desenho", "borboleta", "pipoca", "camarão", 
            "esmeralda", "nuvem", "castelo", "dicionário", "vassoura", 
            "sapato", "telefone", "geladeira", "planeta", "ocelote", 
            "futebol", "canguru", "salsicha", "jardim", "quadro", 
            "livro", "chocolate", "paralelepípedo", "zebra", "arco-íris", 
            "macaco", "martelo", "ventilador", "praia", "leopardo", 
            "oceano", "abelha", "formiga", "espelho", "tigre")


homem = {0:('  ',
            '  ',
            '  '),
         1:(' O ',
            '  ',
            '  '),
         2:(' O ',
            ' | ',
            '  '),
         3:(' O ',
            '/| ',
            '  '),
         4:(' O ',
            '/|\\',
            '  '),
         5:(' O ',
            '/|\\',
            '/  '),
         6:(' O ',
            '/|\\',
            '/ \\')}

def mostrar_homem(erros):
    print('*'*30)
    for linha in homem[erros]:
        print(linha)
    print('*'*30)

def mostrar_dica(dica):
    print(' '.join(dica))

def mostrar_resp(palavra):
    print(''.join(palavra))

def main():
    from random import choice as chc
    from time import sleep as slp
    funcionando = True
    palavra = chc(palavras)
    palpites = set()
    dica = ['_'] * len(palavra)
    erros = 0

    while funcionando:
        mostrar_homem(erros)
        mostrar_dica(dica)

        palpite = input('Letra: ').lower()

        if len(palpite) != 1 or not palpite.isalnum:
            print('Escolha apenas uma letra!')
            slp(2)
            continue
        
        if palpite in palpites:
            print(f'"{palpite}" já foi escolhida')
            slp(2)
            continue

        palpites.add(palpite)
        
        if palpite in palavra:
            for l in range(len(palavra)):
                if palavra[l] == palpite:
                    dica[l] = palpite
        else:
            erros +=1

        if '_' not in dica:
            mostrar_homem(erros)
            mostrar_resp(palavra)
            print('Ganhou!!')
            funcionando = False

        if erros == 6:
            mostrar_homem(erros)
            mostrar_resp(palavra)
            print('Perdeu!!')
            funcionando = False


if __name__ == '__main__':
    main()
