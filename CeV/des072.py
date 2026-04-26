numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
num = int(input('Escolha um número de 0 a 20 para ver sua versão extensa: '))
while num<0 or num>20:
    num = int(input('Tente novamente: '))
print(f'{num} por extenso é {numeros[num]}')