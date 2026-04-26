s = float(input('Qual é o seu salário?: R$'))
if s> 1250:
    a = 0.1
    print('Você ganhou um aumento de {:.1f}%! Agora seu novo salário é de R${:.2f}'.format(a*100, s*(1+a)+100))
else:
    a = 0.15
    print('Você ganhou um aumento de {:.1f}%! Agora seu novo salário é de R${:.2f}'.format(a*100, s*(1+a)))
