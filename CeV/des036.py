from time import sleep
print('Olá! Prazer em conhecer você!')
sleep(1.5)
print('Então vamos revisar alguns dado antes de liberar o seu empréstimo..')
sleep(2)
valor = float(input('\33[32mQual é o preço da casa que você quer comprar?:\33[0mR$'))
sleep(0.8)
renda = float(input('\33[33mAgora, qual é sua renda mensal?: R$'))
sleep(0.8)
tempo = int(input('\33[37mEm quantos anos você pretende terminar de pagar?: '))*12
sleep(0.8)
prestacao = valor/tempo
print('\33[0mA prestação vai ser de \33[35mR${:.2f}\33[0m por mês'.format(prestacao))
sleep(2)
if prestacao > renda*0.3:
    print('\33[31mAnalisamos e concluimos que não será possível fazer o empréstimo.')
else:
    print('\33[32mEmpréstimo fechado!')