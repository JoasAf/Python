frase = input("Digite algo!: ").lower().strip()

print(frase,'\n'
            'Quantas vezes a letra "a" aparece na frase?: {}\n'
            'Em qual posição ela apareceu na primeira vez?: {}\n'
            'Em qual posição ela apareceu na última vez?: {}'.format(frase.count('a'),
                                                                     frase.find('a')+1, frase.rfind('a')+1))
