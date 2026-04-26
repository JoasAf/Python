from time import sleep
preco = float(input('Preço do produto a ser pago: R$'))
total = preco
desconto = preco * 0
juros = preco * 0
sleep(0.6)
print('Preço base: \33[32mR${:.2f}'.format(preco))
sleep(0.5)
print('\33[34mInforme a forma de pagamento:')
sleep(0.5)
f = int(input('\33[33mOpção [1]- À vista dinhero/cheque \33[32m(10% desc)\n'
          '\33[33mOpção [2]- À vista no cartão \33[32m(5% desc)\n'
          '\33[33mOpção [3]- Parcelar no cartão \33[31m(mais de 3x, 20% juros)\n'
          '\33[34mOpcão número: '))
sleep(0.5)
if f == 1:
    desconto = preco * 0.1
    total = preco-desconto
    print('\n\33[0mCOMPRA À VISTA DINHERO/CHEQUE\n'
          '\33[34mCálculo:\n'
          'Preço: \33[32mR${:.2f}\n'
          '\33[34mDescontos (10%): \33[36mR${:.2f}\n'
          '\33[34mJuros (0%): \33[31mR${:.2f}\n'
          '\33[34mParcelas: \33[33m{:.0f}\n'
          '\33[34mPrestação: \33[33mR${:.2f}\n'
          '\33[34mTotal: \33[32R${:.2f}'.format(preco, desconto, juros, 0, 0,total))
elif f == 2:
    desconto = preco * 0.05
    total = preco-desconto
    print('\n\33[0mCOMPRA À VISTA CARTÃO\n'
          '\33[34mCálculo:\n'
          'Preço: \33[32nR${:.2f}\n'
          '\33[34mDescontos (5%): \33[36mR${:.2f}\n'
          '\33[34mJuros (0%): \33[31mR${:.2f}\n'
          '\33[34mParcelas: \33[33m{:.0f}\n'
          '\33[34mPrestação: \33[33mR${:.2f}\n'
          '\33[34mTotal: \33[32R${:.2f}'.format(preco, desconto, juros, 0, 0,total))
elif f == 3:
    parcelas = int(input('Em quantas parcelas você vai parcelar?: '))
    if parcelas >= 3:
        juros = preco * 0.2
        total = preco+juros
        print('\n\33[0mCOMPRA PARCELADA\n'
              '\33[34mCálculo:\n'
            'Preço: \33[32mR${:.2f}\n'
            '\33[34mDescontos (0%): \33[36mR${:.2f}\n'
            '\33[34mJuros (20%): \33[31mR${:.2f}\n'
            '\33[34mParcelas: \33[33m{:.0f}\n'
            '\33[34mPrestação: \33[33mR${:.2f}\n'
            '\33[34mTotal: \33[32R${:.2f}'.format(preco, desconto, juros, parcelas, total/parcelas,total))
    elif parcelas == 2:
        print('\n\33[0mCOMPRA PARCELADA\n'
          '\33[34mCálculo:\n'
          'Preço: \33[32mR${:.2f}\n'
          '\33[34mDescontos (0%): \33[36mR${:.2f}\n'
          '\33[34mJuros (20%): \33[31mR${:.2f}\n'
          '\33[34mParcelas: \33[33m{:.0f}\n'
          '\33[34mPrestação: \33[33mR${:.2f}\n'
          '\33[34mTotal: \33[32R${:.2f}'.format(preco, desconto, juros, parcelas, total/parcelas,total))
    elif parcelas == 1:
        desconto = preco * 0.05
        print('\n\33[0mCOMPRA À VISTA CARTÃO\n'
              '\33[34mCálculo:\n'
              'Preço: \33[32mR${:.2f}\n'
              '\33[34mDescontos (5%): \33[36mR${:.2f}\n'
              '\33[34mJuros (0%): \33[31mR${:.2f}\n'
              '\33[34mParcelas: \33[33m{:.0f}\n'
              '\33[34mPrestação: \33[33mR${:.2f}\n'
              '\33[34mTotal: \33[32R${:.2f}'.format(preco, desconto, juros, parcelas, total/parcelas,total))
    else:
        print('\33[31mVocê digitou menos de 1 parcela!')
else:
    print('\33[31mVocê digitou uma opção inexistente!')
