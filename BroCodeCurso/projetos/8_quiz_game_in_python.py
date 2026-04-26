# Quiz Game in Python
from time import sleep

perguntas = (
    'Quantos elementos existem na tabela periódica?',
    'Qual animal põe os maiores ovos?',
    'Qual é o gás mais abundante na atmosfera da Terra?',
    'Quantos ossos existem no corpo humano?',
    'Qual planeta no sistema solar é o mais quente?'
)

opções = (
    ('A) 116', 'B) 117', 'C) 118', 'D) 119'),
    ('A) Baleia', 'B) Crocodilo', 'C) Elefante', 'D) Avestruz'),
    ('A) Nitrogênio', 'B) Oxigênio', 'C) Dióxido de Carbono', 'D) Hidrogênio'),
    ('A) 206', 'B) 207', 'C) 208', 'D) 209'),
    ('A) Mercúrio', 'B) Vênus', 'C) Terra', 'D) Marte')
)

respostas = ('C', 'D', 'A', 'A', 'B')

tentativas = []
pontuação = 0

print(f'{" QUIZ GAME EM PYTHON ":=^40}\n')

for num_pergunta, pergunta in enumerate(perguntas):
    print(f'{num_pergunta + 1}- {pergunta}')

    for opção in opções[num_pergunta]:
        print(opção)

    tentativa = input('Resposta: ').strip().upper()
    tentativas.append(tentativa)

    if tentativa == respostas[num_pergunta]:
        print('CERTO!\n')
        pontuação += 1
    else:
        print(f'ERRADO! Resposta certa: {respostas[num_pergunta]}\n')
    sleep(2)
print(f'{" RESULTADO FINAL ":=^40}')
print(f'Tentativas: {" ".join(tentativas)}')
print(f'Respostas: {" ".join(respostas)}')
print(f'Pontuação: {pontuação}/{len(perguntas)} ({pontuação / len(perguntas) * 100:.2f}%)')

# Feito pelo chat Gpt ^


# Código original:

# perguntas = (
#     'Quantos elementos existem na tabela periódica?',
#     'Qual animal põe os maiores ovos?',
#     'Qual é o gás mais abundante na atmosfera da Terra?:',
#     'Quantos ossos existem no corpo humano?',
#     'Qual planeta no sistema solar é o mais quente?'
# )
#
# opções = (
#     ('A) 116', 'B) 117', 'C) 118', 'D) 119'),
#     ('A) Baleia', 'B) Crocodilo', 'C) Elefante', 'D) Avestruz'),
#     ('A) Nitrogênio', 'B) Oxigênio', 'C) Dióxido de Carbono', 'D) Hidrogênio'),
#     ('A) 206', 'B) 207', 'C) 208', 'D) 209'),
#     ('A) Mercúrio', 'B) Vênus', 'C) Terra', 'D) Marte')
# )
#
# respostas = ('C', 'D', 'A', 'A', 'B')
#
#
# tentativas = []
# pontuação = num_pergunta = 0
#
# print(f'{"QUIZ GAME IN PYTHON":-^30}')
#
# for pergunta in perguntas:
#     print(f'{num_pergunta+1}- {pergunta}')
#
#     for opção in opções[num_pergunta]:
#         print(opção)
#
#     tentativa = input('Resposta: ')
#
#     if tentativa == respostas[num_pergunta]:
#         print('CERTO!')
#         pontuação += 1
#     else:
#         print('ERRADO!')
#         print(f'Reposta certa : {respostas[num_pergunta]}')
#
#     num_pergunta += 1
#     tentativas.append(tentativa)
#
# print(f'{"Tentativas:":<12}', end='')
#
# for tentativa in tentativas:
#     print(f'{tentativa}', end=' ')
#
# print()
#
# print(f'{"Respostas:":<12}', end='')
# for resposta in respostas:
#     print(resposta, end= ' ')
#
# print()
#
# print(f'Pontuação: {pontuação/len(perguntas)*100}%')