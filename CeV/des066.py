soma = cont = 0
while True:
    n = float(input('Digite algum valor: '))
    if n == 999:
        break
    soma += n
    cont += 1
print(f'Você digitou {cont} valores e a soma foi {soma:.0f}')
