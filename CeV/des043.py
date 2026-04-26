a = float(input('Qual é a sua altura?(cm): '))/100
p = float(input('Qual é o seu peso?(kg): '))
imc = p/a**2
if imc<18.5:
    print('Seu IMC é {:.2f} e você está abaixo do peso'.format(imc))
elif 18.5<=imc<25:
    print('Seu IMC é {:.2f} e você está no peso ideal'.format(imc))
elif 25<=imc<30:
    print('Sue IMC é {:.2f} e você está com sobrepeso'.format(imc))
elif 30<=imc<40:
    print('Seu IMC é {:.2f} e você está com obesidade'.format(imc))
elif imc>=40:
    print('Seu IMC é {:.2f} e você está com obesidade mórbida'.format(imc))
