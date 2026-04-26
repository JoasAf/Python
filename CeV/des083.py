expr = str(input('Digite uma expressão: '))
aber = fec = 0
for simb in expr:   
    if simb == '(':
        aber += 1
    if simb == ')':
        fec += 1
if aber == fec:
    print('Sua expressão é válida!')
else:
    print('Sua expressão é inválida!')