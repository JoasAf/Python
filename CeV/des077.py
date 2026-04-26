words=('amor', 'carinho', 'afeto', 'felicidade', 'compaixao',
      'empatia', 'sentileza', 'simpatia', 'afeicao')
for palavra in range(0, len(words)):
    print(f'\nNa palavra {words[palavra]} temos: |', end='')
    for vogais in words[palavra]:
        if vogais in 'aeiou':
            print(vogais, end='|')
