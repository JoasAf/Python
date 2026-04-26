# formatação = {:formatos} formata um valor baseado
#                          nos formatos inseridos

# :.(num)f = Arredonda um número para tantas casas decimais
# :(num) = Aloca o valor em tantos espaços
# :0(num) = Aloca o valor em tantos espaços preenchidos com zeros
# :< = Alinha o valor para a esquerda
# :> = Alinha o valor para a direita
# :^ = Alinhas o valor para o centro
# :+ = Coloca um + na frente de números positivos
# :  = Coloca um espaço na frente de números positivos
# :, = Separa milhares por vírgula

preço1 = 12.34
preço2 = -999
preço3 = 59999

print(f'Preço 1 = {preço1:>+10,.2f}')
print(f'Preço 2 = {preço2:>+10,.2f}')
print(f'Preço 3 = {preço3:>+10,.2f}')
