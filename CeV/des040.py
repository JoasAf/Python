nota1 = float(input('1ª nota: '))
nota2 = float(input('2ª nota: '))
media = (nota1+nota2)/2
if media >= 7:
    print('\33[32mAluno aprovado. Média: {:.2f}'.format(media))
elif media < 5:
    print('\33[31mAluno repovado. Média: {:.2f}'.format(media))
else:
    print('\33[33mRecuperação. Média: {:.2f}'.format(media))
