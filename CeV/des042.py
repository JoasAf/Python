lado1 = float(input('Digite o comprimento da 1ª reta: '))
lado2 = float(input('Digite o comprimento da 2ª reta: '))
lado3 = float(input('Digite o comprimento da 3ª reta: '))

if lado1<lado2+lado3 and lado2<lado1+lado3 and lado3<lado1+lado2:
    if lado1==lado2==lado3:
        print('Você formou um triângulo Equilátero!')
    elif lado1!=lado2!=lado3!=lado1:
        print('Você formou um triângulo Escaleno!')
    else:
        print('Você formou um triângulo Isósceles!')
else:
    print('Não é possível formar um triângulo com essas medidas')
