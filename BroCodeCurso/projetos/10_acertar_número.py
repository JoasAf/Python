# Jogo de acertar o número
from random import randint


palpites = 0
menor_num = 1
maior_num = 100
num_computador = randint(menor_num, maior_num)


print(f'Tente adivinhar o número de {menor_num} a {maior_num}!')

while True:

    num_jogador = input('Seu palpite: ')


    if not num_jogador.isdigit() or int(num_jogador) > maior_num or int(num_jogador) < menor_num:
        print(f'Inválido! Digite um número entre {menor_num} e {maior_num}!')
        continue

    else:
        num_jogador = int(num_jogador)

        if num_jogador == num_computador:
            break


        else:
            if num_jogador > maior_num or num_jogador < menor_num:
                print('Esse número está fora de alcance!')
                continue


            else:
                palpites += 1

                if num_jogador > num_computador:
                    print('Errou! Tá muito alto!')

                else:
                    print('Errou! Tá muito baixo!')

print(f'Parabéns era {num_computador}! Você ganhou com {palpites+1} palpites!')
